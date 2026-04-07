"""
Round-based online MI bridge for nearalQT.

Purpose:
1. Parse nearalQT motor-imagery session logs.
2. Extract 4-second imagery trials from two-channel EEG.
3. Downsample each trial to 1000 points to match the thesis low-channel model input.
4. Train or update a subject-specific model after each completed round.
5. Run per-trial inference in the next round and return JSON for Qt display.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import torch
import torch.nn as nn
from scipy import signal
from sklearn.model_selection import train_test_split

from conformer_lowchannel_b2_diff import ConformerB2


LABEL_TO_INDEX = {
    "Left Hand": 0,
    "Right Hand": 1,
}

INDEX_TO_LABEL = {
    0: "Left Hand",
    1: "Right Hand",
}

PRETRAINED_CHECKPOINT = Path(
    r"C:\Users\qzwsw\Documents\thesis\02_Source_Material\04_Algorithm_Workbench\results\2b_pretrain_transfer\weights\conformer_b2_c3c4_pretrain_2b.pt"
)
PREPROCESS_DESC = "phase_4s_imagery -> 8-30Hz bandpass -> resample_1000 -> per_trial_channel_zscore"


@dataclass
class TrialSample:
    trial_index: int
    cue: str
    samples: np.ndarray  # shape [2, n]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="nearalQT online MI bridge")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for sub in ("train-round", "infer-trial"):
        p = subparsers.add_parser(sub)
        p.add_argument("--summary", required=True, help="Path to MI summary csv")
        p.add_argument("--raw", required=True, help="Path to MI raw EEG csv")
        p.add_argument("--runtime-root", required=True, help="Runtime storage root")
        p.add_argument("--epochs", type=int, default=24)
        p.add_argument("--lr", type=float, default=2e-4)
        p.add_argument("--seed", type=int, default=42)

    infer = subparsers.choices["infer-trial"]
    infer.add_argument("--trial-index", type=int, required=True)

    return parser.parse_args()


def load_trial_cues(summary_path: Path) -> Dict[int, str]:
    cues: Dict[int, str] = {}
    with summary_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                trial_index = int(row["trial_index"])
            except (KeyError, TypeError, ValueError):
                continue
            cue = row.get("cue_label", "").strip()
            if cue in LABEL_TO_INDEX:
                cues[trial_index] = cue
    return cues


def load_imagery_trials(raw_path: Path, summary_path: Path) -> List[TrialSample]:
    cues = load_trial_cues(summary_path)
    grouped: Dict[int, Dict[str, List[float]]] = {}

    with raw_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            phase = row.get("phase", "").strip().strip('"')
            if phase != "Imagery":
                continue
            try:
                trial_index = int(row["trial_index"])
                ch0 = float(row["ch0_uv"])
                ch1 = float(row["ch1_uv"])
            except (KeyError, TypeError, ValueError):
                continue

            cue = row.get("cue_label", "").strip().strip('"')
            cue = cue if cue in LABEL_TO_INDEX else cues.get(trial_index, "")
            if cue not in LABEL_TO_INDEX:
                continue

            bucket = grouped.setdefault(trial_index, {"cue": cue, "ch0": [], "ch1": []})
            bucket["ch0"].append(ch0)
            bucket["ch1"].append(ch1)

    trials: List[TrialSample] = []
    for trial_index in sorted(grouped):
        item = grouped[trial_index]
        arr = np.stack(
            [
                np.asarray(item["ch0"], dtype=np.float32),
                np.asarray(item["ch1"], dtype=np.float32),
            ],
            axis=0,
        )
        trials.append(TrialSample(trial_index=trial_index, cue=item["cue"], samples=arr))
    return trials


def resample_to_target(samples: np.ndarray, target_points: int = 1000) -> np.ndarray:
    if samples.ndim != 2 or samples.shape[0] != 2:
        raise ValueError("Expected samples shaped [2, n_points].")

    current_points = samples.shape[1]
    if current_points == target_points:
        return samples.astype(np.float32, copy=False)

    x_old = np.linspace(0.0, 1.0, current_points, dtype=np.float32)
    x_new = np.linspace(0.0, 1.0, target_points, dtype=np.float32)
    resampled = np.empty((2, target_points), dtype=np.float32)
    for ch in range(2):
        resampled[ch] = np.interp(x_new, x_old, samples[ch]).astype(np.float32)
    return resampled


def butter_bandpass(samples: np.ndarray, fs: float = 500.0, low: float = 8.0, high: float = 30.0) -> np.ndarray:
    sos = signal.butter(4, [low, high], btype="bandpass", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, samples, axis=1).astype(np.float32)


def channelwise_zscore(samples: np.ndarray) -> np.ndarray:
    mean = samples.mean(axis=1, keepdims=True)
    std = samples.std(axis=1, keepdims=True)
    std[std < 1e-6] = 1.0
    return ((samples - mean) / std).astype(np.float32)


def preprocess_trial_samples(samples: np.ndarray) -> np.ndarray:
    x = samples.astype(np.float32, copy=False)
    x = x - x.mean(axis=1, keepdims=True)
    x = butter_bandpass(x, fs=500.0, low=8.0, high=30.0)
    x = resample_to_target(x, target_points=1000)
    x = channelwise_zscore(x)
    return x


def trials_to_dataset(trials: List[TrialSample]) -> Tuple[np.ndarray, np.ndarray, List[int]]:
    xs: List[np.ndarray] = []
    ys: List[int] = []
    idxs: List[int] = []

    for trial in trials:
        if trial.cue not in LABEL_TO_INDEX:
            continue
        if trial.samples.shape[1] < 200:
            continue
        x = preprocess_trial_samples(trial.samples)
        xs.append(np.expand_dims(x, axis=0))  # [1, 2, 1000]
        ys.append(LABEL_TO_INDEX[trial.cue])
        idxs.append(trial.trial_index)

    if not xs:
        raise RuntimeError("No valid imagery trials were found in this session.")

    x_arr = np.stack(xs, axis=0).astype(np.float32)  # [N, 1, 2, 1000]
    y_arr = np.asarray(ys, dtype=np.int64)
    return x_arr, y_arr, idxs


def ensure_runtime_paths(runtime_root: Path) -> Dict[str, Path]:
    runtime_root.mkdir(parents=True, exist_ok=True)
    datasets_dir = runtime_root / "datasets"
    models_dir = runtime_root / "models"
    reports_dir = runtime_root / "reports"
    datasets_dir.mkdir(parents=True, exist_ok=True)
    models_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    return {
        "root": runtime_root,
        "datasets": datasets_dir,
        "models": models_dir,
        "reports": reports_dir,
        "accumulated_npz": datasets_dir / "accumulated_rounds.npz",
        "latest_model": models_dir / "latest_model.pth",
        "latest_meta": models_dir / "latest_model_meta.json",
    }


def append_round_data(runtime_paths: Dict[str, Path], x_round: np.ndarray, y_round: np.ndarray,
                      summary_path: Path, raw_path: Path) -> Tuple[np.ndarray, np.ndarray]:
    acc_path = runtime_paths["accumulated_npz"]
    if acc_path.exists():
        previous = np.load(acc_path, allow_pickle=False)
        x_all = np.concatenate([previous["x"], x_round], axis=0)
        y_all = np.concatenate([previous["y"], y_round], axis=0)
    else:
        x_all = x_round
        y_all = y_round

    np.savez_compressed(
        acc_path,
        x=x_all.astype(np.float32),
        y=y_all.astype(np.int64),
        source_summary=str(summary_path),
        source_raw=str(raw_path),
    )
    return x_all, y_all


def make_model(device: torch.device) -> ConformerB2:
    model = ConformerB2(
        n_channels=2,
        n_classes=2,
        window_size=8,
        use_diff_branch=True,
    )
    return model.to(device)


def extract_state_dict(obj):
    if isinstance(obj, dict) and "state_dict" in obj and isinstance(obj["state_dict"], dict):
        return obj["state_dict"]
    return obj


def load_initial_weights(model: ConformerB2, runtime_paths: Dict[str, Path], device: torch.device) -> str:
    latest_model = runtime_paths["latest_model"]
    if latest_model.exists():
        state = torch.load(latest_model, map_location=device)
        model.load_state_dict(extract_state_dict(state), strict=False)
        return str(latest_model)

    if PRETRAINED_CHECKPOINT.exists():
        state = torch.load(PRETRAINED_CHECKPOINT, map_location=device)
        model.load_state_dict(extract_state_dict(state), strict=False)
        return str(PRETRAINED_CHECKPOINT)

    return "random_init"


def split_train_val(x_all: np.ndarray, y_all: np.ndarray, seed: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    class_counts = np.bincount(y_all, minlength=2)
    if np.min(class_counts) >= 2 and len(y_all) >= 8:
        return train_test_split(
            x_all,
            y_all,
            test_size=0.2,
            random_state=seed,
            stratify=y_all,
        )
    return x_all, x_all, y_all, y_all


def normalize_sets(x_train: np.ndarray, x_val: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float, float]:
    mean = float(x_train.mean())
    std = float(x_train.std())
    if std < 1e-6:
        std = 1.0
    x_train = (x_train - mean) / std
    x_val = (x_val - mean) / std
    return x_train, x_val, mean, std


def train_round(args: argparse.Namespace) -> None:
    runtime_paths = ensure_runtime_paths(Path(args.runtime_root))
    summary_path = Path(args.summary)
    raw_path = Path(args.raw)
    latest_model = runtime_paths["latest_model"]

    trials = load_imagery_trials(raw_path, summary_path)
    x_round, y_round, trial_indices = trials_to_dataset(trials)
    x_all, y_all = append_round_data(runtime_paths, x_round, y_round, summary_path, raw_path)

    x_train, x_val, y_train, y_val = split_train_val(x_all, y_all, args.seed)
    x_train, x_val, mean, std = normalize_sets(x_train, x_val)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = make_model(device)
    init_source = load_initial_weights(model, runtime_paths, device)

    train_tensor = torch.from_numpy(x_train).float().to(device)
    train_label = torch.from_numpy(y_train).long().to(device)
    val_tensor = torch.from_numpy(x_val).float().to(device)
    val_label = torch.from_numpy(y_val).long().to(device)

    batch_size = max(4, min(16, len(train_tensor)))
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    best_state = None
    best_acc = -1.0
    last_train_acc = 0.0
    epochs = max(6, int(args.epochs))

    for _epoch in range(epochs):
        model.train()
        perm = torch.randperm(train_tensor.size(0), device=device)
        correct = 0
        seen = 0

        for start in range(0, train_tensor.size(0), batch_size):
            idx = perm[start:start + batch_size]
            xb = train_tensor[idx]
            yb = train_label[idx]
            _, logits = model(xb)
            loss = criterion(logits, yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            pred = logits.argmax(dim=1)
            correct += int((pred == yb).sum().item())
            seen += int(yb.numel())

        last_train_acc = float(correct / max(1, seen))

        model.eval()
        with torch.no_grad():
            _, val_logits = model(val_tensor)
            val_pred = val_logits.argmax(dim=1)
            val_acc = float((val_pred == val_label).float().mean().item())

        if val_acc >= best_acc:
            best_acc = val_acc
            best_state = {k: v.detach().cpu() for k, v in model.state_dict().items()}

    if best_state is None:
        best_state = {k: v.detach().cpu() for k, v in model.state_dict().items()}

    torch.save(best_state, latest_model)
    meta = {
        "status": "ok",
        "device": str(device),
        "round_trials": int(len(x_round)),
        "round_trial_indices": trial_indices,
        "samples_total": int(len(x_all)),
        "train_accuracy": last_train_acc,
        "validation_accuracy": best_acc,
        "epochs": epochs,
        "mean": mean,
        "std": std,
        "preprocessing": PREPROCESS_DESC,
        "initialization_source": init_source,
        "model_path": str(latest_model),
        "label_map": INDEX_TO_LABEL,
        "source_summary": str(summary_path),
        "source_raw": str(raw_path),
    }
    runtime_paths["latest_meta"].write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False))


def load_latest_meta(runtime_paths: Dict[str, Path]) -> Dict[str, object]:
    meta_path = runtime_paths["latest_meta"]
    if not meta_path.exists():
        raise RuntimeError("No trained MI model metadata found.")
    return json.loads(meta_path.read_text(encoding="utf-8"))


def infer_trial(args: argparse.Namespace) -> None:
    runtime_paths = ensure_runtime_paths(Path(args.runtime_root))
    meta = load_latest_meta(runtime_paths)

    trials = load_imagery_trials(Path(args.raw), Path(args.summary))
    target = None
    for trial in trials:
        if trial.trial_index == args.trial_index:
            target = trial
            break

    if target is None:
        raise RuntimeError(f"Trial {args.trial_index} not found in raw MI log.")

    x = preprocess_trial_samples(target.samples)
    x = np.expand_dims(np.expand_dims(x, axis=0), axis=0).astype(np.float32)

    mean = float(meta.get("mean", 0.0))
    std = float(meta.get("std", 1.0))
    if std < 1e-6:
        std = 1.0
    x = (x - mean) / std

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = make_model(device)
    state = torch.load(runtime_paths["latest_model"], map_location=device)
    model.load_state_dict(extract_state_dict(state), strict=False)
    model.eval()

    with torch.no_grad():
        xb = torch.from_numpy(x).float().to(device)
        _, logits = model(xb)
        probs = torch.softmax(logits, dim=1).detach().cpu().numpy()[0]
        pred_index = int(np.argmax(probs))

    result = {
        "status": "ok",
        "trial_index": int(args.trial_index),
        "cue_label": target.cue,
        "predicted_label": INDEX_TO_LABEL[pred_index],
        "confidence": float(probs[pred_index]),
        "prob_left": float(probs[0]),
        "prob_right": float(probs[1]),
        "model_path": str(runtime_paths["latest_model"]),
        "preprocessing": meta.get("preprocessing", PREPROCESS_DESC),
    }
    print(json.dumps(result, ensure_ascii=False))


def main() -> None:
    args = parse_args()
    try:
        if args.command == "train-round":
            train_round(args)
        elif args.command == "infer-trial":
            infer_trial(args)
        else:
            raise RuntimeError(f"Unsupported command: {args.command}")
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False))
        raise


if __name__ == "__main__":
    main()
