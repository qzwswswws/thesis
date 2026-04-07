from __future__ import annotations

import csv
import importlib.util
import json
import random
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import scipy.io
import torch
import torch.nn as nn
from scipy import signal
from sklearn.model_selection import train_test_split


ROOT = Path(r"C:\Users\qzwsw\Documents\thesis")
SCRIPT_DIR = ROOT / "02_Source_Material" / "04_Algorithm_Workbench" / "scripts"
DATA_ROOT_2B = ROOT / "02_Source_Material" / "04_Algorithm_Workbench" / "datasets" / "standard_2b_strict_TE"
LOCAL_LOG_ROOT = Path(r"C:\Users\qzwsw\Documents\nearalQT_mi_logs")
RESULT_ROOT = ROOT / "02_Source_Material" / "04_Algorithm_Workbench" / "results" / "2b_pretrain_transfer"
REPORT_PATH = ROOT / "00_AI_Management" / "Output_Drafts" / "MI_2B_Pretrain_Transfer_Report_20260401.md"

LOCAL_SESSIONS = [
    "20260401_122743_mi_lr",
    "20260401_123310_mi_lr",
]
EVAL_SEEDS = [42, 3407, 20260401]


@dataclass
class Trial:
    session: str
    trial_index: int
    cue: str
    prepare: np.ndarray
    imagery: np.ndarray
    rest: np.ndarray


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_conformer_class():
    target = SCRIPT_DIR / "conformer_lowchannel_b2_diff.py"
    spec = importlib.util.spec_from_file_location("conformer_lowchannel_b2_diff", target)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.ConformerB2


ConformerB2 = load_conformer_class()


def load_2b_split() -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, List[str], List[str]]:
    train_x, train_y, test_x, test_y = [], [], [], []
    train_files, test_files = [], []

    for mat_path in sorted(DATA_ROOT_2B.glob("B0*.mat")):
        mat = scipy.io.loadmat(mat_path)
        data = np.asarray(mat["data"], dtype=np.float32)  # [1000, 3, n]
        label = np.asarray(mat["label"]).reshape(-1).astype(np.int64) - 1
        # keep C3 / C4 only to match local dual-channel setting
        x = np.transpose(data[:, [0, 2], :], (2, 1, 0))[:, None, :, :]  # [n, 1, 2, 1000]

        if mat_path.stem.endswith("T"):
            train_x.append(x)
            train_y.append(label)
            train_files.append(mat_path.name)
        else:
            test_x.append(x)
            test_y.append(label)
            test_files.append(mat_path.name)

    if not train_x or not test_x:
        raise RuntimeError(f"Missing 2b MAT files under {DATA_ROOT_2B}")

    return (
        np.concatenate(train_x, axis=0).astype(np.float32),
        np.concatenate(train_y, axis=0).astype(np.int64),
        np.concatenate(test_x, axis=0).astype(np.float32),
        np.concatenate(test_y, axis=0).astype(np.int64),
        train_files,
        test_files,
    )


def load_local_trials(session_base: str) -> List[Trial]:
    summary_path = LOCAL_LOG_ROOT / f"{session_base}_summary.csv"
    raw_path = LOCAL_LOG_ROOT / f"{session_base}_raw_eeg.csv"

    summary_rows = {
        int(row["trial_index"]): row
        for row in csv.DictReader(summary_path.open("r", encoding="utf-8", newline=""))
        if row["status"].strip('"') == "completed" and row["aborted"] == "0"
    }

    grouped: Dict[int, Dict[str, List[List[float]]]] = {}
    with raw_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            trial_index = int(row["trial_index"])
            if trial_index not in summary_rows:
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
        item = grouped[trial_index]
        trials.append(
            Trial(
                session=session_base,
                trial_index=trial_index,
                cue=item["cue"],
                prepare=np.asarray(item["Prepare"], dtype=np.float32),
                imagery=np.asarray(item["Imagery"], dtype=np.float32),
                rest=np.asarray(item["Rest"], dtype=np.float32),
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


def preprocess_local_trial(trial: Trial) -> np.ndarray:
    imagery = interp_channels(trial.imagery, 2000)
    imagery = imagery - imagery.mean(axis=1, keepdims=True)
    imagery = butter_bandpass(imagery, fs=500.0, low=8.0, high=30.0)
    imagery = interp_channels(imagery, 1000)
    imagery = channelwise_zscore(imagery)
    return imagery


def build_local_dataset(trials: List[Trial]) -> Tuple[np.ndarray, np.ndarray]:
    xs = []
    ys = []
    for trial in trials:
        xs.append(np.expand_dims(preprocess_local_trial(trial), axis=0))
        ys.append(0 if trial.cue == "Left Hand" else 1)
    return np.stack(xs, axis=0).astype(np.float32), np.asarray(ys, dtype=np.int64)


def normalize_sets(x_train: np.ndarray, x_other: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float, float]:
    mean = float(x_train.mean())
    std = float(x_train.std())
    if std < 1e-6:
        std = 1.0
    return (
        ((x_train - mean) / std).astype(np.float32),
        ((x_other - mean) / std).astype(np.float32),
        mean,
        std,
    )


def run_epoch(model, x, y, batch_size, optimizer=None, device=torch.device("cpu")) -> Tuple[float, float]:
    train_mode = optimizer is not None
    model.train(mode=train_mode)
    perm = torch.randperm(x.size(0), device=device) if train_mode else torch.arange(x.size(0), device=device)
    total_loss = 0.0
    total_correct = 0

    for start in range(0, x.size(0), batch_size):
        idx = perm[start:start + batch_size]
        xb = x[idx]
        yb = y[idx]
        _, logits = model(xb)
        loss = nn.CrossEntropyLoss()(logits, yb)

        if optimizer is not None:
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        total_loss += float(loss.item()) * yb.size(0)
        total_correct += int((logits.argmax(dim=1) == yb).sum().item())

    n = int(x.size(0))
    return total_loss / max(n, 1), total_correct / max(n, 1)


def train_model(
    x_train: np.ndarray,
    y_train: np.ndarray,
    x_eval: np.ndarray,
    y_eval: np.ndarray,
    seed: int,
    epochs: int,
    lr: float,
    batch_size: int,
    init_state: Dict[str, torch.Tensor] | None = None,
    save_path: Path | None = None,
) -> Dict[str, object]:
    set_seed(seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    x_tr, x_va, y_tr, y_va = train_test_split(
        x_train, y_train, test_size=0.1 if len(y_train) >= 100 else 0.25, random_state=seed, stratify=y_train
    )
    x_tr, x_va, mean, std = normalize_sets(x_tr, x_va)
    x_eval_n = ((x_eval - mean) / std).astype(np.float32)

    model = ConformerB2(n_channels=2, n_classes=2, window_size=8, use_diff_branch=True).to(device)
    if init_state is not None:
        model.load_state_dict(init_state, strict=True)

    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    tr_x = torch.from_numpy(x_tr).float().to(device)
    tr_y = torch.from_numpy(y_tr).long().to(device)
    va_x = torch.from_numpy(x_va).float().to(device)
    va_y = torch.from_numpy(y_va).long().to(device)
    te_x = torch.from_numpy(x_eval_n).float().to(device)
    te_y = torch.from_numpy(y_eval).long().to(device)

    best_state = None
    best_val_acc = -1.0
    best_epoch = -1
    history = []

    for epoch in range(1, epochs + 1):
        train_loss, train_acc = run_epoch(model, tr_x, tr_y, batch_size=batch_size, optimizer=optimizer, device=device)
        val_loss, val_acc = run_epoch(model, va_x, va_y, batch_size=batch_size, optimizer=None, device=device)
        history.append(
            {
                "epoch": epoch,
                "train_loss": train_loss,
                "train_acc": train_acc,
                "val_loss": val_loss,
                "val_acc": val_acc,
            }
        )
        if val_acc >= best_val_acc:
            best_val_acc = val_acc
            best_epoch = epoch
            best_state = {k: v.detach().cpu() for k, v in model.state_dict().items()}

    assert best_state is not None
    model.load_state_dict(best_state, strict=True)
    test_loss, test_acc = run_epoch(model, te_x, te_y, batch_size=batch_size, optimizer=None, device=device)

    if save_path is not None:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(
            {
                "state_dict": best_state,
                "mean": mean,
                "std": std,
                "seed": seed,
                "best_epoch": best_epoch,
                "best_val_acc": best_val_acc,
                "test_acc": test_acc,
                "history": history,
            },
            save_path,
        )

    return {
        "best_state": best_state,
        "best_epoch": best_epoch,
        "best_val_acc": best_val_acc,
        "test_acc": test_acc,
        "test_loss": test_loss,
        "history": history,
    }


def run_local_transfer(
    pretrained_state: Dict[str, torch.Tensor],
    session_a: str,
    session_b: str,
) -> Dict[str, object]:
    trials_a = load_local_trials(session_a)
    trials_b = load_local_trials(session_b)
    x_a, y_a = build_local_dataset(trials_a)
    x_b, y_b = build_local_dataset(trials_b)

    directions = [
        ("A_to_B", x_a, y_a, x_b, y_b, session_a, session_b),
        ("B_to_A", x_b, y_b, x_a, y_a, session_b, session_a),
    ]

    results = {"baseline": [], "pretrained": []}

    for seed in EVAL_SEEDS:
        for tag, x_train, y_train, x_test, y_test, train_name, test_name in directions:
            baseline_path = RESULT_ROOT / "local_finetune" / f"baseline_{tag}_seed{seed}.pt"
            pretrain_path = RESULT_ROOT / "local_finetune" / f"pretrained_{tag}_seed{seed}.pt"

            baseline = train_model(
                x_train,
                y_train,
                x_test,
                y_test,
                seed=seed,
                epochs=20,
                lr=2e-4,
                batch_size=8,
                init_state=None,
                save_path=baseline_path,
            )
            transferred = train_model(
                x_train,
                y_train,
                x_test,
                y_test,
                seed=seed,
                epochs=20,
                lr=1e-4,
                batch_size=8,
                init_state=pretrained_state,
                save_path=pretrain_path,
            )

            results["baseline"].append(
                {
                    "seed": seed,
                    "direction": tag,
                    "train_session": train_name,
                    "test_session": test_name,
                    "acc": baseline["test_acc"],
                }
            )
            results["pretrained"].append(
                {
                    "seed": seed,
                    "direction": tag,
                    "train_session": train_name,
                    "test_session": test_name,
                    "acc": transferred["test_acc"],
                }
            )

    return results


def summarize_acc(rows: List[Dict[str, object]]) -> Dict[str, float]:
    arr = np.asarray([float(r["acc"]) for r in rows], dtype=np.float32)
    return {
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=0)),
        "min": float(arr.min()),
        "max": float(arr.max()),
    }


def write_report(pretrain_metrics: Dict[str, object], local_results: Dict[str, object], train_files: List[str], test_files: List[str]) -> None:
    base_stats = summarize_acc(local_results["baseline"])
    pre_stats = summarize_acc(local_results["pretrained"])
    delta = pre_stats["mean"] - base_stats["mean"]

    lines = [
        "# 2b 预训练迁移实验记录（2026-04-01）",
        "",
        "## 实验目的",
        "",
        "- 使用 `BCI Competition IV 2b` 的双导化数据（仅保留 `C3/C4`）预训练 `ConformerB2`。",
        "- 将预训练权重迁移到当前本地 `nearalQT` 双导左右手离线数据，比较“随机初始化”与“2b 预训练初始化”的跨轮泛化表现。",
        "",
        "## 2b 预训练设置",
        "",
        f"- 2b 数据根目录：`{DATA_ROOT_2B}`",
        f"- 训练文件数：{len(train_files)} (`T` sessions)",
        f"- 测试文件数：{len(test_files)} (`E` sessions)",
        "- 通道：`C3/C4`（从 `C3/Cz/C4` 中选取两导）",
        "- 输入长度：`1000` 点",
        "- 模型：`ConformerB2(n_channels=2, n_classes=2, use_diff_branch=True)`",
        "",
        "## 2b 预训练结果",
        "",
        f"- 最优验证轮次：{pretrain_metrics['best_epoch']}",
        f"- 验证集最佳准确率：{pretrain_metrics['best_val_acc']:.4f}",
        f"- 2b E-session 测试准确率：{pretrain_metrics['test_acc']:.4f}",
        "",
        "## 本地双导离线迁移结果",
        "",
        f"- 基线（随机初始化）均值：{base_stats['mean']:.4f} ± {base_stats['std']:.4f}",
        f"- 预训练初始化均值：{pre_stats['mean']:.4f} ± {pre_stats['std']:.4f}",
        f"- 均值提升：{delta:+.4f}",
        "",
        "### 逐次结果",
        "",
        "| Condition | Seed | Direction | Accuracy |",
        "| --- | --- | --- | --- |",
    ]

    for condition in ("baseline", "pretrained"):
        for row in local_results[condition]:
            lines.append(f"| {condition} | {row['seed']} | {row['direction']} | {float(row['acc']):.4f} |")

    lines.extend(
        [
            "",
            "## 预训练权重与结果文件",
            "",
            f"- 2b 预训练权重：`{RESULT_ROOT / 'weights' / 'conformer_b2_c3c4_pretrain_2b.pt'}`",
            f"- 本地微调权重目录：`{RESULT_ROOT / 'local_finetune'}`",
            "",
            "## 初步判断",
            "",
        ]
    )

    if delta > 0.02:
        lines.append("- 在当前两轮双导离线数据上，2b 预训练初始化表现出明确正向帮助，后续值得作为在线轮次训练的默认初始化方式。")
    elif delta > -0.02:
        lines.append("- 在当前两轮双导离线数据上，2b 预训练初始化与随机初始化差异较小，说明预训练特征有一定可迁移性，但收益尚未稳定显现。")
    else:
        lines.append("- 在当前两轮双导离线数据上，2b 预训练初始化未带来稳定收益，说明当前本地数据域偏移与采集不稳定性仍是主要瓶颈。")

    lines.append("- 无论结果方向如何，预训练权重已经保留，可继续用于后续更多轮本地数据的增量微调和对比。")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    start = time.time()
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    (RESULT_ROOT / "weights").mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("2b pretrain + local transfer")
    print(f"2b root:   {DATA_ROOT_2B}")
    print(f"local log: {LOCAL_LOG_ROOT}")
    print(f"results:   {RESULT_ROOT}")
    print("=" * 72)

    x_train_2b, y_train_2b, x_test_2b, y_test_2b, train_files, test_files = load_2b_split()
    print(f"2b train: {x_train_2b.shape} 2b test: {x_test_2b.shape}")

    pretrain_ckpt = RESULT_ROOT / "weights" / "conformer_b2_c3c4_pretrain_2b.pt"
    pretrain_metrics = train_model(
        x_train_2b,
        y_train_2b,
        x_test_2b,
        y_test_2b,
        seed=42,
        epochs=12,
        lr=2e-4,
        batch_size=128,
        init_state=None,
        save_path=pretrain_ckpt,
    )
    print(
        "2b pretrain done:",
        f"best_epoch={pretrain_metrics['best_epoch']}",
        f"val={pretrain_metrics['best_val_acc']:.4f}",
        f"test={pretrain_metrics['test_acc']:.4f}",
    )

    local_results = run_local_transfer(
        pretrain_metrics["best_state"],
        LOCAL_SESSIONS[0],
        LOCAL_SESSIONS[1],
    )
    base_stats = summarize_acc(local_results["baseline"])
    pre_stats = summarize_acc(local_results["pretrained"])
    print(
        "local baseline:",
        f"{base_stats['mean']:.4f} ± {base_stats['std']:.4f}",
        "| pretrained:",
        f"{pre_stats['mean']:.4f} ± {pre_stats['std']:.4f}",
    )

    write_report(pretrain_metrics, local_results, train_files, test_files)

    manifest = {
        "2b_train_files": train_files,
        "2b_test_files": test_files,
        "pretrain_checkpoint": str(pretrain_ckpt),
        "report_path": str(REPORT_PATH),
        "elapsed_sec": round(time.time() - start, 2),
    }
    (RESULT_ROOT / "run_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"report: {REPORT_PATH}")
    print(f"elapsed: {manifest['elapsed_sec']} sec")


if __name__ == "__main__":
    main()
