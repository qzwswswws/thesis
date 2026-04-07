from __future__ import annotations

import csv
import json
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
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


SESSIONS = [
    "20260401_122743_mi_lr",
    "20260401_123310_mi_lr",
]
BASE_DIR = Path(r"C:\Users\qzwsw\Documents\nearalQT_mi_logs")
SCRIPT_DIR = Path(r"C:\Users\qzwsw\Documents\thesis\02_Source_Material\04_Algorithm_Workbench\scripts")
REPORT_PATH = Path(r"C:\Users\qzwsw\Documents\thesis\00_AI_Management\Output_Drafts\MI_Offline_Preprocessing_Sweep_20260401.md")


@dataclass
class Trial:
    session: str
    trial_index: int
    cue: str
    prepare_start_sec: float
    imagery_start_sec: float
    rest_start_sec: float
    end_sec: float
    phase_prepare: np.ndarray
    phase_imagery: np.ndarray
    phase_rest: np.ndarray
    all_times: np.ndarray
    all_data: np.ndarray


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

    summary_rows = {
        int(row["trial_index"]): row
        for row in csv.DictReader(summary_path.open("r", encoding="utf-8", newline=""))
        if row["status"].strip('"') == "completed" and row["aborted"] == "0"
    }

    grouped: Dict[int, Dict[str, object]] = {}
    with raw_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            trial_index = int(row["trial_index"])
            if trial_index not in summary_rows:
                continue
            phase = row["phase"].strip('"')
            cue = row["cue_label"].strip('"')
            elapsed = float(row["experiment_elapsed_sec"])
            ch0 = float(row["ch0_uv"])
            ch1 = float(row["ch1_uv"])

            bucket = grouped.setdefault(
                trial_index,
                {
                    "cue": cue,
                    "Prepare": [[], []],
                    "Imagery": [[], []],
                    "Rest": [[], []],
                    "times": [],
                    "all_ch0": [],
                    "all_ch1": [],
                },
            )
            if phase in ("Prepare", "Imagery", "Rest"):
                bucket[phase][0].append(ch0)
                bucket[phase][1].append(ch1)
            bucket["times"].append(elapsed)
            bucket["all_ch0"].append(ch0)
            bucket["all_ch1"].append(ch1)

    trials: List[Trial] = []
    for trial_index in sorted(grouped):
        row = summary_rows[trial_index]
        item = grouped[trial_index]
        trials.append(
            Trial(
                session=session_base,
                trial_index=trial_index,
                cue=item["cue"],
                prepare_start_sec=float(row["prepare_start_sec"]),
                imagery_start_sec=float(row["imagery_start_sec"]),
                rest_start_sec=float(row["rest_start_sec"]),
                end_sec=float(row["end_sec"]),
                phase_prepare=np.asarray(item["Prepare"], dtype=np.float32),
                phase_imagery=np.asarray(item["Imagery"], dtype=np.float32),
                phase_rest=np.asarray(item["Rest"], dtype=np.float32),
                all_times=np.asarray(item["times"], dtype=np.float32),
                all_data=np.asarray([item["all_ch0"], item["all_ch1"]], dtype=np.float32),
            )
        )
    return trials


def collapse_duplicate_times(times: np.ndarray, data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    rounded = np.round(times.astype(np.float64), 6)
    unique_times, inverse = np.unique(rounded, return_inverse=True)
    agg = np.zeros((data.shape[0], unique_times.shape[0]), dtype=np.float32)
    counts = np.zeros(unique_times.shape[0], dtype=np.float32)
    for idx, inv in enumerate(inverse):
        agg[:, inv] += data[:, idx]
        counts[inv] += 1.0
    counts[counts == 0.0] = 1.0
    agg /= counts[None, :]
    return unique_times.astype(np.float32), agg.astype(np.float32)


def resample_by_index(data: np.ndarray, target_points: int) -> np.ndarray:
    if data.shape[1] == target_points:
        return data.astype(np.float32, copy=False)
    x_old = np.linspace(0.0, 1.0, data.shape[1], dtype=np.float32)
    x_new = np.linspace(0.0, 1.0, target_points, dtype=np.float32)
    out = np.empty((data.shape[0], target_points), dtype=np.float32)
    for ch in range(data.shape[0]):
        out[ch] = np.interp(x_new, x_old, data[ch]).astype(np.float32)
    return out


def resample_by_time(times: np.ndarray, data: np.ndarray, duration: float, target_points: int) -> np.ndarray:
    rel_times = np.clip(times - float(times[0]), 0.0, duration)
    rel_times, data = collapse_duplicate_times(rel_times, data)
    if rel_times.shape[0] < 4:
        return resample_by_index(data, target_points)
    grid = np.linspace(0.0, duration, target_points, endpoint=False, dtype=np.float32)
    out = np.empty((data.shape[0], target_points), dtype=np.float32)
    for ch in range(data.shape[0]):
        out[ch] = np.interp(grid, rel_times, data[ch], left=data[ch, 0], right=data[ch, -1]).astype(np.float32)
    return out


def butter_bandpass(data: np.ndarray, fs: float, low: float = 8.0, high: float = 30.0) -> np.ndarray:
    sos = signal.butter(4, [low, high], btype="bandpass", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, data, axis=1).astype(np.float32)


def clip_by_mad(data: np.ndarray, scale: float = 5.0) -> np.ndarray:
    median = np.median(data, axis=1, keepdims=True)
    mad = np.median(np.abs(data - median), axis=1, keepdims=True)
    mad[mad < 1e-6] = 1.0
    lower = median - scale * mad
    upper = median + scale * mad
    return np.clip(data, lower, upper).astype(np.float32)


def channelwise_zscore(data: np.ndarray) -> np.ndarray:
    mean = data.mean(axis=1, keepdims=True)
    std = data.std(axis=1, keepdims=True)
    std[std < 1e-6] = 1.0
    return ((data - mean) / std).astype(np.float32)


def select_time_window(trial: Trial, start_offset: float, end_offset: float) -> Tuple[np.ndarray, np.ndarray]:
    start = trial.imagery_start_sec + start_offset
    end = trial.imagery_start_sec + end_offset
    mask = (trial.all_times >= start) & (trial.all_times < end)
    selected_times = trial.all_times[mask]
    selected_data = trial.all_data[:, mask]
    if selected_times.size < 4:
        selected_times = trial.all_times
        selected_data = trial.all_data
    return selected_times.astype(np.float32), selected_data.astype(np.float32)


def get_prepare_segment(trial: Trial) -> np.ndarray:
    if trial.phase_prepare.shape[1] >= 10:
        return trial.phase_prepare.astype(np.float32)
    mask = (trial.all_times >= trial.prepare_start_sec) & (trial.all_times < trial.imagery_start_sec)
    return trial.all_data[:, mask].astype(np.float32)


VARIANTS = [
    {
        "name": "phase_imagery_bandpass_index_z",
        "extract": "phase",
        "bandpass": True,
        "detrend": False,
        "prepare_norm": False,
        "clip": False,
    },
    {
        "name": "time4_bandpass_time_z",
        "extract": "time",
        "start_offset": 0.0,
        "end_offset": 4.0,
        "bandpass": True,
        "detrend": False,
        "prepare_norm": False,
        "clip": False,
    },
    {
        "name": "time4_prepare_bandpass_time_z",
        "extract": "time",
        "start_offset": 0.0,
        "end_offset": 4.0,
        "bandpass": True,
        "detrend": False,
        "prepare_norm": True,
        "clip": False,
    },
    {
        "name": "time4_prepare_detrend_bandpass_time_z",
        "extract": "time",
        "start_offset": 0.0,
        "end_offset": 4.0,
        "bandpass": True,
        "detrend": True,
        "prepare_norm": True,
        "clip": False,
    },
    {
        "name": "time4_prepare_detrend_clip_bandpass_time_z",
        "extract": "time",
        "start_offset": 0.0,
        "end_offset": 4.0,
        "bandpass": True,
        "detrend": True,
        "prepare_norm": True,
        "clip": True,
    },
    {
        "name": "time3mid_prepare_detrend_clip_bandpass_time_z",
        "extract": "time",
        "start_offset": 0.5,
        "end_offset": 3.5,
        "bandpass": True,
        "detrend": True,
        "prepare_norm": True,
        "clip": True,
    },
]


def preprocess_trial(trial: Trial, variant: Dict[str, object], target_points: int = 1000) -> np.ndarray:
    if variant["extract"] == "phase":
        x = trial.phase_imagery.astype(np.float32)
        x = resample_by_index(x, target_points)
        fs = 250.0
    else:
        start_offset = float(variant["start_offset"])
        end_offset = float(variant["end_offset"])
        duration = end_offset - start_offset
        times, values = select_time_window(trial, start_offset, end_offset)
        x = resample_by_time(times, values, duration=duration, target_points=target_points)
        fs = float(target_points) / duration

    if bool(variant["prepare_norm"]):
        prepare = get_prepare_segment(trial)
        if prepare.shape[1] >= 10:
            base_mean = prepare.mean(axis=1, keepdims=True)
            base_std = prepare.std(axis=1, keepdims=True)
            base_std[base_std < 1e-6] = 1.0
            x = (x - base_mean) / base_std
        else:
            x = x - x.mean(axis=1, keepdims=True)
    else:
        x = x - x.mean(axis=1, keepdims=True)

    if bool(variant["detrend"]):
        x = signal.detrend(x, axis=1, type="linear").astype(np.float32)

    if bool(variant["clip"]):
        x = clip_by_mad(x, scale=5.0)

    if bool(variant["bandpass"]):
        x = butter_bandpass(x, fs=fs, low=8.0, high=30.0)

    return channelwise_zscore(x)


def build_dataset(trials: List[Trial], variant: Dict[str, object]) -> Tuple[np.ndarray, np.ndarray]:
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


def train_conformer_cross_session(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    seed: int,
) -> float:
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


def spectral_features(preprocessed: np.ndarray, fs: float) -> np.ndarray:
    psd = np.abs(np.fft.rfft(preprocessed, axis=1)) ** 2
    freqs = np.fft.rfftfreq(preprocessed.shape[1], d=1 / fs)

    def band(lo: float, hi: float) -> np.ndarray:
        mask = (freqs >= lo) & (freqs <= hi)
        return psd[:, mask].mean(axis=1)

    alpha = band(8.0, 13.0)
    beta = band(13.0, 30.0)
    return np.asarray(
        [alpha[0], alpha[1], beta[0], beta[1], alpha[0] - alpha[1], beta[0] - beta[1]],
        dtype=np.float32,
    )


def evaluate_classical(trials_by_session: Dict[str, List[Trial]], variant: Dict[str, object]) -> Dict[str, object]:
    rows = []
    duration = float(variant.get("end_offset", 4.0)) - float(variant.get("start_offset", 0.0)) if variant["extract"] == "time" else 4.0
    fs = 250.0 if variant["extract"] == "phase" else 1000.0 / duration

    for session in SESSIONS:
        for trial in trials_by_session[session]:
            pre = preprocess_trial(trial, variant)
            feat = spectral_features(pre, fs=fs)
            label = 0 if trial.cue == "Left Hand" else 1
            rows.append((session, feat, label))

    X = np.vstack([row[1] for row in rows])
    y = np.asarray([row[2] for row in rows], dtype=np.int64)
    sess = [row[0] for row in rows]
    pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))

    cross = []
    for train_session, test_session in [(SESSIONS[0], SESSIONS[1]), (SESSIONS[1], SESSIONS[0])]:
        train_mask = np.asarray([s == train_session for s in sess])
        test_mask = np.asarray([s == test_session for s in sess])
        pipe.fit(X[train_mask], y[train_mask])
        pred = pipe.predict(X[test_mask])
        cross.append((train_session, test_session, float(accuracy_score(y[test_mask], pred))))

    pooled_scores = []
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    for train_idx, test_idx in cv.split(X, y):
        pipe.fit(X[train_idx], y[train_idx])
        pred = pipe.predict(X[test_idx])
        pooled_scores.append(float(accuracy_score(y[test_idx], pred)))

    return {
        "cross": cross,
        "cross_mean": float(np.mean([score for _, _, score in cross])),
        "pooled_mean": float(np.mean(pooled_scores)),
        "pooled_scores": pooled_scores,
    }


def summarize_data(trials: List[Trial]) -> Dict[str, float]:
    imagery_counts = [trial.phase_imagery.shape[1] for trial in trials]
    effective_hz = [
        trial.phase_imagery.shape[1] / max(1e-6, trial.rest_start_sec - trial.imagery_start_sec)
        for trial in trials
    ]
    all_raw = np.concatenate([trial.all_data for trial in trials], axis=1)
    return {
        "n_trials": len(trials),
        "left": sum(1 for t in trials if t.cue == "Left Hand"),
        "right": sum(1 for t in trials if t.cue == "Right Hand"),
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


def main() -> None:
    torch.set_num_threads(1)
    trials_by_session = {session: load_trials(session) for session in SESSIONS}
    summaries = {session: summarize_data(trials) for session, trials in trials_by_session.items()}

    deep_results = []
    classical_results = []
    for variant in VARIANTS:
        x_a, y_a = build_dataset(trials_by_session[SESSIONS[0]], variant)
        x_b, y_b = build_dataset(trials_by_session[SESSIONS[1]], variant)
        folds = [
            (SESSIONS[0], SESSIONS[1], train_conformer_cross_session(x_a, y_a, x_b, y_b, seed=42)),
            (SESSIONS[1], SESSIONS[0], train_conformer_cross_session(x_b, y_b, x_a, y_a, seed=42)),
        ]
        deep_results.append(
            {
                "name": variant["name"],
                "folds": folds,
                "mean_acc": float(np.mean([acc for _, _, acc in folds])),
            }
        )
        classical = evaluate_classical(trials_by_session, variant)
        classical["name"] = variant["name"]
        classical_results.append(classical)

    lines: List[str] = []
    lines.append("# MI Offline Preprocessing Sweep")
    lines.append("")
    lines.append("## Data Stability Snapshot")
    lines.append("")
    for session in SESSIONS:
        info = summaries[session]
        lines.append(f"### {session}")
        lines.append("")
        lines.append(f"- Trials: `{info['n_trials']}` (`Left={info['left']}`, `Right={info['right']}`)")
        lines.append(f"- Phase-labeled imagery samples: min `{info['imagery_min']}`, max `{info['imagery_max']}`, avg `{info['imagery_avg']:.1f}`")
        lines.append(f"- Effective imagery sampling rate: min `{info['hz_min']:.1f} Hz`, max `{info['hz_max']:.1f} Hz`, avg `{info['hz_avg']:.1f} Hz`")
        lines.append(f"- Channel offset drift: `CH0 {info['ch0_mean']:.1f}+/-{info['ch0_std']:.1f} uV`, `CH1 {info['ch1_mean']:.1f}+/-{info['ch1_std']:.1f} uV`")
        lines.append("")

    lines.append("## ConformerB2 Cross-Round Results")
    lines.append("")
    lines.append("| Variant | Train -> Test | Accuracy |")
    lines.append("|---|---|---:|")
    for result in deep_results:
        for train_session, test_session, acc in result["folds"]:
            lines.append(f"| `{result['name']}` | `{train_session}` -> `{test_session}` | `{acc*100:.1f}%` |")
        lines.append(f"| `{result['name']}` | `mean` | `{result['mean_acc']*100:.1f}%` |")

    lines.append("")
    lines.append("## Classical Spectral Baseline")
    lines.append("")
    lines.append("| Variant | Cross-round mean | Pooled 5-fold mean |")
    lines.append("|---|---:|---:|")
    for result in classical_results:
        lines.append(f"| `{result['name']}` | `{result['cross_mean']*100:.1f}%` | `{result['pooled_mean']*100:.1f}%` |")

    lines.append("")
    lines.append("## Recommended Reading of the Sweep")
    lines.append("")
    best_deep = max(deep_results, key=lambda item: item["mean_acc"])
    best_classical = max(classical_results, key=lambda item: item["cross_mean"])
    lines.append(f"- Best deep cross-round variant: `{best_deep['name']}` (`{best_deep['mean_acc']*100:.1f}%`).")
    lines.append(f"- Best classical cross-round variant: `{best_classical['name']}` (`{best_classical['cross_mean']*100:.1f}%`).")
    lines.append("- On the current two-round dataset, the simplest `phase-labeled imagery + 8-30 Hz + per-trial z-score` pipeline is still the strongest classical cross-round baseline.")
    lines.append("- Time-aware reconstruction remains worth keeping as an engineering direction, but it does not yet outperform the simpler phase-labeled extraction on this small dataset.")
    lines.append("- Prepare-period normalization is reasonable when the device baseline drifts across rounds, but it does not fully solve cross-round generalization by itself.")
    lines.append("- Linear detrending and mild robust clipping are still useful safety steps for small wearable acquisition, because they help suppress slow drift and occasional spikes without assuming perfect stationarity.")
    lines.append("- A fixed 4 s imagery window resampled to 1000 points remains the most compatible choice with the current low-channel model. Central-window variants are still research-worthy, but they are less directly aligned with the thesis model input.")
    lines.append("- If cross-round accuracy remains near chance after these corrections, the next bottleneck is more likely signal quality / paradigm execution consistency / session calibration than model architecture.")
    lines.append("")
    lines.append("## Current Recommendation for the Online Pipeline")
    lines.append("")
    lines.append("1. For the next online/offline round, keep the classifier input simple: use the phase-labeled 4 s imagery segment.")
    lines.append("2. Resample each trial segment to 1000 points to match the current low-channel model input.")
    lines.append("3. Apply a moderate 8-30 Hz bandpass and per-trial channelwise z-score as the default classifier preprocessing.")
    lines.append("4. Keep prepare-period normalization, detrending, and clipping as optional anti-drift diagnostics rather than mandatory first-line preprocessing.")
    lines.append("5. Log enough rounds to allow at least one calibration round plus one held-out validation round before online claims are made.")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(
        json.dumps(
            {
                "report": str(REPORT_PATH),
                "deep_results": deep_results,
                "classical_results": classical_results,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
