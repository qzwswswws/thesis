# 论文进度全景看板 (Progress Dashboard)

| 阶段 | 任务名称 | 状态 | 关联文件 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| **框架** | 目录及项目初始化 | [x] 已完成 | `01_Thesis_LaTeX`, `00_AI_Management` | 结构已优化，归档已建立 |
| **阶段 1** | 绪论与背景 (Chap 1) | [x] 已完成 | `01_Thesis_LaTeX/data/chap01.tex` | 已集成高效注意力算法现状与完善文献 |
| **阶段 2** | 技术基础 (Chap 2) | [x] 初稿完成 | `01_Thesis_LaTeX/data/chap02.tex` | `2.1`--`2.6` 已完成写作并通过编译，后续按统稿节奏再收束 |
| **阶段 3** | 硬件系统 (Chap 3) | [/] 初稿完成 | `01_Thesis_LaTeX/data/chap03.tex` | 已按实测结果补写第 3 章后半部分并通过编译；实验 1/3 已落正文，实验 2 保守表述，实验 4 仍待补测 |
| **阶段 4** | 算法设计 (Chap 4) | [/] 初稿完成 | `01_Thesis_LaTeX/data/chap04.tex` | 已集成 EdgeMIFormer 核心逻辑，并补入补充稳健性验证、通道组合与错误模式分析 |
| **阶段 5** | 实验验证 (Chap 5) | [/] 初稿启动 | `01_Thesis_LaTeX/data/chap05.tex` | 已将主线收束为“22 导到 2 导算法落地 + 双导在线实验验证”，后续补充实时性与真实双导结果 |
| **阶段 6** | 结论与润色 | [ ] 待启动 | 全文 | - |

## 当前节点整合判断

### 已完成主线

*   论文主结构已稳定，`chap01` 至 `chap05` 均已进入可编译正文状态，整篇 `thesis.pdf` 当前为 `67` 页。
*   第 1 章与第 2 章已具备可用初稿，第 3 章已形成完整硬件系统章节，第 4 章已形成完整算法章节，第 5 章已完成“系统集成与验证框架”首轮起草。
*   当前论文主线已明确收束为：`运动想象解码 + 低通道硬件系统 + 边缘部署约束 + 系统级验证`。
*   管理区内与正文已明显脱钩的过程草稿，已开始按 `DEL_` 前缀标记，便于后续统一清理。

### 当前未完成主线

*   第 3 章仍缺少关键定量测试：端到端延迟、无线传输稳定性、功耗/续航、Alpha/眨眼等基础生理验证图。
*   第 5 章仍缺少关键实测结果：`RK3568` 推理延迟、全链路延迟、真实双通道解码结果、移动场景稳定性测试。
*   第 6 章目前仍基本为空，仅保留结构标题，尚未正式写作。
*   全文尚未进入最终统稿阶段，后续仍需统一语言风格、压缩重复表述并补齐最后的图表和结论。

### 当前保留 / 清理判断

*   应继续保留：`Algorithm_Experiment_Execution_Plan.md`、`Chap02_Research_Prompts.md`、第 3 章材料整合与未完成清单、`Prompt_Chap03_Drafting_Codex.md`。
*   已标记可删：`DEL_Chap01_Draft_Efficient_Attention_Review.md`、`DEL_Chap02_Draft_Efficient_Attention_Theory.md`、`DEL_Chap04_Expansion_Draft_20260329.md`。
*   建议暂不删除但可后续再判断：`Edge_Deployment_Literature_List.md`、`New_Report_Fulltext_Download_Priority.md`。

### 当前最优下一步

1. 先补第 3 章最短板的实测材料，使硬件章从“能写”变成“有证据”。
2. 再补第 5 章与这些实测直接相关的结果，尤其是链路时延和双导真实数据验证。
3. 随后完成第 6 章“结论与展望”，再进入全文统稿与删减阶段。
4. “降低 AI 率 / 全文自然化”暂不作为当前主线，统一后移至终稿阶段视实际查重与评阅反馈再决定是否处理。

## 当前聚焦: **第 3 / 5 章实测补齐与全文收束**

*   [x] 确认 `00_AI_Management` 结构
*   [x] 算法第 4 章初稿起草 (EdgeMIFormer)
*   [x] 建立 Codex 最小协作工作流入口 (`_CODEX_QUICKSTART.md`)
*   [x] 盲审视角收敛修订第 1.2 与第 2.2 节
*   [x] 固化近期文本风格要求至 `Writing_Quality_Standards.md`
*   [x] 固化 Undermind（知识簇1）人群与证据边界到 `Chap02_Research_Prompts.md`
*   [x] 优化 `_AI_SYNC_BOARD.md`，加入受限跨 AI 协作机制
*   [x] 新建 `_AI_RELAY_CHAT.md`，用于双 AI 对话式协作
*   [x] 在 `_AI_RELAY_CHAT.md` 建立 T001：讨论既有文献材料去留与整理策略
*   [x] 基于核心原文与证据报告补写第 2 章 `2.1` 两个小节，并完成一轮编译检查
*   [x] 修复 `2.1` 新增文献引用，补录 `[Pfu06] [Mcf04] [Zap20b] [Xu19] [Rim23b]` 等核心 Bib 条目并完成重编译
*   [x] 将后续文献调研重点改写为 `4A/4B` 两个边缘部署知识簇，并补充 `1B` 可选尾部补强提示词
*   [x] 将“硬件优化报告解析与下载清单”交由 Antigravity 接手，并在 `_AI_RELAY_CHAT.md` 建立 T002
*   [x] 完成第 2 章 `2.3`--`2.6` 写作，补入边缘部署、BLE 与 KS1092 相关技术基础，并将研究不足回写到第 1 章
*   [x] 重写 `Algorithm_Experiment_Execution_Plan.md`，将其收束为面向跨设备 AI 助手的实验执行说明，明确协议冻结、实验矩阵、优先级与停止条件
*   [x] 读取 `04_Algorithm_Workbench` 实验汇总并对 `chap04.tex` 开展增量补写，明确小论文主线与本论文补充实验的衔接关系
*   [x] 新建 `DEL_Chap04_Expansion_Draft_20260329.md`（原 `Chap04_Expansion_Draft_20260329.md`），评估第 4 章进一步扩写、正式化命名与新增图片的可行性；现已被正文吸收并标记为可删过程稿
*   [x] 完成第 4 章一轮统稿深化：去除过程性表述，扩写低通道退化与任务收束分析，补入统一协议表、低通道路径比较表和新增图 `C4-9lowchannel_path_compare.png`
*   [x] 已检查并修复 Antigravity 对第 4 章的新改动：补回局部注意力公式结构，编译新增 TikZ 图为 PDF，并完成 `bibtex + xelatex + xelatex`
*   [ ] 执行项目健康检查与 Git 全量同步
*   [x] 已下载 `swkd` GitHub 仓库到 `02_Source_Material/03_Hardware_Workbench/swkd`，提取固件、BLE 协议、上位机功能、板级引脚与采样机制，新增 `Chap03_Hardware_Info_Integration_20260329.md` 作为第 3 章写作前材料整合稿
*   [x] 已复查 `Input_Buffer` 中新增的原理图、BOM、STEP、PCB 包与局部电路截图，整理形成 `Chap03_Material_Inventory_20260329.md`，用于第 3 章材料分层与写作映射
*   [x] 已将 `Input_Buffer` 中的硬件资料迁移至 `02_Source_Material/03_Hardware_Workbench/` 分类目录，解压 `PCB_PCB1_2026-03-29.zip`、规范自动位号图文件名，并新增 `02_Source_Material/03_Hardware_Workbench/README.md`
*   [x] 已新增第 3 章硬件章节专用写作协议 `00_AI_Management/Prompt_Library/Hardware_Chapter_Writing_Protocol.md`，重点约束“硕士论文风格”与“工程手册风格”的边界
*   [x] 已新增可直接调用的起草提示词 `00_AI_Management/Output_Drafts/Prompt_Chap03_Drafting_Codex.md`，供后续正式撰写 `chap03.tex` 前使用
*   [x] 已完成 `chap03.tex` 首轮正式写作，新增硬件结构、协议、前端电路、主控电路、固件流程与联调验证内容，并引入 `C3-1` 至 `C3-5` 图像后通过整篇 `makepdf.bat` 编译
*   [x] 已梳理第 3 章当前所有未完成事项，形成 `00_AI_Management/Output_Drafts/Chap03_Unfinished_Checklist_20260329.md`，按“定量验证项 / 实物材料 / 事实边界 / 图表增强”四类整理待补内容
*   [x] 已将与当前论文无关的旧 `C5-*` 图素材归档至 `99_Archive/Unused_Thesis_Figures/2026-03-29_Original_Chap05`，并完成 `chap05.tex` 首轮写作，补入系统全链路集成、评价指标、实时性实验设计与硬件--算法协同验证框架，整篇重新编译通过
*   [x] 已重新检查项目管理区与正文区，按当前节点重写“已完成 / 未完成 / 可清理”判断，并将 `Chap01/Chap02/Chap04` 的三份过程草稿改名为 `DEL_*.md` 以便后续统一清理
*   [x] 已新增 `00_AI_Management/Output_Drafts/Current_Node_Lookback_and_Outlook_20260329.md`，用于汇总当前节点的回顾、风险边界、未完成主线与最优下一步
*   [x] 已新增 `00_AI_Management/Prompt_Library/LaTeX_Compilation_Protocol.md`，并在 `_AI_ENTRY_POINT.md` 中加入“论文编译与日志排障任务”路由，用于约束 Antigravity/Codex 后续的编译判断与排障动作
*   [x] 已将 `00_AI_Management/Prompt_Library/AIGC_Optimization_Protocol.md` 从活跃 `Prompt_Library` 移出并归档至 `99_Archive/Prompt_Library_Archive/2026-03-30/`，同时移除 `_AI_ENTRY_POINT.md` 中对应任务路由
*   [x] 已明确将“降低 AI 率 / 全文自然化”后移到终稿阶段处理；当前主线重新聚焦于第 3 章与第 5 章实测补齐、第 6 章写作以及整篇事实性统稿
*   [x] 已新增 `00_AI_Management/Output_Drafts/Chap03_Hardware_Validation_Experiment_Plan_20260330.md`，将第 3 章需要补齐的硬件验证实验收束为“采集有效性、无线稳定性、端到端延迟、功耗续航”四组主实验，并给出优先级与最小可交付实验包
*   [x] 已新增 `00_AI_Management/Output_Drafts/EEG_Headband_Status_Path_Foundation_Index_20260331.md`，将论文文件夹内与“脑电头环/便携式低通道脑电终端”相关的研究现状、路径方案与工作基础材料汇总为一份可直接查阅的索引文档，并明确当前强项在系统闭环与板级基础，短板在头环形态证据与量化实测
*   [x] 已依据 `Chap03_Writing_Status_And_Data_Index_20260401.md` 与已完成实验结果重写第 3 章验证部分：将“脑电采集与显示功能验证”改写为含 Alpha 实验结果的“脑电采集有效性验证”，补入标签链路响应统计表与模式对比表，并将无线稳定性、供电续航明确区分为“当前可保守声称”与“后续待补测”两类结论；整篇 `makepdf.bat` 重新编译通过，`thesis.pdf` 当前为 `64` 页
*   [x] 已基于 `02_Source_Material/04_Algorithm_Workbench/Charge` 中的补充实验与图件扩写第 4 章：新增“补充稳健性验证与误差结构分析”一节，补入多随机种子复现、`PhysioNet eegmmidb` 外部验证、`EEGNet` 最小经典对照、通道组合 pilot 与聚合混淆矩阵分析，并引入 `C4-12_confusion_matrix_key_conditions.png` 与 `C4-13_channel_combo_pilot_2class.png` 两幅新图；整篇 `makepdf.bat` 重新编译通过，`thesis.pdf` 当前为 `67` 页
*   [x] 已按当前节点重构第 5 章叙事主线：将章节标题改为“`双导端侧系统集成与在线实验验证`”，并将前半章收束为“22 导到 2 导的算法落地路径”“在线实验基础与评价口径”“在线链路时延与推理分析”“硬件在线实验与系统验证”四个层次，明确在线实验应以 `C3/C4` 双导左右手二分类为主目标；整篇 `makepdf.bat` 重新编译通过，`thesis.pdf` 仍为 `67` 页
*   [x] 宸插皢 `forexp/datasets.zip` 鍐呯殑 `BCI Competition IV 2b` 鏁版嵁闆嗚惤鍦拌嚦 `02_Source_Material/04_Algorithm_Workbench/datasets/`锛屽鐢?`standard_2b_strict_TE` 鍙屽鍖?MAT鏁版嵁锛屾柊澧?`pretrain_2b_transfer_local_mi.py` 瀹屾垚鈥?b 棰勮缁?+ 鏈湴涓よ疆鍙屽绂荤嚎杩佺Щ瀵规瘮鈥濓紝骞朵繚瀛樻潈閲嶈嚦 `results/2b_pretrain_transfer/weights/conformer_b2_c3c4_pretrain_2b.pt`锛涘綋鍓嶅垵姝ョ粨鏋滀负锛氶殢鏈哄垵濮嬪寲璺ㄨ疆鍧囧€?`0.5000`锛?2b 棰勮缁冨垵濮嬪寲璺ㄨ疆鍧囧€?`0.5250`
*   [x] 宸蹭慨澶?`nearalQT` 鍦ㄧ嚎 MI 鑱斿姩榛樿瑙ｉ噴鍣ㄩ€夋嫨閫昏緫锛氫笂浣嶆満鐜板湪浼氫紭鍏堜娇鐢?`D:/pycode/cspsvm/EEG_SVM-master/EEG_SVM-master/.conda/python.exe` 浣滀负 `online_mi_round_bridge.py` 鐨?Python 鐜锛屾壘涓嶅埌鏃跺啀鍥為€€鍒扮郴缁?`python`锛屼互淇鈥滃瓙杩涚▼鍚姩浜嗕絾鍥犵己灏?torch 鑰屾棤娉曞畬鎴愯缁冣€濈殑鍦ㄧ嚎瀹為獙鍗￠】闂
*   [x] 宸插鏈€鏂颁竴杞?`20260401_141355_mi_lr` 鍋氬揩閫熺绾垮鐩橈細浠ュ墠涓よ疆 `20260401_122743_mi_lr + 20260401_123310_mi_lr` 浣滀负璁粌闆嗭紝浣跨敤鈥?4s imagery + 8-30Hz + resample1000 + per-trial z-score鈥濋澶勭悊鍜?`ConformerB2` 杩涜绠€鐗堟祴璇曪紱缁撴灉鏄剧ず闅忔満鍒濆鍖栧潎鍊间负 `0.5000`锛?2b 棰勮缁冨垵濮嬪寲鍧囧€间负 `0.5667`锛屾彁鍗?`+0.0667`锛屽凡鏂板缓 `MI_Last_Session_Quickcheck_20260401.md`
*   [x] 宸插杩涘叆鍦ㄧ嚎鑱斿姩闃舵鐨?4 杞?`20260401_144934_mi_lr ~ 20260401_150213_mi_lr` 鍋氱郴缁熷垎鏋愶紝鏂板缓 `MI_Online_Sessions_Analysis_20260401.md`锛屽熀浜庘€滃墠搴忚疆娆¤缁冦€佸悗涓€杞祴璇曗€濈殑绱Н璇勪及琛ㄦ槑锛氬綋鍓?4 杞湪绾挎暟鎹畬鏁存€ц壇濂斤紝浣?`2b` 棰勮缁冨垵濮嬪寲鏁翠綋骞舵湭绋冲畾浼樹簬闅忔満鍒濆鍖栵紙Baseline `0.5222` vs Pretrained `0.5167`锛夛紝褰撳墠鏇寸鍚堚€滈璁粌鍏锋湁娼滃湪甯姪浣嗘敹鐩婁粛鍙椾紶鎰熷櫒婕傜Щ涓庡皬鏍锋湰闄愬埗鈥濈殑鍒ゆ柇
