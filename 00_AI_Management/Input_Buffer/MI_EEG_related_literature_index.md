# MI_EEG_related_literature_index

##### [**Undermind**](https://undermind.ai)

---


## Table of Contents

- [MI EEG related literature index](#mi-eeg-related-literature-index)
- [Priority reading list](#priority-reading-list)
- [1. Core physiology](#core-physiology)
- [2. Timing / baseline / ERD-ERS dynamics](#timing-baseline-erd-ers-dynamics)
- [3. Design-support / engineering bridge](#design-support-engineering-bridge)
- [4. Provisional / abstract-only](#provisional-abstract-only)
- [5. Excluded from mainline narrative](#excluded-from-mainline-narrative)
- [Final note on use status](#final-note-on-use-status)
  - [Essential](#essential)
  - [Optional](#optional)
  - [Provisional](#provisional)
  - [Keep excluded from the Section 2.1 mainline](#keep-excluded-from-the-section-2.1-mainline)
- [References](#references)

## MI EEG related literature index

Companion index for later thesis drafting.

Scope:

- Includes core papers, screened support papers, downgraded papers, provisional papers, and excluded papers from the completed search.
- Not a narrative review.
- Not a rewrite of the Section 2.1 evidence report.

Legend:

- **Access**: full text available, HTML only, abstract only
- **Trace**: yes, partial, no
- **Safe to cite without full text?**: yes, conditional, no

## Priority reading list

| Rank | Paper ID | Bibliographic record | Why priority | Safe to cite without full text? |
|:---|:---|:---|:---|:---|
| 1 | \[Pfu06\] | Pfurtscheller et al. *Mu rhythm (de)synchronization and EEG single-trial classification of different motor imagery tasks*. NeuroImage, 2006. | Best core paper for C3 C4 Cz, mu-beta separation, and canonical MI physiology. | yes |
| 2 | \[Mcf04\] | McFarland et al. *Mu and Beta Rhythm Topographies During Motor Imagery and Actual Movements*. Brain Topography, 2000. | Best topography paper for mu-beta distinction. | yes |
| 3 | \[Zap20b\] | Zapała et al. *The effects of handedness on sensorimotor rhythm desynchronization and motor-imagery BCI control*. Scientific Reports, 2020. | Best modern variability paper for handedness and lateralization. | conditional |
| 4 | \[Xu19\] | Xu et al. *The Sensitivity of Single-Trial Mu-Suppression Detection for Motor Imagery Performance as Compared to Motor Execution and Motor Observation Performance*. Frontiers in Human Neuroscience, 2019. | Best timing paper for individualized latency. | yes |
| 5 | \[Rim23b\] | Rimbert et al. *Impact of the baseline temporal selection on the ERD/ERS analysis for Motor Imagery-based BCI*. EMBC, 2023. | Best baseline-timing caution paper. | yes |
| 6 | \[Men18\] | Meng et al. *A Study of the Effects of Electrode Number and Decoding Algorithm on Online EEG-Based BCI Behavioral Performance*. Frontiers in Neuroscience, 2018. | Strong decoder-design bridge for small vs large montage. | conditional |
| 7 | \[Arp20\] | Arpaia et al. *Channel Selection for Optimal EEG Measurement in Motor Imagery-Based Brain-Computer Interfaces*. International Journal of Neural Systems, 2021. | Strong reduced-channel feasibility paper. | conditional |
| 8 | \[San19\] | Sannelli et al. *A large scale screening study with a SMR-based BCI: Categorization of BCI users and differences in their SMR activity*. PLoS ONE, 2019. | Strong large-cohort variability context. | conditional |
| 9 | \[Tid20\] | Tidare et al. *Time-resolved estimation of strength of motor imagery representation by multivariate EEG decoding*. Journal of Neural Engineering, 2020. | Useful timing-dynamics paper, though same-hand task. | conditional |
| 10 | \[Bla22\] | Blanco-Díaz et al. *Comparative Analysis of Spectral and Temporal Combinations in CSP-based Methods for Decoding Hand Motor Imagery Tasks*. Journal of Neuroscience Methods, 2022. | Clean design-support paper for band banks and 1.5 s window. | no |

## 1. Core physiology

| Paper ID | Exact bibliographic record | Category | Cohort | Task | Access | Trace | Thesis section support | Usefulness note | Caution note | Safe to cite without full text? |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| \[Pfu06\] | Pfurtscheller et al. *Mu rhythm (de)synchronization and EEG single-trial classification of different motor imagery tasks*. NeuroImage, 2006. | core physiology | healthy | mixed task | full text available | yes | Section 2.1 core physiology | Canonical source for C3 C4 Cz importance and mu-beta ERD patterns. | Mixed-task design means hand-specific claims should be stated carefully. | yes |
| \[Mcf04\] | McFarland et al. *Mu and Beta Rhythm Topographies During Motor Imagery and Actual Movements*. Brain Topography, 2000. | core physiology | healthy | left-right hand MI and movement | full text available | yes | Section 2.1 core physiology | Strongest traced source for distinct mu and beta topographies. | Beta maximum wording still needs one final locus check. | yes |
| \[Zap20b\] | Zapała et al. *The effects of handedness on sensorimotor rhythm desynchronization and motor-imagery BCI control*. Scientific Reports, 2020. | core physiology | healthy | left-right hand MI | HTML only | partial | Section 2.1 variability paragraph | Best modern paper on handedness and alpha-lateralization differences. | Cluster-based sensorimotor evidence, not a clean C3 C4 electrode paper. | conditional |
| \[Che21\] | Chen et al. *Mu oscillations and motor imagery performance: A reflection of intra-individual success, not inter-individual ability*. Human Movement Science, 2021. | core physiology | healthy | other MI | abstract only | no | optional background on mu meaning | Useful for the claim that mu tracks within-subject imagery success. | Task is not a standard left-right hand MI BCI paradigm. | no |
| \[Men19\] | Meng and He. *Exploring Training Effect in 42 Human Subjects Using a Non-invasive Sensorimotor Rhythm Based Online BCI*. Frontiers in Human Neuroscience, 2019. | core physiology | healthy | left-right hand MI | abstract only | no | optional Section 2.1 variability or training note | Useful for short-term training and ERD lateralization changes. | Better as training context than as core mechanism evidence. | no |
| \[Gro24\] | Gamboa von Groll et al. *Large scale investigation of the effect of gender on mu rhythm suppression in motor imagery brain-computer interfaces*. Brain Computer Interfaces, 2024. | core physiology | healthy | left-right hand MI | abstract only | no | optional background on user factors | Large pooled healthy dataset with C3 C4 mu suppression index. | Negative result and pooled-dataset design make it background, not a core anchor. | no |
| \[Vas21\] | Vasilyev et al. *Does Real-Time Feedback Affect Sensorimotor EEG Patterns in Routine Motor Imagery Practice?* Brain Sciences, 2021. | core physiology | healthy | mixed hand and arm MI | abstract only | no | optional feedback-context note | Useful for stability of ERD spatial sources across sessions. | Not a clean left-right hand MI physiology paper. | no |
| \[Fil20\] | Filho et al. *On the (in)efficacy of motor imagery training without feedback and event-related desynchronizations considerations*. Biomedical Physics & Engineering Express, 2020. | core physiology | healthy | hands MI | abstract only | no | optional note on mu vs beta and training | Useful for the claim that mu and beta ERD differ and no-feedback training may not enhance ERD. | Better as support for variability and training than as a main anchor. | no |
| \[San19\] | Sannelli et al. *A large scale screening study with a SMR-based BCI: Categorization of BCI users and differences in their SMR activity*. PLoS ONE, 2019. | core physiology | healthy | mixed task | abstract only | no | optional user-variability context | Large screening study for SMR variability and BCI inefficiency. | Broad SMR aptitude study, not specific to C3 C4 Cz physiology. | no |

## 2. Timing / baseline / ERD-ERS dynamics

| Paper ID | Exact bibliographic record | Category | Cohort | Task | Access | Trace | Thesis section support | Usefulness note | Caution note | Safe to cite without full text? |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| \[Xu19\] | Xu et al. *The Sensitivity of Single-Trial Mu-Suppression Detection for Motor Imagery Performance as Compared to Motor Execution and Motor Observation Performance*. Frontiers in Human Neuroscience, 2019. | timing / baseline / ERD-ERS dynamics | healthy | other MI | full text available | yes | Section 2.1 timing paragraph | Best traced evidence for individualized mu latency and short local windows. | Detection paper, not direct left-vs-right class-decoding evidence. | yes |
| \[Rim23b\] | Rimbert et al. *Impact of the baseline temporal selection on the ERD/ERS analysis for Motor Imagery-based BCI*. EMBC, 2023. | timing / baseline / ERD-ERS dynamics | healthy | left-right hand MI | full text available | yes | Section 2.1 baseline paragraph | Best traced source for baseline-driven changes in ERD and MI-vs-rest performance. | Conference short paper; keep claims tight to baseline effects. | yes |
| \[Tid20\] | Tidare et al. *Time-resolved estimation of strength of motor imagery representation by multivariate EEG decoding*. Journal of Neural Engineering, 2020. | timing / baseline / ERD-ERS dynamics | healthy | other MI | abstract only | no | optional timing-dynamics support | Useful for early dynamic and later stationary MI representations. | Same-hand opening-closing task limits direct transfer to left-right thesis claims. | no |
| \[Ors20\] | Orset et al. *User Adaptation to Closed-Loop Decoding of Motor Imagery Termination*. IEEE Transactions on Biomedical Engineering, 2021. | timing / baseline / ERD-ERS dynamics | healthy | other MI | abstract only | no | optional offset-decoding note | Useful for MI termination latency and offset decoding. | Both-hands termination task is outside the Section 2.1 mainline. | no |
| \[Sis24\] | Sisti et al. *Postmovement Beta Rebound in Real and Imagined Movement*. Motor Control, 2024. | timing / baseline / ERD-ERS dynamics | healthy | mixed task | abstract only | no | optional post-MI beta context | Recent PMBR paper showing imagined-movement rebound. | Visuomotor tracking context is not standard left-right hand MI. | no |
| \[Pap24\] | Papadopoulos et al. *Surfing beta burst waveforms to improve motor imagery-based BCI*. Imaging Neuroscience, 2024. | timing / baseline / ERD-ERS dynamics | healthy | left-right hand MI | abstract only | no | optional advanced beta-dynamics note | Useful for burst-based reinterpretation of beta dynamics. | Primarily a decoding paper, not a core physiology paper. | no |
| \[Pap23\] | Papadopoulos et al. *Beta bursts question the ruling power for brain–computer interfaces*. Journal of Neural Engineering, 2023. | timing / baseline / ERD-ERS dynamics | healthy | left-right hand MI | abstract only | no | optional advanced beta-dynamics note | Useful for updating the interpretation of beta power in MI. | Better for discussion or future-work context than for the mainline. | no |
| \[Wan22b\] | Wang et al. *Intelligent Classification Technique of Hand Motor Imagery Using EEG Beta Rebound Follow-Up Pattern*. Biosensors, 2022. | timing / baseline / ERD-ERS dynamics | healthy | left-right hand MI / mixed task | abstract only | no | optional beta-rebound support | Useful for follow-up beta-rebound classification ideas. | Rehabilitation-style engineering framing dominates over physiology. | no |
| \[Abb18c\] | Abbaspour et al. *An Effective Brain-Computer Interface System Based on the Optimal Timeframe Selection of Brain Signals*. International Clinical Neuroscience Journal, 2018. | timing / baseline / ERD-ERS dynamics | mixed or unclear | left-right hand MI | abstract only | no | optional time-window support | Useful for the claim that shorter, better targeted windows may improve decoding. | Evidence is dataset-driven and not primarily physiological. | no |
| \[Sou23\] | de Souza et al. *Window-Delay Analysis on EEGNet*. ISCMI, 2023. | timing / baseline / ERD-ERS dynamics | mixed or unclear | left-right hand MI | abstract only | no | optional design-timing bridge | Useful for delay-performance tradeoff framing. | Pure model-evaluation paper, not physiology evidence. | no |
| \[Liu22b\] | Liu et al. *Motor imagery classification method based on long and short windows interception*. Measurement Science and Technology, 2022. | timing / baseline / ERD-ERS dynamics | mixed | mixed task | abstract only | no | optional design-timing bridge | Useful for variable-window interception logic. | Pure classification paper. | no |

## 3. Design-support / engineering bridge

| Paper ID | Exact bibliographic record | Category | Cohort | Task | Access | Trace | Thesis section support | Usefulness note | Caution note | Safe to cite without full text? |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| \[Men18\] | Meng et al. *A Study of the Effects of Electrode Number and Decoding Algorithm on Online EEG-Based BCI Behavioral Performance*. Frontiers in Neuroscience, 2018. | design-support / engineering bridge | healthy | hand MI | abstract only | no | decoder-design bridge | Strong support for compact central montages and online training effects. | Do not present as primary physiology evidence. | conditional |
| \[Arp20\] | Arpaia et al. *Channel Selection for Optimal EEG Measurement in Motor Imagery-Based Brain-Computer Interfaces*. International Journal of Neural Systems, 2021. | design-support / engineering bridge | healthy benchmark | left-right hand MI / mixed task | abstract only | no | decoder-design bridge | Strong reduced-channel feasibility paper. | Benchmark paper, not mechanism evidence. | conditional |
| \[Mal21b\] | Malan and Sharma. *Time window and frequency band optimization using regularized neighbourhood component analysis for Multi-View Motor Imagery EEG classification*. Biomedical Signal Processing and Control, 2021. | design-support / engineering bridge | healthy benchmark | mixed task | abstract only | no | decoder-design bridge | Strong joint time-band optimization paper. | Dataset-optimization paper only. | no |
| \[Rob18\] | Robinson et al. *Neurophysiological predictors and spectro-spatial discriminative features for enhancing SMR-BCI*. Journal of Neural Engineering, 2018. | design-support / engineering bridge | healthy | bilateral MI | abstract only | no | bridge to subject-specific design | Useful for subject-specific spectro-spatial modeling and resting-state predictors. | More predictor and algorithm framing than physiology. | no |
| \[Tsu21\] | Tsuchimoto et al. *Use of common average reference and large-Laplacian spatial-filters enhances EEG signal-to-noise ratios in intrinsic sensorimotor activity*. Journal of Neuroscience Methods, 2021. | design-support / engineering bridge | healthy | not specific to left-right MI | abstract only | no | methods or signal-processing support | Useful for reference and spatial-filtering decisions near sensorimotor cortex. | Not a hand-MI physiology paper. | no |
| \[Sun18\] | Sun et al. *A contralateral channel guided model for EEG based motor imagery classification*. Biomedical Signal Processing and Control, 2018. | design-support / engineering bridge | mixed | left-right hand MI | abstract only | no | design bridge | Useful for contralateral-channel model ideas. | Classification-oriented and not traced. | no |
| \[Cat19\] | Cattai et al. *Phase/Amplitude Synchronization of Brain Signals During Motor Imagery BCI Tasks*. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2019. | design-support / engineering bridge | healthy | hand MI | abstract only | no | optional advanced feature support | Useful for connectivity-feature framing around MI. | Not needed for a focused Section 2.1 physiology narrative. | no |
| \[Yan14\] | Yang et al. *Time-frequency optimization for discrimination between imagination of right and left hand movements based on two bipolar electroencephalography channels*. EURASIP Journal on Advances in Signal Processing, 2014. | design-support / engineering bridge | healthy benchmark | left-right hand MI | abstract only | no | channel-reduction bridge | Useful for two-channel C3 C4 optimization logic. | Optimization paper rather than physiology paper. | no |
| \[Dai20\] | Dai et al. *Effect of Spatial Filtering and Channel Selection on Motor Imagery BCI*. Proceedings of the 2020 Conference on Artificial Intelligence and Healthcare, 2020. | design-support / engineering bridge | mixed | mixed task | abstract only | no | small-montage support | Useful for arguing that 8 channels may be enough. | Weak and conference-level support only. | no |
| \[Mal21\] | Malan and Sharma. *Motor Imagery EEG Spectral-Spatial Feature Optimization Using Dual-Tree Complex Wavelet and Neighbourhood Component Analysis*. IRBM, 2021. | design-support / engineering bridge | healthy benchmark | mixed task | abstract only | no | bridge to band-selection methods | Useful for spectral-spatial sub-band optimization context. | Pure algorithm paper. | no |
| \[Zha22\] | Zhang et al. *Enhancing Visual-Guided Motor Imagery Performance via Sensory Threshold Somatosensory Electrical Stimulation Training*. IEEE Transactions on Biomedical Engineering, 2022. | design-support / engineering bridge | healthy | left-right hand MI | abstract only | no | training-design bridge | Useful for training interventions that strengthen alpha ERD and classification. | Better for methods or intervention context than Section 2.1 mechanism. | no |
| \[Wan19\] | Wang et al. *A BCI based visual-haptic neurofeedback training improves cortical activations and classification performance during motor imagery*. Journal of Neural Engineering, 2019. | design-support / engineering bridge | healthy | motor imagery | abstract only | no | neurofeedback bridge | Useful for multi-band ERD enhancement after neurofeedback. | Training paper, not primary physiology. | no |
| \[Ang12\] | Ang et al. *Filter Bank Common Spatial Pattern Algorithm on BCI Competition IV Datasets 2a and 2b*. Frontiers in Neuroscience, 2012. | design-support / engineering bridge | healthy benchmark | mixed task | abstract only | no | canonical engineering citation | Canonical FBCSP citation for sub-band filtering. | Benchmark algorithm paper only. | no |
| \[San10\] | Sannelli et al. *On Optimal Channel Configurations for SMR-based Brain–Computer Interfaces*. Brain Topography, 2010. | design-support / engineering bridge | healthy | mixed task | abstract only | no | channel-selection bridge | Useful early channel-configuration support. | Not traced and not specific to Section 2.1 mechanism. | no |
| \[Lu13\] | Lu et al. *Adaptive Laplacian filtering for sensorimotor rhythm-based brain–computer interfaces*. Journal of Neural Engineering, 2013. | design-support / engineering bridge | healthy | SMR BCI | abstract only | no | spatial-filtering methods | Useful support for Laplacian spatial filtering. | Methods paper, not physiology. | no |
| \[Nae09\] | Naeem et al. *Dimensionality Reduction and Channel Selection of Motor Imagery Electroencephalographic Data*. Computational Intelligence and Neuroscience, 2009. | design-support / engineering bridge | healthy benchmark | mixed task | abstract only | no | channel-reduction bridge | Useful for reduced-channel and reduced-component feasibility. | Old and primarily engineering-focused. | no |

## 4. Provisional / abstract-only

| Paper ID | Exact bibliographic record | Category | Cohort | Task | Access | Trace | Thesis section support | Usefulness note | Caution note | Safe to cite without full text? |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| \[Neu99\] | Neuper et al. *Enhancement of left-right sensorimotor EEG differences during feedback-regulated motor imagery*. Journal of Clinical Neurophysiology, 1999. | provisional / abstract-only | healthy | left-right hand MI | abstract only | no | optional Section 2.1 feedback note | Potentially important canonical feedback paper. | Do not rely on it for strong claims until full-text trace is completed. | no |
| \[Pfu97\] | Pfurtscheller et al. *EEG-based discrimination between imagination of right and left hand movement*. Electroencephalography and Clinical Neurophysiology, 1997. | provisional / abstract-only | healthy | left-right hand MI | abstract only | no | optional canonical citation | Important early left-right MI paper. | Small sample and no completed page trace. | no |
| \[Pfu05\] | Pfurtscheller et al. *Beta rebound after different types of motor imagery in man*. Neuroscience Letters, 2005. | provisional / abstract-only | healthy | mixed task | abstract only | no | optional post-MI rebound note | Canonical rebound paper. | Stronger rebound effect is for feet than hands; full text still needed. | no |
| \[Bla22\] | Blanco-Díaz et al. *Comparative Analysis of Spectral and Temporal Combinations in CSP-based Methods for Decoding Hand Motor Imagery Tasks*. Journal of Neuroscience Methods, 2022. | provisional / abstract-only | healthy benchmark | left-right hand MI | abstract only | no | design bridge only | Clean benchmark support for sub-bands and 1.5 s window. | Keep out of the main physiology narrative until traced and explicitly marked as engineering support. | no |

## 5. Excluded from mainline narrative

| Paper ID | Exact bibliographic record | Category | Cohort | Task | Access | Trace | Thesis section support | Usefulness note | Caution note | Safe to cite without full text? |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| \[Has13\] | Hashimoto and Ushiba. *EEG-based classification of imaginary left and right foot movements using beta rebound*. Clinical Neurophysiology, 2013. | excluded from mainline narrative | healthy | other MI | abstract only | no | none or foot-MI aside only | Useful only if a foot-MI rebound comparison is needed. | Not directly transferable to left-right hand MI physiology. | no |
| \[Kwo18\] | Kwon et al. *Event-Related Desynchronization (ERD) May Not be Correlated with Motor Imagery BCI Performance*. IEEE SMC, 2018. | excluded from mainline narrative | mixed | mixed task | abstract only | no | optional discussion caveat | Useful as a caution that ERD magnitude and classification are not the same. | Too indirect for the main Section 2.1 line. | no |
| \[Li19\] | Li et al. *Brain-Computer Interface Channel-Selection Strategy Based on Analysis of Event-Related Desynchronization Topography in Stroke Patients*. Journal of Healthcare Engineering, 2019. | excluded from mainline narrative | patient | motor attempt | abstract only | no | stroke transferability note only | Useful for explicit patient-transferability warnings. | Patient ERD topography should not be pooled with healthy thesis claims. | no |
| \[Man22\] | Mansour et al. *Exploring the ability of stroke survivors in using the contralesional hemisphere to control a brain–computer interface*. Scientific Reports, 2022. | excluded from mainline narrative | patient | affected-hand MI | abstract only | no | stroke transferability note only | Useful for contralesional-control discussion in patients. | Outside healthy Section 2.1 scope. | no |
| \[Rem19\] | Remsik et al. *Ipsilesional Mu Rhythm Desynchronization and Changes in Motor Behavior Following Post Stroke BCI Intervention for Motor Rehabilitation*. Frontiers in Neuroscience, 2019. | excluded from mainline narrative | patient | attempted movement | abstract only | no | stroke transferability note only | Useful for rehab-related mu changes. | Post-stroke intervention context is outside the healthy thesis setting. | no |
| \[Ben20\] | Benzy et al. *Motor Imagery Hand Movement Direction Decoding Using Brain Computer Interface to Aid Stroke Recovery and Rehabilitation*. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2020. | excluded from mainline narrative | patient | mixed hand direction task | abstract only | no | rehabilitation methods only | Useful if a rehab engineering comparison is needed. | Stroke-direction decoding is not Section 2.1 physiology evidence. | no |
| \[Seb20\] | Sebastián-Romagosa et al. *EEG Biomarkers Related With the Functional State of Stroke Patients*. Frontiers in Neuroscience, 2020. | excluded from mainline narrative | mixed | resting state and rehab MI-BCI | abstract only | no | none or rehab background only | Useful for stroke EEG biomarkers and laterality metrics. | Not a healthy hand-MI physiology paper. | no |
| \[Lea14\] | Leamy et al. *An exploration of EEG features during recovery following stroke – implications for BCI-mediated neurorehabilitation therapy*. Journal of NeuroEngineering and Rehabilitation, 2014. | excluded from mainline narrative | mixed | movement task | abstract only | no | rehab transferability note only | Useful for patient-specific adaptation arguments. | Not a healthy MI physiology source. | no |
| \[Iri18\] | Irimia et al. *High Classification Accuracy of a Motor Imagery Based Brain-Computer Interface for Stroke Rehabilitation Training*. Frontiers in Robotics and AI, 2018. | excluded from mainline narrative | patient | left-right hand MI | abstract only | no | rehab context only | Useful only if comparing healthy and patient control accuracy. | Patient cohort and feedback-rich rehab context make it non-transferable to Section 2.1 claims. | no |

## Final note on use status

### Essential

- \[Pfu06\]
- \[Mcf04\]
- \[Zap20b\]
- \[Xu19\]
- \[Rim23b\]

These are the main papers for Section 2.1 and its immediate physiology-to-design bridge.

### Optional

- \[Men18\]
- \[Arp20\]
- \[San19\]
- \[Tid20\]
- \[Che21\]
- \[Men19\]
- \[Gro24\]
- \[Vas21\]
- \[Fil20\]
- \[Rob18\]
- \[Tsu21\]
- \[Zha22\]
- \[Wan19\]
- \[Cat19\]
- \[Yan14\]
- \[Ang12\]
- \[San10\]
- \[Lu13\]
- \[Nae09\]

These can support methods, variability, or decoder-design discussion, but should not dominate the core Section 2.1 narrative.

### Provisional

- \[Neu99\]
- \[Pfu97\]
- \[Pfu05\]
- \[Bla22\]

These are potentially useful, but current use should remain limited until full-text tracing is completed.

### Keep excluded from the Section 2.1 mainline

- \[Has13\]
- \[Kwo18\]
- \[Li19\]
- \[Man22\]
- \[Rem19\]
- \[Ben20\]
- \[Seb20\]
- \[Lea14\]
- \[Iri18\]

These may still be useful for transferability warnings, rehab context, or later discussion sections, but they should not anchor the healthy hand-MI sensorimotor physiology subsection.

---

## References

\[Pfu06\] G. Pfurtscheller, C. Brunner, A. Schlögl, and F. H. L. D. Silva, “Mu rhythm (de)synchronization and EEG single-trial classification of different motor imagery tasks,” *NeuroImage*, vol. 31 1, pp. 153–9, May 2006, doi: [10.1016/J.NEUROIMAGE.2005.12.003](https://doi.org/10.1016/J.NEUROIMAGE.2005.12.003).

\[Mcf04\] D. McFarland, L. A. Miner, T. Vaughan, and J. Wolpaw, “Mu and Beta Rhythm Topographies During Motor Imagery and Actual Movements,” *Brain Topography*, vol. 12, pp. 177–186, 2004, doi: [10.1023/A:1023437823106](https://doi.org/10.1023/A:1023437823106).

\[Zap20b\] D. Zapała *et al.*, “The effects of handedness on sensorimotor rhythm desynchronization and motor-imagery BCI control,” *Scientific Reports*, vol. 10, Feb. 2020, doi: [10.1038/s41598-020-59222-w](https://doi.org/10.1038/s41598-020-59222-w).

\[Xu19\] K. Xu, Y. Huang, and J. Duann, “The Sensitivity of Single-Trial Mu-Suppression Detection for Motor Imagery Performance as Compared to Motor Execution and Motor Observation Performance,” *Frontiers in Human Neuroscience*, vol. 13, Aug. 2019, doi: [10.3389/fnhum.2019.00302](https://doi.org/10.3389/fnhum.2019.00302).

\[Rim23b\] S. Rimbert, D. Trocellier, and F. Lotte, “Impact of the baseline temporal selection on the ERD/ERS analysis for Motor Imagery-based BCI,” *2023 45th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)*, pp. 1–4, Jul. 2023, doi: [10.1109/EMBC40787.2023.10340748](https://doi.org/10.1109/EMBC40787.2023.10340748).

\[Men18\] J. Meng *et al.*, “A Study of the Effects of Electrode Number and Decoding Algorithm on Online EEG-Based BCI Behavioral Performance,” *Frontiers in Neuroscience*, vol. 12, Apr. 2018, doi: [10.3389/fnins.2018.00227](https://doi.org/10.3389/fnins.2018.00227).

\[Arp20\] P. Arpaia, F. Donnarumma, A. Esposito, and M. Parvis, “Channel Selection for Optimal EEG Measurement in Motor Imagery-Based Brain-Computer Interfaces,” *International journal of neural systems*, pp. 2150003, Nov. 2020, doi: [10.1142/s0129065721500039](https://doi.org/10.1142/s0129065721500039).

\[San19\] C. Sannelli, C. Vidaurre, K. Müller, and B. Blankertz, “A large scale screening study with a SMR-based BCI: Categorization of BCI users and differences in their SMR activity,” *PLoS ONE*, vol. 14, Jan. 2019, doi: [10.1371/journal.pone.0207351](https://doi.org/10.1371/journal.pone.0207351).

\[Tid20\] J. Tidare, M. Leon, and E. Åstrand, “Time-resolved estimation of strength of motor imagery representation by multivariate EEG decoding,” *Journal of Neural Engineering*, vol. 18, Dec. 2020, doi: [10.1088/1741-2552/abd007](https://doi.org/10.1088/1741-2552/abd007).

\[Bla22\] C. F. Blanco-Díaz, J. M. Antelis-Ortíz, and A. F. Ruiz-Olaya, “Comparative Analysis of Spectral and Temporal Combinations in CSP-based Methods for Decoding Hand Motor Imagery Tasks.” *Journal of neuroscience methods*, pp. 109495, Feb. 2022, doi: [10.1016/j.jneumeth.2022.109495](https://doi.org/10.1016/j.jneumeth.2022.109495).

\[Che21\] Y. Y. Chen, K. Lambert, C. Madan, and A. Singhal, “Mu oscillations and motor imagery performance: A reflection of intra-individual success, not inter-individual ability.” *Human movement science*, vol. 78, pp. 102819, May 2021, doi: [10.1016/j.humov.2021.102819](https://doi.org/10.1016/j.humov.2021.102819).

\[Men19\] J. Meng and B. He, “Exploring Training Effect in 42 Human Subjects Using a Non-invasive Sensorimotor Rhythm Based Online BCI,” *Frontiers in Human Neuroscience*, vol. 13, Apr. 2019, doi: [10.3389/fnhum.2019.00128](https://doi.org/10.3389/fnhum.2019.00128).

\[Gro24\] V. G. von Groll *et al.*, “Large scale investigation of the effect of gender on mu rhythm suppression in motor imagery brain-computer interfaces,” *Brain Computer Interfaces (Abingdon, England)*, vol. 11, pp. 87–97, May 2024, doi: [10.1080/2326263X.2024.2345449](https://doi.org/10.1080/2326263X.2024.2345449).

\[Vas21\] A. Vasilyev, Y. O. Nuzhdin, and A. Kaplan, “Does Real-Time Feedback Affect Sensorimotor EEG Patterns in Routine Motor Imagery Practice?” *Brain Sciences*, vol. 11, Sep. 2021, doi: [10.3390/brainsci11091234](https://doi.org/10.3390/brainsci11091234).

\[Fil20\] C. A. S. Filho *et al.*, “On the (in)efficacy of motor imagery training without feedback and event-related desynchronizations considerations,” *Biomedical Physics & Engineering Express*, vol. 6, Apr. 2020, doi: [10.1088/2057-1976/ab8992](https://doi.org/10.1088/2057-1976/ab8992).

\[Ors20\] B. Orset, K. Lee, R. Chavarriaga, and J. Millán, “User Adaptation to Closed-Loop Decoding of Motor Imagery Termination,” *IEEE Transactions on Biomedical Engineering*, vol. 68, pp. 3–10, Jun. 2020, doi: [10.1109/TBME.2020.3001981](https://doi.org/10.1109/TBME.2020.3001981).

\[Sis24\] H. M. Sisti, A. Beebe, E. Gabrielsson, and M. Bishop, “Postmovement Beta Rebound in Real and Imagined Movement.” *Motor control*, pp. 1–16, Aug. 2024, doi: [10.1123/mc.2023-0033](https://doi.org/10.1123/mc.2023-0033).

\[Pap24\] S. Papadopoulos, L. Darmet, M. J. Szul, M. Congedo, J. J. Bonaiuto, and J. Mattout, “Surfing beta burst waveforms to improve motor imagery-based BCI,” *Imaging Neuroscience*, vol. 2, Jul. 2024, doi: [10.1101/2024.07.18.604064](https://doi.org/10.1101/2024.07.18.604064).

\[Pap23\] S. Papadopoulos, M. J. Szul, M. Congedo, J. Bonaiuto, and J. Mattout, “Beta bursts question the ruling power for brain–computer interfaces,” *Journal of Neural Engineering*, vol. 21, Sep. 2023, doi: [10.1088/1741-2552/ad19ea](https://doi.org/10.1088/1741-2552/ad19ea).

\[Wan22b\] J. Wang, Y.-H. Chen, J. Yang, and M. Sawan, “Intelligent Classification Technique of Hand Motor Imagery Using EEG Beta Rebound Follow-Up Pattern,” *Biosensors*, vol. 12, Jun. 2022, doi: [10.3390/bios12060384](https://doi.org/10.3390/bios12060384).

\[Abb18c\] H. Abbaspour, N. Mehrshad, and S. Razavi, “An Effective Brain-Computer Interface System Based on the Optimal Timeframe Selection of Brain Signals,” Jun. 01, 2018. doi: [10.15171/ICNJ.2018.07](https://doi.org/10.15171/ICNJ.2018.07).

\[Sou23\] G. H. D. Souza, D. E. D. Santos, H. Bernardino, A. B. Vieira, and L. Motta, “Window-Delay Analysis on EEGNet,” *2023 10th International Conference on Soft Computing & Machine Intelligence (ISCMI)*, pp. 166–170, Nov. 2023, doi: [10.1109/ISCMI59957.2023.10458480](https://doi.org/10.1109/ISCMI59957.2023.10458480).

\[Liu22b\] X. Liu, P. Yan, S. Zhang, and D. Zheng, “Motor imagery classification method based on long and short windows interception,” May 04, 2022. doi: [10.1088/1361-6501/ac6cc8](https://doi.org/10.1088/1361-6501/ac6cc8).

\[Mal21b\] N. S. Malan and S. Sharma, “Time window and frequency band optimization using regularized neighbourhood component analysis for Multi-View Motor Imagery EEG classification,” *Biomed. Signal Process. Control.*, vol. 67, p. 102550, May 2021, doi: [10.1016/J.BSPC.2021.102550](https://doi.org/10.1016/J.BSPC.2021.102550).

\[Rob18\] N. Robinson, K. P. Thomas, and A. P. Vinod, “Neurophysiological predictors and spectro-spatial discriminative features for enhancing SMR-BCI,” *Journal of Neural Engineering*, vol. 15, Oct. 2018, doi: [10.1088/1741-2552/aae597](https://doi.org/10.1088/1741-2552/aae597).

\[Tsu21\] S. Tsuchimoto *et al.*, “Use of common average reference and large-Laplacian spatial-filters enhances EEG signal-to-noise ratios in intrinsic sensorimotor activity,” *Journal of Neuroscience Methods*, vol. 353, Jan. 2021, doi: [10.1016/j.jneumeth.2021.109089](https://doi.org/10.1016/j.jneumeth.2021.109089).

\[Sun18\] L. Sun, Z. Feng, B. Chen, and N. Lu, “A contralateral channel guided model for EEG based motor imagery classification,” *Biomed. Signal Process. Control.*, vol. 41, pp. 1–9, Mar. 2018, doi: [10.1016/j.bspc.2017.10.012](https://doi.org/10.1016/j.bspc.2017.10.012).

\[Cat19\] T. Cattai, S. Colonnese, M.-C. Corsi, D. Bassett, G. Scarano, and F. de V. Fallani, “Phase/Amplitude Synchronization of Brain Signals During Motor Imagery BCI Tasks,” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, vol. 29, pp. 1168–1177, Dec. 2019, doi: [10.1109/TNSRE.2021.3088637](https://doi.org/10.1109/TNSRE.2021.3088637).

\[Yan14\] Y. Yang, S. Chevallier, J. Wiart, and I. Bloch, “Time-frequency optimization for discrimination between imagination of right and left hand movements based on two bipolar electroencephalography channels,” *EURASIP Journal on Advances in Signal Processing*, vol. 2014, Mar. 2014, doi: [10.1186/1687-6180-2014-38](https://doi.org/10.1186/1687-6180-2014-38).

\[Dai20\] H. Dai, S. Su, Y. Zhang, and W. Jian, *Effect of Spatial Filtering and Channel Selection on Motor Imagery BCI*. 2020. doi: [10.1145/3433996.3434046](https://doi.org/10.1145/3433996.3434046).

\[Mal21\] N. S. Malan and S. Sharma, “Motor Imagery EEG Spectral-Spatial Feature Optimization Using Dual-Tree Complex Wavelet and Neighbourhood Component Analysis,” Jan. 16, 2021. doi: [10.1016/J.IRBM.2021.01.002](https://doi.org/10.1016/J.IRBM.2021.01.002).

\[Zha22\] L. Zhang, L. Chen, Z. Wang, X. Zhang, X. Liu, and D. Ming, “Enhancing Visual-Guided Motor Imagery Performance via Sensory Threshold Somatosensory Electrical Stimulation Training,” *IEEE Transactions on Biomedical Engineering*, vol. 70, pp. 756–765, Aug. 2022, doi: [10.1109/TBME.2022.3202189](https://doi.org/10.1109/TBME.2022.3202189).

\[Wan19\] Z. Wang *et al.*, “A BCI based visual-haptic neurofeedback training improves cortical activations and classification performance during motor imagery,” *Journal of Neural Engineering*, vol. 16, Oct. 2019, doi: [10.1088/1741-2552/ab377d](https://doi.org/10.1088/1741-2552/ab377d).

\[Ang12\] K. Ang, Z. Chin, C. Wang, C. Guan, and H. Zhang, “Filter Bank Common Spatial Pattern Algorithm on BCI Competition IV Datasets 2a and 2b,” *Frontiers in Neuroscience*, vol. 6, Mar. 2012, doi: [10.3389/fnins.2012.00039](https://doi.org/10.3389/fnins.2012.00039).

\[San10\] C. Sannelli, T. Dickhaus, S. Halder, E. Hammer, K. Müller, and B. Blankertz, “On Optimal Channel Configurations for SMR-based Brain–Computer Interfaces,” *Brain Topography*, vol. 23, pp. 186–193, Feb. 2010, doi: [10.1007/s10548-010-0135-0](https://doi.org/10.1007/s10548-010-0135-0).

\[Lu13\] J. Lu, D. McFarland, and J. Wolpaw, “Adaptive Laplacian filtering for sensorimotor rhythm-based brain–computer interfaces,” *Journal of Neural Engineering*, vol. 10, Feb. 2013, doi: [10.1088/1741-2560/10/1/016002](https://doi.org/10.1088/1741-2560/10/1/016002).

\[Nae09\] M. Naeem, C. Brunner, and G. Pfurtscheller, “Dimensionality Reduction and Channel Selection of Motor Imagery Electroencephalographic Data,” *Computational Intelligence and Neuroscience*, vol. 2009, Jun. 2009, doi: [10.1155/2009/537504](https://doi.org/10.1155/2009/537504).

\[Neu99\] C. Neuper, A. Schlögl, and G. Pfurtscheller, “Enhancement of left-right sensorimotor EEG differences during feedback-regulated motor imagery.” *Journal of clinical neurophysiology : official publication of the American Electroencephalographic Society*, vol. 16 4, pp. 373–82, Jul. 1999, doi: [10.1097/00004691-199907000-00010](https://doi.org/10.1097/00004691-199907000-00010).

\[Pfu97\] G. Pfurtscheller, C. Neuper, D. Flotzinger, and M. Pregenzer, “EEG-based discrimination between imagination of right and left hand movement.” *Electroencephalography and clinical neurophysiology*, vol. 103 6, pp. 642–51, Dec. 1997, doi: [10.1016/S0013-4694(97)00080-1](https://doi.org/10.1016/S0013-4694(97)00080-1).

\[Pfu05\] G. Pfurtscheller, C. Neuper, C. Brunner, and F. H. L. Silva, “Beta rebound after different types of motor imagery in man.” *Neuroscience letters*, vol. 378 3, pp. 156–9, Apr. 2005, doi: [10.1016/J.NEULET.2004.12.034](https://doi.org/10.1016/J.NEULET.2004.12.034).

\[Has13\] Y. Hashimoto and J. Ushiba, “EEG-based classification of imaginary left and right foot movements using beta rebound,” *Clinical Neurophysiology*, vol. 124, pp. 2153–2160, Nov. 2013, doi: [10.1016/j.clinph.2013.05.006](https://doi.org/10.1016/j.clinph.2013.05.006).

\[Kwo18\] M. Kwon, H. Cho, K. Won, M. Ahn, and S. Jun, “Event-Related Desynchronization (ERD) May Not be Correlated with Motor Imagery BCI Performance,” *2018 IEEE International Conference on Systems, Man, and Cybernetics (SMC)*, pp. 1133–1137, Oct. 2018, doi: [10.1109/SMC.2018.00200](https://doi.org/10.1109/SMC.2018.00200).

\[Li19\] C. Li, T. Jia, Q. Xu, L. Ji, and Y. Pan, “Brain-Computer Interface Channel-Selection Strategy Based on Analysis of Event-Related Desynchronization Topography in Stroke Patients,” *Journal of Healthcare Engineering*, vol. 2019, Aug. 2019, doi: [10.1155/2019/3817124](https://doi.org/10.1155/2019/3817124).

\[Man22\] S. Mansour, J. Giles, K. Ang, K. Nair, K. Phua, and M. Arvaneh, “Exploring the ability of stroke survivors in using the contralesional hemisphere to control a brain–computer interface,” *Scientific Reports*, vol. 12, Sep. 2022, doi: [10.1038/s41598-022-20345-x](https://doi.org/10.1038/s41598-022-20345-x).

\[Rem19\] A. Remsik *et al.*, “Ipsilesional Mu Rhythm Desynchronization and Changes in Motor Behavior Following Post Stroke BCI Intervention for Motor Rehabilitation,” *Frontiers in Neuroscience*, vol. 13, Mar. 2019, doi: [10.3389/fnins.2019.00053](https://doi.org/10.3389/fnins.2019.00053).

\[Ben20\] V. Benzy, A. P. Vinod, R. Subasree, S. Alladi, and K. Raghavendra, “Motor Imagery Hand Movement Direction Decoding Using Brain Computer Interface to Aid Stroke Recovery and Rehabilitation,” *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, vol. 28, pp. 3051–3062, Nov. 2020, doi: [10.1109/TNSRE.2020.3039331](https://doi.org/10.1109/TNSRE.2020.3039331).

\[Seb20\] M. Sebastián-Romagosa *et al.*, “EEG Biomarkers Related With the Functional State of Stroke Patients,” *Frontiers in Neuroscience*, vol. 14, Jul. 2020, doi: [10.3389/fnins.2020.00582](https://doi.org/10.3389/fnins.2020.00582).

\[Lea14\] D. J. Leamy *et al.*, “An exploration of EEG features during recovery following stroke – implications for BCI-mediated neurorehabilitation therapy,” Jan. 28, 2014. doi: [10.1186/1743-0003-11-9](https://doi.org/10.1186/1743-0003-11-9).

\[Iri18\] D. Irimia, R. Ortner, M. Poboroniuc, B. E. Ignat, and C. Guger, “High Classification Accuracy of a Motor Imagery Based Brain-Computer Interface for Stroke Rehabilitation Training,” *Frontiers in Robotics and AI*, vol. 5, Nov. 2018, doi: [10.3389/frobt.2018.00130](https://doi.org/10.3389/frobt.2018.00130).
