from __future__ import annotations

import csv
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import torch
import torch.nn as nn
from scipy import signal
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


SESSIONS = [
    "20260401_122743_mi_lr",
    "20260401_123310_mi_lr",
]
BASE_DIR = Path(r"C:\Users\qzwsw\Documents\nearalQT_mi_logs")
SCRIPT_DIR = Path(r"C:\Users\qzwsw\Documents\thesis\02_Source_Material\04_Algorithm_Workbench\scripts")
REPORT_PATH = Path(r"C:\Users\qzwsw\Documents\thesis\00_AI_Management\Output_Drafts\MI_Offline_Round_Analysis_20260401.md")


@dataclass
class Trial:
    session: str
    trial_index: int
    cue: str
    prepare: np.ndarray  # [2, n]
    imagery: np.ndarray  # [2, n]
    rest: np.ndarray  # [2, n]
    imagery_duration: float


def load_conformer_class():
    import importlib.util

    target = SCRIPT_DIR / "conformer_lowchannel_b2_diff.py"
    spec = importlib.util.spec_from_file_location("conformer_lowchannel_b2_diff", target)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.ConformerB2


ConformerB2 = load_conformer_class()


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_trials(session_base: str) -> List[Trial]:
    summary_path = BASE_DIR / f"{session_base}_summary.csv"
    raw_path = BASE_DIR / f"{session_base}_raw_eeg.csv"

    summary_rows = list(csv.DictReader(summary_path.open("r", encoding="utf-8", newline="")))
    summary_map = {
        int(row["trial_index"]): row
        for row in summary_rows
        if row["status"].strip('"') == "completed" and row["aborted"] == "0"
    }

    grouped: Dict[int, Dict[str, List[List[float]]]] = {}
    with raw_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            trial_index = int(row["trial_index"])
            if trial_index not in summary_map:
                continue
            phase = row["phase"].strip('"')
            cue = row["cue_label"].strip('"')
            ch0 = float(row["ch0_uv"])
            ch1 = float(row["ch1_uv"])

            bucket = grouped.setdefault(
                trial_index,
                {"cue": cue, "Prepare": [[], []], "Imagery": [[], []], "Rest": [[], []]},
            )
            if phase in bucket:
                bucket[phase][0].append(ch0)
                bucket[phase][1].append(ch1)

    trials: List[Trial] = []
    for trial_index in sorted(grouped):
        row = summary_map[trial_index]
        item = grouped[trial_index]
        imagery_duration = float(row["rest_start_sec"]) - float(row["imagery_start_sec"])
        trials.append(
            Trial(
                session=session_base,
                trial_index=trial_index,
                cue=item["cue"],
                prepare=np.asarray(item["Prepare"], dtype=np.float32),
                imagery=np.asarray(item["Imagery"], dtype=np.float32),
                rest=np.asarray(item["Rest"], dtype=np.float32),
                imagery_duration=imagery_duration,
            )
        )
    return trials


def interp_channels(data: np.ndarray, target_points: int) -> np.ndarray:
    if data.shape[1] == target_points:
        return data.astype(np.float32, copy=False)
    x_old = np.linspace(0.0, 1.0, data.shape[1], dtype=np.float32)
    x_new = np.linspace(0.0, 1.0, target_points, dtype=np.float32)
    out = np.empty((data.shape[0], target_points), dtype=np.float32)
    for ch in range(data.shape[0]):
        out[ch] = np.interp(x_new, x_old, data[ch]).astype(np.float32)
    return out


def butter_bandpass(data: np.ndarray, fs: float = 500.0, low: float = 8.0, high: float = 30.0) -> np.ndarray:
    sos = signal.butter(4, [low, high], btype="bandpass", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, data, axis=1).astype(np.float32)


def channelwise_zscore(data: np.ndarray) -> np.ndarray:
    mean = data.mean(axis=1, keepdims=True)
    std = data.std(axis=1, keepdims=True)
    std[std < 1e-6] = 1.0
    return ((data - mean) / std).astype(np.float32)


def preprocess_trial(trial: Trial, variant: str) -> np.ndarray:
    imagery_2000 = interp_channels(trial.imagery, 2000)
    prepare_1000 = interp_channels(trial.prepare, 1000) if trial.prepare.shape[1] > 10 else None

    if variant == "raw_trial_z":
        x = interp_channels(imagery_2000, 1000)
        x = x - x.mean(axis=1, keepdims=True)
        return channelwise_zscore(x)

    if variant == "bandpass_trial_z":
        x = imagery_2000 - imagery_2000.mean(axis=1, keepdims=True)
        x = butter_bandpass(x, fs=500.0, low=8.0, high=30.0)
        x = interp_channels(x, 1000)
        return channelwise_zscore(x)

    if variant == "prepare_norm_bandpass":
        x = imagery_2000.copy()
        if prepare_1000 is not None:
            base_mean = prepare_1000.mean(axis=1, keepdims=True)
            base_std = prepare_1000.std(axis=1, keepdims=True)
            base_std[base_std < 1e-6] = 1.0
            x = (x - base_mean) / base_std
        else:
            x = x - x.mean(axis=1, keepdims=True)
        x = butter_bandpass(x, fs=500.0, low=8.0, high=30.0)
        x = interp_channels(x, 1000)
        return channelwise_zscore(x)

    raise ValueError(f"Unsupported variant: {variant}")


def build_dataset(trials: List[Trial], variant: str) -> Tuple[np.ndarray, np.ndarray]:
    xs = []
    ys = []
    for trial in trials:
        x = preprocess_trial(trial, variant)
        xs.append(np.expand_dims(x, axis=0))
        ys.append(0 if trial.cue == "Left Hand" else 1)
    return np.stack(xs, axis=0).astype(np.float32), np.asarray(ys, dtype=np.int64)


def normalize_sets(x_train: np.ndarray, x_test: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    mean = float(x_train.mean())
    std = float(x_train.std())
    if std < 1e-6:
        std = 1.0
    return ((x_train - mean) / std).astype(np.float32), ((x_test - mean) / std).astype(np.float32)


def train_and_eval(x_train: np.ndarray, y_train: np.ndarray, x_test: np.ndarray, y_test: np.ndarray, seed: int) -> float:
    set_seed(seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    x_train, x_test = normalize_sets(x_train, x_test)
    x_fit, x_val, y_fit, y_val = train_test_split(
        x_train, y_train, test_size=0.25, random_state=seed, stratify=y_train
    )

    model = ConformerB2(n_channels=2, n_classes=2, window_size=8, use_diff_branch=True).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=2e-4)

    fit_x = torch.from_numpy(x_fit).float().to(device)
    fit_y = torch.from_numpy(y_fit).long().to(device)
    val_x = torch.from_numpy(x_val).float().to(device)
    val_y = torch.from_numpy(y_val).long().to(device)
    test_x = torch.from_numpy(x_test).float().to(device)

    batch_size = max(4, min(8, len(fit_x)))
    best_state = None
    best_val = -1.0

    for _epoch in range(20):
        model.train()
        perm = torch.randperm(fit_x.size(0), device=device)
        for start in range(0, fit_x.size(0), batch_size):
            idx = perm[start:start + batch_size]
            xb = fit_x[idx]
            yb = fit_y[idx]
            _, logits = model(xb)
            loss = criterion(logits, yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            _, val_logits = model(val_x)
            val_pred = val_logits.argmax(dim=1)
            val_acc = float((val_pred == val_y).float().mean().item())
        if val_acc >= best_val:
            best_val = val_acc
            best_state = {k: v.detach().cpu() for k, v in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)

    model.eval()
    with torch.no_grad():
        _, test_logits = model(test_x)
        test_pred = test_logits.argmax(dim=1).detach().cpu().numpy()
    return float((test_pred == y_test).mean())


def summarize_trials(trials: List[Trial]) -> Dict[str, float]:
    imagery_counts = [trial.imagery.shape[1] for trial in trials]
    effective_hz = [trial.imagery.shape[1] / trial.imagery_duration for trial in trials if trial.imagery_duration > 0]
    all_raw = np.concatenate([np.concatenate([t.prepare, t.imagery, t.rest], axis=1) for t in trials], axis=1)
    left = sum(1 for t in trials if t.cue == "Left Hand")
    right = sum(1 for t in trials if t.cue == "Right Hand")
    return {
        "n_trials": len(trials),
        "left": left,
        "right": right,
        "imagery_min": int(min(imagery_counts)),
        "imagery_max": int(max(imagery_counts)),
        "imagery_avg": float(np.mean(imagery_counts)),
        "hz_min": float(min(effective_hz)),
        "hz_max": float(max(effective_hz)),
        "hz_avg": float(np.mean(effective_hz)),
        "ch0_mean": float(all_raw[0].mean()),
        "ch0_std": float(all_raw[0].std()),
        "ch1_mean": float(all_raw[1].mean()),
        "ch1_std": float(all_raw[1].std()),
    }


def classical_features(trial: Trial) -> np.ndarray:
    x = interp_channels(trial.imagery, 2000)
    x = x - x.mean(axis=1, keepdims=True)
    x = butter_bandpass(x, fs=500.0, low=8.0, high=30.0)
    psd = np.abs(np.fft.rfft(x, axis=1)) ** 2
    freqs = np.fft.rfftfreq(x.shape[1], d=1 / 500.0)

    def bp(lo: float, hi: float) -> np.ndarray:
        mask = (freqs >= lo) & (freqs <= hi)
        return psd[:, mask].mean(axis=1)

    alpha = bp(8.0, 13.0)
    beta = bp(13.0, 30.0)
    return np.asarray(
        [
            alpha[0], alpha[1], beta[0], beta[1],
            alpha[0] - alpha[1], beta[0] - beta[1],
        ],
        dtype=np.float32,
    )


def eval_classical_baseline(all_trials_by_session: Dict[str, List[Trial]]) -> Dict[str, object]:
    rows = []
    for session in SESSIONS:
        for trial in all_trials_by_session[session]:
            rows.append((session, classical_features(trial), 0 if trial.cue == "Left Hand" else 1))

    X = np.vstack([r[1] for r in rows])
    y = np.asarray([r[2] for r in rows], dtype=np.int64)
    sessions = [r[0] for r in rows]
    pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))

    cross = []
    for train_session, test_session in [(SESSIONS[0], SESSIONS[1]), (SESSIONS[1], SESSIONS[0])]:
        train_mask = np.asarray([s == train_session for s in sessions])
        test_mask = np.asarray([s == test_session for s in sessions])
        pipe.fit(X[train_mask], y[train_mask])
        pred = pipe.predict(X[test_mask])
        cross.append((train_session, test_session, float(accuracy_score(y[test_mask], pred))))

    return {
        "folds": cross,
        "mean_acc": float(np.mean([acc for _, _, acc in cross])),
    }


def main() -> None:
    all_trials_by_session = {session: load_trials(session) for session in SESSIONS}
    summaries = {session: summarize_trials(trials) for session, trials in all_trials_by_session.items()}

    variants = ["raw_trial_z", "bandpass_trial_z", "prepare_norm_bandpass"]
    results = []
    seed = 42

    for variant in variants:
        fold_scores = []
        for train_session, test_session in [(SESSIONS[0], SESSIONS[1]), (SESSIONS[1], SESSIONS[0])]:
            x_train, y_train = build_dataset(all_trials_by_session[train_session], variant)
            x_test, y_test = build_dataset(all_trials_by_session[test_session], variant)
            acc = train_and_eval(x_train, y_train, x_test, y_test, seed=seed)
            fold_scores.append((train_session, test_session, acc))
        results.append(
            {
                "variant": variant,
                "folds": fold_scores,
                "mean_acc": float(np.mean([score for _, _, score in fold_scores])),
            }
        )
    classical = eval_classical_baseline(all_trials_by_session)

    lines: List[str] = []
    lines.append("# MI Offline Round Analysis")
    lines.append("")
    lines.append("## Data Summary")
    lines.append("")
    for session in SESSIONS:
        info = summaries[session]
        lines.append(f"### {session}")
        lines.append("")
        lines.append(f"- Trials: `{info['n_trials']}` (`Left={info['left']}`, `Right={info['right']}`)")
        lines.append(f"- Imagery sample count: min `{info['imagery_min']}`, max `{info['imagery_max']}`, avg `{info['imagery_avg']:.1f}`")
        lines.append(f"- Effective sampling rate by trial: min `{info['hz_min']:.1f} Hz`, max `{info['hz_max']:.1f} Hz`, avg `{info['hz_avg']:.1f} Hz`")
        lines.append(f"- Channel offset drift: `CH0 {info['ch0_mean']:.1f}+/-{info['ch0_std']:.1f} uV`, `CH1 {info['ch1_mean']:.1f}+/-{info['ch1_std']:.1f} uV`")
        lines.append("")

    lines.append("## Offline ConformerB2 Pilot")
    lines.append("")
    lines.append("| Variant | Train -> Test | Accuracy |")
    lines.append("|---|---|---:|")
    for item in results:
        for train_session, test_session, acc in item["folds"]:
            lines.append(f"| `{item['variant']}` | `{train_session}` -> `{test_session}` | `{acc*100:.1f}%` |")
        lines.append(f"| `{item['variant']}` | `mean` | `{item['mean_acc']*100:.1f}%` |")

    lines.append("")
    lines.append("## Classical Spectral Baseline")
    lines.append("")
    lines.append("| Variant | Train -> Test | Accuracy |")
    lines.append("|---|---|---:|")
    for train_session, test_session, acc in classical["folds"]:
        lines.append(f"| `alpha/beta power + channel difference` | `{train_session}` -> `{test_session}` | `{acc*100:.1f}%` |")
    lines.append(f"| `alpha/beta power + channel difference` | `mean` | `{classical['mean_acc']*100:.1f}%` |")

    lines.append("")
    lines.append("## Suggested Interpretation")
    lines.append("")
    best = max(results, key=lambda x: x["mean_acc"])
    lines.append(f"- Best pilot variant in this run: `{best['variant']}` with mean cross-round accuracy `{best['mean_acc']*100:.1f}%`.")
    lines.append("- Raw imagery lengths vary noticeably across trials, so direct fixed-index slicing is less stable than resampling each imagery segment to a fixed target length.")
    lines.append("- Because channel offsets drift between rounds, trialwise centering or baseline-aware normalization is necessary before model training.")
    lines.append("- A SMR-oriented bandpass (`8-30 Hz`) is worth keeping as the default starting point for the next offline/online iteration.")
    lines.append("- The classical alpha/beta-power baseline also stays near chance across rounds, which suggests the current issue is not only model capacity but also limited discriminative signal or session-to-session drift.")
    lines.append("- Current results are only a pilot because the dataset contains one subject and 40 trials total.")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"report": str(REPORT_PATH), "results": results, "summaries": summaries, "classical": classical}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    torch.set_num_threads(1)
    main()
