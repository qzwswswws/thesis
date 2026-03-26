# New Report Fulltext Download Priority

This note consolidates what is worth downloading in full from the newly added edge-deployment and MI-physiology follow-up reports.

## A. K4 edge deployment: highest-value originals

These are the papers most worth having as original full texts for Chapters 3-4 and for platform/deployment claims.

| Priority | Paper ID | Why it matters | Local status | Action |
| --- | --- | --- | --- | --- |
| A1 | `Wan20` | Direct MI-EEG deployment on Cortex-M4F/M7 with concrete accuracy, memory, latency, and energy trade-offs. | `Wan20.pdf` already local in `K4_Edge_Deployment_Optimization` | No re-download needed; parse the original carefully. |
| A1 | `Sch20` | Best quantized MI-EEG CNN edge anchor: 8-bit, PULP, latency, energy, and memory reduction are all directly useful. | No clearly identified local original yet. `EdgeDL2020_cameraReady.pdf` may be related but is not confirmed. | Download official full text. |
| A1 | `Wan22b` | Strongest direct MI-EEG efficiency result with channel selection, quantization, `30 μJ` and `2.95 ms` level claims. | Original PDF already local in `03_Literature/K4A_Edge_Compression_Quantization` as `MI-BMInet...pdf` | No re-download needed; use as a core source. |
| A1 | `Ene23` | Direct Arduino Nano 33 Sense PTQ deployment evidence; very thesis-friendly for wearable low-cost deployment. | `Low-power_EEGNet-based_Brain-Computer_Interface_implemented_on_an_Arduino_Nano_33_Sense.pdf` already local | No re-download needed; parse the original carefully. |
| A1 | `Pac24` | Best platform-comparison paper across CPU, Jetson, and FPGA for MI classification. | Local HTML capture is present in `K4_Edge_Deployment_Optimization` | Download the official PDF as well. |
| A2 | `Bia24` | Rare on-device learning / subject-shift adaptation evidence for MI-EEG, which is highly valuable for real-world deployment discussion. | No local original found | Download official full text. |
| A2 | `Asa25` | Closest direct attention-based MI-EEG embedded paper (`TinyEEGConformer`); important for the transformer branch of the thesis. | No local original found | Download official full text. |
| A2 | `Jun24` | Strongest generic tiny-transformer deployment framework paper for memory layout, fused attention, and runtime scheduling claims. | No local original found | Download official full text. |
| A2 | `Bus24` | Strongest adjacent EEG-transformer edge deployment evidence on real low-power hardware. | Only older/related web capture found; no confirmed local original for `Bus24` | Download official full text. |
| A2 | `You24` | Closest RK3568 temporal-model deployment evidence; needed if RK3568/RKNN is discussed concretely. | No local original found | Download official full text. |

### K4 direct link index

- `Wan20`
  - DOI: <https://doi.org/10.1109/MeMeA49120.2020.9137134>
  - ETH repository: <https://www.research-collection.ethz.ch/handle/20.500.11850/495442>
- `Sch20`
  - DOI: <https://doi.org/10.1109/SMARTCOMP50058.2020.00065>
  - ETH repository: <https://www.research-collection.ethz.ch/handle/20.500.11850/457739>
- `Wan22b`
  - DOI: <https://doi.org/10.1109/JSEN.2024.3353146>
  - IBM publication page: <https://research.ibm.com/publications/mi-bminet-an-efficient-convolutional-neural-network-for-motor-imagery-brain-machine-interfaces-with-eeg-channel-selection>
- `Ene23`
  - DOI: <https://doi.org/10.1109/DCIS58620.2023.10335978>
  - IEEE Xplore: <https://ieeexplore.ieee.org/document/10335978>
- `Pac24`
  - DOI: <https://doi.org/10.3390/electronics13091646>
  - MDPI article: <https://www.mdpi.com/2079-9292/13/9/1646>
  - PDF: <https://www.mdpi.com/2079-9292/13/9/1646/pdf>
- `Bia24`
  - DOI: <https://doi.org/10.1145/3675095.3676607>
  - dblp metadata: <https://dblp.org/rec/conf/iswc/BianKMLBRM24.html>
  - available mirror page with downloadable PDF: <https://www.library.sk/arl-sav/en/detail-sav_un_epca-307069-Ondevice-learning-of-EEGNetbased-network-for-wearable-motor-imagery-braincomputer-interface/?disprec=2&iset=1>
- `Asa25`
  - DOI: <https://doi.org/10.1109/SAS65169.2025.11105112>
- `Jun24`
  - DOI: <https://doi.org/10.1109/TC.2024.3500360>
  - accepted-manuscript PDF: <https://iris.polito.it/bitstream/11583/2996571/1/TinyFormer_Extension.pdf>
- `Bus24`
  - DOI: <https://doi.org/10.1109/TBCAS.2024.3357509>
  - PubMed: <https://pubmed.ncbi.nlm.nih.gov/38261487/>
  - accepted-manuscript PDF: <https://iris.polito.it/retrieve/handle/11583/2996576/67c60555-ede5-4eee-b1fa-7a7108edfc55/Reducing_False_Alarms_in_Wearable_Seizure_Detection_With_EEGformer_A_Compact_Transformer_Model_for_MCUs.pdf>
- `You24`
  - DOI: <https://doi.org/10.1109/SEAI62072.2024.10674174>
  - IEEE Xplore: <https://ieeexplore.ieee.org/document/10674174>

## B. K4 edge deployment: useful but secondary

These are helpful support papers, but they do not need to be downloaded before the A-tier set is digested.

| Paper ID | Why it is secondary |
| --- | --- |
| `Ism23` | Useful for board-level RK3568 power and rough NPU scale, but modality mismatch is high. |
| `Bus22` | Good earlier EEGformer deployment context, but `Bus24` is the stronger version. |
| `Bus24b` | Strong tiny-transformer biosignal efficiency result, but ECG is less transferable than EEG. |
| `Bur21b` | Good MCU transformer-kernel feasibility paper, but not EEG-specific. |
| `Bur22` | Strong wearable biosignal transformer deployment support, but sEMG transferability is only medium. |
| `Mir24` | Important if the thesis compares streaming TCNs with attention, otherwise secondary. |
| `Lin24` | Good FPGA quantized-transformer support, but forecasting is farther from MI-EEG. |

## C. MI physiology follow-up: worth downloading only if Section 2.1 will be strengthened further

If the plan is to harden the extended physiology discussion, these are the most worthwhile originals from the follow-up review.

| Priority | Paper ID | Why it matters |
| --- | --- | --- |
| P1 | `Men19` | Strong direct evidence that training changes separability/lateralization before raw `C3/C4` amplitude changes. |
| P1 | `Wan19` | Best multimodal feedback paper with direct improvement in ERD and classification performance. |
| P1 | `Ono18b` | Strong evidence that physiologically congruent proprioceptive feedback matters more than generic feedback. |
| P1 | `Vas21` | Important boundary-condition paper showing feedback does not always amplify ERD in experienced users. |
| P1 | `Zho22b` | Randomized tactile-assisted MI training paper with clear accuracy and physiology gains. |
| P2 | `Tar20` | Strongest modern foot-MI beta-rebound paper with explicit discrimination numbers. |
| P2 | `Sis24` | Best modern paper to support the claim that PMBR exists in MI but is weaker than in execution. |
| P2 | `San19` | Large-cohort variability anchor for user heterogeneity beyond the simple left/right average story. |
| P2 | `Kap24` | Recent large-scale evidence linking MI-BCI performance more to SNR than connectivity. |

### MI physiology follow-up link index

- `Men19`
  - Frontiers full text: <https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2019.00128/full>
  - PDF: <https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2019.00128/pdf>
  - DOI: <https://doi.org/10.3389/fnhum.2019.00128>
- `Wan19`
  - PubMed: <https://pubmed.ncbi.nlm.nih.gov/31365911/>
  - DOI: <https://doi.org/10.1088/1741-2552/ab377d>
- `Ono18b`
  - PubMed: <https://pubmed.ncbi.nlm.nih.gov/29698736/>
  - DOI: <https://doi.org/10.1016/j.neuropsychologia.2018.04.016>
- `Vas21`
  - PMC full text: <https://pmc.ncbi.nlm.nih.gov/articles/PMC8469546/>
  - DOI: <https://doi.org/10.3390/brainsci11091234>
- `Zho22b`
  - PubMed: <https://pubmed.ncbi.nlm.nih.gov/36001509/>
  - DOI: <https://doi.org/10.1109/TBME.2022.3201241>
- `Tar20`
  - PLOS article: <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0230184>
  - PMC full text: <https://pmc.ncbi.nlm.nih.gov/articles/PMC7077852/>
  - DOI: <https://doi.org/10.1371/journal.pone.0230184>
- `Sis24`
  - DOI: <https://doi.org/10.1123/mc.2023-0033>
- `San19`
  - PLOS article: <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0207351>
  - DOI: <https://doi.org/10.1371/journal.pone.0207351>
- `Kap24`
  - DOI: <https://doi.org/10.1088/1741-2552/ad7a24>

## Practical order

If time is limited, use this order:

1. `Sch20`
2. `Pac24`
3. `Bia24`
4. `Asa25`
5. `Jun24`
6. `Bus24`
7. `You24`
8. `Men19`
9. `Wan19`
10. `Ono18b`

Notes:

- `Wan20`, `Wan22b`, and `Ene23` are already strong and are already present locally, so they should be parsed rather than re-downloaded.
- `Pac24` and `TinyML/Hua24` currently have local HTML-style captures, but PDF originals are still preferable if the thesis will quote exact numeric results.
