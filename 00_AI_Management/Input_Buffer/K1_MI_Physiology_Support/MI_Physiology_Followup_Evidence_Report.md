# Knowledge Cluster 1B: MI Physiology Follow-up Evidence Report
*(Extracted from Undermind.ai Research Project)*

## Executive Summary
This targeted review provides quantitative evidence for unresolved physiological mechanisms in Chapter 2.1. Key findings confirm the plasticity of hemispheric asymmetry under feedback, the task-dependency of Beta rebound, and the critical role of subject variability as a system feature.

## 1. Resolution of Core Physiological Questions

### Q1: Does feedback or training change hemispheric asymmetry or ERD strength?
- **Finding**: Yes. Coherent feedback (Proprioceptive, Tactile, or Visiotactile fusion) significantly enhances ERD lateralization and stability.
- **Evidence**: 
  - **Ono18b**: Proprioceptive feedback outperforms visual in stabilizing mu-ERD.
  - **Vas21**: Short-term training significantly improves lateralization metrics.
  - **Neu99**: Impact of visual feedback on cortical activation patterns.

### Q2: How reliable is Beta rebound in hand MI tasks?
- **Finding**: Beta rebound is stable in hand MI but highly task-dependent (strongest in termination paradigms). It is less reliable than foot MI rebound and should be used as a secondary/supportive feature.
- **Evidence**:
  - **Pfu05**: Classic definition of post-MI ERS (rebound).
  - **Has13**: Analyzing task dependency in discrete vs. continuous MI.
  - **Tar20**: Quantitative study (n=20) showed only 45% of subjects had significant hand-MI rebound compared to higher foot-MI rates.

### Q3: Evidence for Large-Sample User Variability?
- **Finding**: 15-30% of users are "BCI illiterate" or have low SMR control. This relates to resting-state quality, handedness, and the stability of the ERD pattern.
- **Evidence**:
  - **San19**: Psychological factors (depression, motivation) inversely correlate with BCI performance (n=80).
  - **Acq16**: Large-scale distribution of MI features in the population.
  - **Bla10/Kap24**: Predicting BCI performance based on initial SMR quality.

## 2. Recommended Citation Strategy for Chapter 2
- **Update 2.1**: Integrate Ono18b to support the "Feedback Loop" section.
- **Update Assessment of Variability**: Use San19 and Acq16 to justify the need for "Adaptive Algorithms" in Chapter 4 (connecting back to the hardware-aware adaptation results in [Bia24]).
- **Beta Rebound Warning**: Cite Tar20 to emphasize why the proposed `EdgeMIFormer` focuses primarily on Mu-ERD rather than over-relying on transient-beta.
