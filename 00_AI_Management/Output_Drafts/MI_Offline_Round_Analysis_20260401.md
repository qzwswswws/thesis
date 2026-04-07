# MI Offline Round Analysis

## Data Summary

### 20260401_122743_mi_lr

- Trials: `20` (`Left=10`, `Right=10`)
- Imagery sample count: min `1600`, max `2680`, avg `2091.0`
- Effective sampling rate by trial: min `375.9 Hz`, max `625.3 Hz`, avg `491.3 Hz`
- Channel offset drift: `CH0 2949.1+/-66.5 uV`, `CH1 1612.4+/-24.9 uV`

### 20260401_123310_mi_lr

- Trials: `20` (`Left=10`, `Right=10`)
- Imagery sample count: min `1960`, max `2820`, avg `2124.0`
- Effective sampling rate by trial: min `465.9 Hz`, max `662.3 Hz`, avg `502.2 Hz`
- Channel offset drift: `CH0 2866.4+/-79.3 uV`, `CH1 1175.2+/-38.2 uV`

## Offline ConformerB2 Pilot

| Variant | Train -> Test | Accuracy |
|---|---|---:|
| `raw_trial_z` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `40.0%` |
| `raw_trial_z` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `45.0%` |
| `raw_trial_z` | `mean` | `42.5%` |
| `bandpass_trial_z` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `bandpass_trial_z` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `50.0%` |
| `bandpass_trial_z` | `mean` | `50.0%` |
| `prepare_norm_bandpass` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `prepare_norm_bandpass` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `50.0%` |
| `prepare_norm_bandpass` | `mean` | `50.0%` |

## Classical Spectral Baseline

| Variant | Train -> Test | Accuracy |
|---|---|---:|
| `alpha/beta power + channel difference` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `alpha/beta power + channel difference` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `55.0%` |
| `alpha/beta power + channel difference` | `mean` | `52.5%` |

## Suggested Interpretation

- Best pilot variant in this run: `bandpass_trial_z` with mean cross-round accuracy `50.0%`.
- Raw imagery lengths vary noticeably across trials, so direct fixed-index slicing is less stable than resampling each imagery segment to a fixed target length.
- Because channel offsets drift between rounds, trialwise centering or baseline-aware normalization is necessary before model training.
- A SMR-oriented bandpass (`8-30 Hz`) is worth keeping as the default starting point for the next offline/online iteration.
- The classical alpha/beta-power baseline also stays near chance across rounds, which suggests the current issue is not only model capacity but also limited discriminative signal or session-to-session drift.
- Current results are only a pilot because the dataset contains one subject and 40 trials total.
