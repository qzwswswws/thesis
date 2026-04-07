# MI Offline Preprocessing Sweep

## Data Stability Snapshot

### 20260401_122743_mi_lr

- Trials: `20` (`Left=10`, `Right=10`)
- Phase-labeled imagery samples: min `1600`, max `2680`, avg `2091.0`
- Effective imagery sampling rate: min `375.9 Hz`, max `625.3 Hz`, avg `491.3 Hz`
- Channel offset drift: `CH0 2949.1+/-66.5 uV`, `CH1 1612.4+/-24.9 uV`

### 20260401_123310_mi_lr

- Trials: `20` (`Left=10`, `Right=10`)
- Phase-labeled imagery samples: min `1960`, max `2820`, avg `2124.0`
- Effective imagery sampling rate: min `465.9 Hz`, max `662.3 Hz`, avg `502.2 Hz`
- Channel offset drift: `CH0 2866.4+/-79.3 uV`, `CH1 1175.2+/-38.2 uV`

## ConformerB2 Cross-Round Results

| Variant | Train -> Test | Accuracy |
|---|---|---:|
| `phase_imagery_bandpass_index_z` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `phase_imagery_bandpass_index_z` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `50.0%` |
| `phase_imagery_bandpass_index_z` | `mean` | `50.0%` |
| `time4_bandpass_time_z` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `time4_bandpass_time_z` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `50.0%` |
| `time4_bandpass_time_z` | `mean` | `50.0%` |
| `time4_prepare_bandpass_time_z` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `time4_prepare_bandpass_time_z` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `50.0%` |
| `time4_prepare_bandpass_time_z` | `mean` | `50.0%` |
| `time4_prepare_detrend_bandpass_time_z` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `time4_prepare_detrend_bandpass_time_z` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `50.0%` |
| `time4_prepare_detrend_bandpass_time_z` | `mean` | `50.0%` |
| `time4_prepare_detrend_clip_bandpass_time_z` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `time4_prepare_detrend_clip_bandpass_time_z` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `50.0%` |
| `time4_prepare_detrend_clip_bandpass_time_z` | `mean` | `50.0%` |
| `time3mid_prepare_detrend_clip_bandpass_time_z` | `20260401_122743_mi_lr` -> `20260401_123310_mi_lr` | `50.0%` |
| `time3mid_prepare_detrend_clip_bandpass_time_z` | `20260401_123310_mi_lr` -> `20260401_122743_mi_lr` | `55.0%` |
| `time3mid_prepare_detrend_clip_bandpass_time_z` | `mean` | `52.5%` |

## Classical Spectral Baseline

| Variant | Cross-round mean | Pooled 5-fold mean |
|---|---:|---:|
| `phase_imagery_bandpass_index_z` | `60.0%` | `62.5%` |
| `time4_bandpass_time_z` | `52.5%` | `65.0%` |
| `time4_prepare_bandpass_time_z` | `52.5%` | `65.0%` |
| `time4_prepare_detrend_bandpass_time_z` | `52.5%` | `65.0%` |
| `time4_prepare_detrend_clip_bandpass_time_z` | `52.5%` | `65.0%` |
| `time3mid_prepare_detrend_clip_bandpass_time_z` | `45.0%` | `55.0%` |

## Recommended Reading of the Sweep

- Best deep cross-round variant: `time3mid_prepare_detrend_clip_bandpass_time_z` (`52.5%`).
- Best classical cross-round variant: `phase_imagery_bandpass_index_z` (`60.0%`).
- On the current two-round dataset, the simplest `phase-labeled imagery + 8-30 Hz + per-trial z-score` pipeline is still the strongest classical cross-round baseline.
- Time-aware reconstruction remains worth keeping as an engineering direction, but it does not yet outperform the simpler phase-labeled extraction on this small dataset.
- Prepare-period normalization is reasonable when the device baseline drifts across rounds, but it does not fully solve cross-round generalization by itself.
- Linear detrending and mild robust clipping are still useful safety steps for small wearable acquisition, because they help suppress slow drift and occasional spikes without assuming perfect stationarity.
- A fixed 4 s imagery window resampled to 1000 points remains the most compatible choice with the current low-channel model. Central-window variants are still research-worthy, but they are less directly aligned with the thesis model input.
- If cross-round accuracy remains near chance after these corrections, the next bottleneck is more likely signal quality / paradigm execution consistency / session calibration than model architecture.

## Current Recommendation for the Online Pipeline

1. For the next online/offline round, keep the classifier input simple: use the phase-labeled 4 s imagery segment.
2. Resample each trial segment to 1000 points to match the current low-channel model input.
3. Apply a moderate 8-30 Hz bandpass and per-trial channelwise z-score as the default classifier preprocessing.
4. Keep prepare-period normalization, detrending, and clipping as optional anti-drift diagnostics rather than mandatory first-line preprocessing.
5. Log enough rounds to allow at least one calibration round plus one held-out validation round before online claims are made.
