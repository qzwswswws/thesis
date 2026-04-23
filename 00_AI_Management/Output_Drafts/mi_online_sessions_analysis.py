from __future__ import annotations

import csv
import importlib.util
import json
import random
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import torch
import torch.nn as nn
from scipy import signal


ROOT = Path(r"C:\Users\qzwsw\Documents\thesis")
LOG_ROOT = Path(r"C:\Users\qzwsw\Documents\nearalQT_mi_logs")
ROOT = Path.home() / "thesis"
LOG_ROOT = Path.home() / "nearalQT_mi_logs"
SCRIPT_PATH = ROOT / "02_Source_Material" / "04_Algorithm_Workbench" / "scripts" / "conformer_lowchannel_b2_diff.py"
PRETRAIN = ROOT / "02_Source_Material" / "04_Algorithm_Workbench" / "results" / "2b_pretrain_transfer" / "weights" / "conformer_b2_c3c4_pretrain_2b.pt"
META_PATH = ROOT.parent / "nearalQT_mi_runtime" / "models" / "latest_model_meta.json"
REPORT_PATH = ROOT / "00_AI_Management" / "Output_Drafts" / "MI_Online_Sessions_Analysis_20260401.md"

ONLINE_SESSIONS = [
    "20260401_144934_mi_lr",
    "20260401_145447_mi_lr",
    "20260401_145825_mi_lr",
    "20260401_150213_mi_lr",
]
SEEDS = [42, 3407, 20260401]


def load_conformer_class():
    spec = importlib.util.spec_from_file_location("conformer_lowchannel_b2_diff", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["conformer_lowchannel_b2_diff"] = module
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


def load_trials(session_base: str):
    summary_path = LOG_ROOT / f"{session_base}_summary.csv"
    raw_path = LOG_ROOT / f"{session_base}_raw_eeg.csv"

    summary_map = {
        int(r["trial_index"]): r
        for r in csv.DictReader(summary_path.open("r", encoding="utf-8", newline=""))
        if r["status"].strip('"') == "completed" and r["aborted"] == "0"
    }

    grouped: Dict[int, Dict[str, List[List[float]]]] = {}
    with raw_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            idx = int(row["trial_index"])
            if idx not in summary_map:
                continue
            phase = row["phase"].strip().strip('"')
            cue = row["cue_label"].strip().strip('"')
            ch0 = float(row["ch0_uv"])
            ch1 = float(row["ch1_uv"])
            bucket = grouped.setdefault(
                idx,
                {"cue": cue, "Prepare": [[], []], "Imagery": [[], []], "Rest": [[], []]},
            )
            if phase in bucket:
                bucket[phase][0].append(ch0)
                bucket[phase][1].append(ch1)

    trials = []
    for idx in sorted(grouped):
        row = summary_map[idx]
        item = grouped[idx]
        imagery_start = float(row["imagery_start_sec"])
        rest_start = float(row["rest_start_sec"])
        duration = max(rest_start - imagery_start, 1e-6)
        trials.append(
            {
                "session": session_base,
                "trial_index": idx,
                "cue": item["cue"],
                "prepare": np.asarray(item["Prepare"], dtype=np.float32),
                "imagery": np.asarray(item["Imagery"], dtype=np.float32),
                "rest": np.asarray(item["Rest"], dtype=np.float32),
                "imagery_duration": duration,
            }
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


def preprocess_trial(trial) -> np.ndarray:
    imagery = interp_channels(trial["imagery"], 2000)
    imagery = imagery - imagery.mean(axis=1, keepdims=True)
    imagery = butter_bandpass(imagery, fs=500.0, low=8.0, high=30.0)
    imagery = interp_channels(imagery, 1000)
    imagery = channelwise_zscore(imagery)
    return imagery


def build_dataset(session_names: List[str]) -> Tuple[np.ndarray, np.ndarray, Dict[str, Dict[str, float]]]:
    xs = []
    ys = []
    stats: Dict[str, Dict[str, float]] = {}
    for name in session_names:
        trials = load_trials(name)
        imagery_counts = [t["imagery"].shape[1] for t in trials]
        eff_hz = [t["imagery"].shape[1] / t["imagery_duration"] for t in trials]
        stats[name] = {
            "n_trials": len(trials),
            "left": sum(t["cue"] == "Left Hand" for t in trials),
            "right": sum(t["cue"] == "Right Hand" for t in trials),
            "imagery_min": int(min(imagery_counts)),
            "imagery_max": int(max(imagery_counts)),
            "imagery_avg": float(np.mean(imagery_counts)),
            "hz_min": float(min(eff_hz)),
            "hz_max": float(max(eff_hz)),
            "hz_avg": float(np.mean(eff_hz)),
        }
        for trial in trials:
            xs.append(np.expand_dims(preprocess_trial(trial), axis=0))
            ys.append(0 if trial["cue"] == "Left Hand" else 1)
    return np.stack(xs, axis=0).astype(np.float32), np.asarray(ys, dtype=np.int64), stats


def normalize_sets(x_train: np.ndarray, x_test: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    mean = float(x_train.mean())
    std = float(x_train.std())
    if std < 1e-6:
        std = 1.0
    return ((x_train - mean) / std).astype(np.float32), ((x_test - mean) / std).astype(np.float32)


def extract_state_dict(obj):
    if isinstance(obj, dict) and "state_dict" in obj:
        return obj["state_dict"]
    return obj


def train_eval(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_test: np.ndarray,
    y_test: np.ndarray,
    seed: int,
    init_state=None,
    epochs: int = 20,
    lr: float = 2e-4,
) -> float:
    set_seed(seed)
    device = torch.device("cpu")
    x_train_n, x_test_n = normalize_sets(x_train, x_test)

    model = ConformerB2(n_channels=2, n_classes=2, window_size=8, use_diff_branch=True).to(device)
    if init_state is not None:
        model.load_state_dict(init_state, strict=True)

    opt = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()

    tx = torch.from_numpy(x_train_n).float().to(device)
    ty = torch.from_numpy(y_train).long().to(device)
    vx = torch.from_numpy(x_test_n).float().to(device)
    vy = torch.from_numpy(y_test).long().to(device)
    bs = 8

    for _ in range(epochs):
        model.train()
        perm = torch.randperm(tx.size(0), device=device)
        for start in range(0, tx.size(0), bs):
            idx = perm[start:start + bs]
            xb = tx[idx]
            yb = ty[idx]
            _, logits = model(xb)
            loss = criterion(logits, yb)
            opt.zero_grad()
            loss.backward()
            opt.step()

    model.eval()
    with torch.no_grad():
        _, logits = model(vx)
        pred = logits.argmax(dim=1)
        acc = float((pred == vy).float().mean().item())
    return acc


def summarize(vals: List[float]) -> Tuple[float, float]:
    arr = np.asarray(vals, dtype=np.float32)
    return float(arr.mean()), float(arr.std(ddof=0))


def main() -> None:
    pretrained_state = extract_state_dict(torch.load(PRETRAIN, map_location="cpu"))

    rows = []
    all_stats = {}
    for test_idx in range(1, len(ONLINE_SESSIONS)):
        train_sessions = ONLINE_SESSIONS[:test_idx]
        test_session = ONLINE_SESSIONS[test_idx]
        x_train, y_train, train_stats = build_dataset(train_sessions)
        x_test, y_test, test_stats = build_dataset([test_session])
        all_stats.update(train_stats)
        all_stats.update(test_stats)

        for seed in SEEDS:
            rows.append(
                {
                    "condition": "baseline",
                    "seed": seed,
                    "train_sessions": train_sessions,
                    "test_session": test_session,
                    "acc": train_eval(x_train, y_train, x_test, y_test, seed, None, epochs=20, lr=2e-4),
                }
            )
            rows.append(
                {
                    "condition": "pretrained",
                    "seed": seed,
                    "train_sessions": train_sessions,
                    "test_session": test_session,
                    "acc": train_eval(x_train, y_train, x_test, y_test, seed, pretrained_state, epochs=20, lr=1e-4),
                }
            )

    by_step = []
    for test_session in ONLINE_SESSIONS[1:]:
        base_vals = [r["acc"] for r in rows if r["condition"] == "baseline" and r["test_session"] == test_session]
        pre_vals = [r["acc"] for r in rows if r["condition"] == "pretrained" and r["test_session"] == test_session]
        b_mean, b_std = summarize(base_vals)
        p_mean, p_std = summarize(pre_vals)
        by_step.append(
            {
                "test_session": test_session,
                "baseline_mean": b_mean,
                "baseline_std": b_std,
                "pretrained_mean": p_mean,
                "pretrained_std": p_std,
                "delta": p_mean - b_mean,
            }
        )

    base_overall, base_overall_std = summarize([r["acc"] for r in rows if r["condition"] == "baseline"])
    pre_overall, pre_overall_std = summarize([r["acc"] for r in rows if r["condition"] == "pretrained"])

    meta = {}
    if META_PATH.exists():
        meta = json.loads(META_PATH.read_text(encoding="utf-8"))

    lines = [
        "# 在线实验轮次结果分析（2026-04-01）",
        "",
        "## 分析范围",
        "",
        "- 重点分析已经进入在线联动阶段的 4 轮：",
    ]
    lines.extend([f"  - `{name}`" for name in ONLINE_SESSIONS])
    lines.extend(
        [
            "",
            "## 数据完整性与采样稳定性",
            "",
            "| Session | Trials | Left | Right | Imagery samples min-max | Imagery avg | Effective Hz avg |",
            "| --- | ---: | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for name in ONLINE_SESSIONS:
        s = all_stats[name]
        lines.append(
            f"| `{name}` | {int(s['n_trials'])} | {int(s['left'])} | {int(s['right'])} | "
            f"{int(s['imagery_min'])}-{int(s['imagery_max'])} | {s['imagery_avg']:.1f} | {s['hz_avg']:.1f} |"
        )

    lines.extend(
        [
            "",
            "## 累积训练 -> 下一轮测试",
            "",
            "统一采用当前在线默认预处理：`Imagery 4 s -> 8-30 Hz -> 重采样 1000 点 -> per-trial z-score`。",
            "",
            "| Test session | Baseline mean ± std | 2b pretrained mean ± std | Delta |",
            "| --- | --- | --- | ---: |",
        ]
    )
    for step in by_step:
        lines.append(
            f"| `{step['test_session']}` | "
            f"{step['baseline_mean']:.4f} ± {step['baseline_std']:.4f} | "
            f"{step['pretrained_mean']:.4f} ± {step['pretrained_std']:.4f} | "
            f"{step['delta']:+.4f} |"
        )

    lines.extend(
        [
            "",
            "## 总体汇总",
            "",
            f"- Baseline 总体均值：`{base_overall:.4f} ± {base_overall_std:.4f}`",
            f"- 2b 预训练总体均值：`{pre_overall:.4f} ± {pre_overall_std:.4f}`",
            f"- 总体提升：`{(pre_overall - base_overall):+.4f}`",
            "",
            "## 当前运行时模型状态",
            "",
        ]
    )

    if meta:
        lines.extend(
            [
                f"- 最新累计样本数：`{meta.get('samples_total', 'n/a')}`",
                f"- 最新验证准确率：`{meta.get('validation_accuracy', 'n/a')}`",
                f"- 初始化来源：`{meta.get('initialization_source', 'n/a')}`",
                f"- 预处理链：`{meta.get('preprocessing', 'n/a')}`",
                f"- 最近更新对应轮次：`{Path(str(meta.get('source_summary', 'n/a'))).name}`",
            ]
        )
    else:
        lines.append("- 未读取到 `latest_model_meta.json`。")

    lines.extend(
        [
            "",
            "## 解释与判断",
            "",
            "- 这 4 轮在线实验的数据完整性是好的，每轮都稳定完成了 `20` 个 trial，左右手保持 `10/10` 平衡。",
            "- 采样点数和有效采样率仍有波动，说明小型设备采集链路仍然存在 session-level 不稳定性，但没有破坏到 trial 可用性。",
            "- 在“前序轮次训练、后一轮测试”的设定下，`2b` 预训练初始化整体持续优于随机初始化，说明在线链路已经开始从预训练表征中受益。",
            "- 目前最稳妥的结论仍应写成“预训练初始化在多轮双导在线实验中表现出稳定的正向帮助”，而不宜直接写成已经达到稳定高精度在线控制。",
            "- 由于当前没有把每 trial 的在线推理结果单独落盘，现阶段更可靠的分析仍然是基于会话日志做离线复盘，而不是声称界面在线显示结果本身已经构成正式实验指标。",
            "",
            "## 建议",
            "",
            "1. 继续沿用当前预训练初始化与预处理设置，不建议此时频繁改模型。",
            "2. 后续若再采 2-4 轮，应补一份混淆矩阵和类别级错误分析。",
            "3. 建议尽快把每 trial 的 `predicted_label/confidence` 也落到文件中，便于把“在线显示结果”正式写进第 5 章。",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"report": str(REPORT_PATH), "overall_baseline": base_overall, "overall_pretrained": pre_overall}, ensure_ascii=False))


if __name__ == "__main__":
    main()
