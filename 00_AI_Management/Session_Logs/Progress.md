# 论文进度全景看板 (Progress Dashboard)

| 阶段 | 任务名称 | 状态 | 关联文件 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| **框架** | 目录及项目初始化 | [x] 已完成 | `01_Thesis_LaTeX`, `00_AI_Management` | 结构已优化，归档已建立 |
| **阶段 1** | 绪论与背景 (Chap 1) | [x] 已完成 | `01_Thesis_LaTeX/data/chap01.tex` | 已集成高效注意力算法现状与完善文献 |
| **阶段 2** | 技术基础 (Chap 2) | [x] 初稿完成 | `01_Thesis_LaTeX/data/chap02.tex` | `2.1`--`2.6` 已完成写作并通过编译，后续按统稿节奏再收束 |
| **阶段 3** | 硬件系统 (Chap 3) | [/] 初稿完成 | `01_Thesis_LaTeX/data/chap03.tex` | 已完成首轮完整起草并通过编译，后续可继续补充定量测试与实物照片 |
| **阶段 4** | 算法设计 (Chap 4) | [/] 初稿完成 | `01_Thesis_LaTeX/data/chap04.tex` | 已集成 EdgeMIFormer 核心逻辑，待绘图与润色 |
| **阶段 5** | 实验验证 (Chap 5) | [/] 初稿启动 | `01_Thesis_LaTeX/data/chap05.tex` | 已完成系统集成与验证框架首轮起草，后续补充实时性与真实双导结果 |
| **阶段 6** | 结论与润色 | [ ] 待启动 | 全文 | - |

## 当前节点整合判断

### 已完成主线

*   论文主结构已稳定，`chap01` 至 `chap05` 均已进入可编译正文状态，整篇 `thesis.pdf` 当前为 `62` 页。
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
*   [x] 已优化 `00_AI_Management/Prompt_Library/AIGC_Optimization_Protocol.md`，将其从“检测规避导向”收束为“学术自然化与模板痕迹消解”协议，并在 `_AI_ENTRY_POINT.md` 中加入对应任务路由
