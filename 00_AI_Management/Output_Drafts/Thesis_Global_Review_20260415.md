# 论文全文阶段性审视与问题分析（2026-04-15）

## 一、总体判断

当前论文已经具备较完整的六章骨架，且第 4、5 章主线已基本围绕“低通道端侧约束下的算法收束与系统落地”统一起来。最新全文页数已达到约 76 页，说明篇幅上已接近硕士论文可交稿区间。

但从“能够编译通过”到“适合送审”之间，当前仍存在三个核心差距：

1. 结尾部分尚未形成闭环，摘要与第 6 章仍是占位状态。
2. 第 5 章的部分小节仍偏“实验设计/验证计划”而非“已完成结果”，与章节标题中的“初步验证”强度仍有落差。
3. 第 1 章虽然主线已改善，但其叙述张力、问题链压缩能力和创新点映射还可以进一步增强，以更好统领第 4、5 章。

因此，当前论文的真实状态更接近：

- 结构已定型
- 主体章节可用
- 收口章节与证据边界仍需重点打磨

## 二、按严重程度排序的主要问题

### A. 高优先级问题

#### A1. 摘要仍为占位文本，属于送审级阻塞项

- 位置：[abstract.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/abstract.tex)
- 现状：中英文摘要仍为模板式占位内容，尚未反映本文的真实研究问题、方法路径、系统实现和结论。
- 风险：这是最直接的完成度问题，会显著拉低整篇论文的正式感。
- 建议：
  - 在第 5 章最终口径稳定后，再统一撰写中文摘要与英文摘要。
  - 摘要中必须明确：双导端侧场景、任务收束、改进型自注意力方法、系统集成、在线联动初步验证。

#### A2. 第 6 章尚未展开，创新点与全文结论还没有最终归拢

- 位置：[chap06.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap06.tex#L1)
- 现状：仅有“全文总结 / 现存不足 / 研究展望”三级标题，正文为空。
- 风险：当前第 1、4、5 章已经出现创新点雏形，但尚未被结论章统一提炼，导致全文主张缺少收口。
- 建议：
  - 先写“全文总结”，用 3 条贡献主线归拢。
  - 再写“现存不足”，重点承认真实在线证据仍偏 pilot、RK3568 实测仍需补强、人机协同尚处探索。
  - 最后写“研究展望”，把更自然范式、在线协同训练、人机双向适配放在这里。

#### A3. 第 5 章仍混有“计划性描述”，证据强度与标题不完全匹配

- 位置：
  - [chap05.tex:132](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap05.tex#L132)
  - [chap05.tex:138](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap05.tex#L138)
  - [chap05.tex:152](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap05.tex#L152)
  - [chap05.tex:158](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap05.tex#L158)
- 现状：
  - “RK3568 原型推理节点延迟测试”仍以“应以”“建议”“若后续”为主。
  - “全链路延迟优化验证”仍主要描述应如何做实验。
  - “双导左右手在线实验设计与当前定位”与“移动场景稳定性测试”也更像设计说明而非实证结果。
- 风险：章节标题已是“双导端侧系统集成、在线实现与初步验证”，若这些小节仍主要是计划口吻，答辩时容易被追问“哪些是真的做了，哪些只是计划”。
- 建议：
  - 将第 5 章内容明确分成三层：
    - 已完成并可直接主张的结果
    - 已完成但仅能作探索性表述的 pilot 结果
    - 尚未完成的验证项（改写为边界说明，不单列成结果节）
  - 若近期无法补测 RK3568 与全链路时延，就应将 5.3 部分压缩为“部署边界与待验证节点”，避免写成结果小节。

### B. 中优先级问题

#### B1. 第 1 章问题链已经成形，但仍略偏“压缩”，叙述张力还可以增强

- 位置：
  - [chap01.tex:4](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap01.tex#L4)
  - [chap01.tex:14](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap01.tex#L14)
  - [chap01.tex:41](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap01.tex#L41)
  - [chap01.tex:53](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap01.tex#L53)
- 现状：
  - 研究现状的三分法已经合理。
  - 但“背景 -> 现状 -> 不足 -> 本文主线”的过渡仍较快，绪论的叙事张力还不够。
- 风险：导师或评审读起来会觉得方向是对的，但“为什么一定要这样做”还可以更顺更有说服力。
- 建议：
  - 把“低成本双导端侧脑机接口”的现实需求写得再具体一点。
  - 把“高密度标准任务为何不能直接映射到真实系统”写成更清晰的问题链。
  - 在 1.3 中进一步把四个不足对应到后续第 3、4、5 章。

#### B2. 第 2 章边界基本清楚，但仍需继续强化“路线选择”而非“材料堆叠”

- 位置：
  - [chap02.tex:25](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap02.tex#L25)
  - [chap02.tex:95](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap02.tex#L95)
  - [chap02.tex:101](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap02.tex#L101)
- 现状：
  - 第 2 章已明显优于早期版本，不再只是“技术知识堆叠”。
  - 但其中部分平台与部署内容，仍带有较强的外部证据综述色彩。
- 风险：若第 5 章后续实测证据补不上，第 2 章中的平台讨论会显得偏多、偏远。
- 建议：
  - 继续强化“为什么本文选择局部高效自注意力 + 低通道端侧友好路线”。
  - 把更偏背景性的外部平台描述控制在“证明可行性”的程度，不要写得像独立综述。

#### B3. 第 3 章与第 5 章之间仍存在“基础验证”与“在线前提验证”的轻微重叠

- 位置：
  - [chap03.tex:157](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap03.tex#L157)
  - [chap05.tex:148](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap05.tex#L148)
- 现状：
  - 第 3 章已经写了 Alpha 与标签链路验证。
  - 第 5 章又从“在线实验前的基础链路验证”角度重新调用这两类结果。
- 风险：如果处理不好，容易让读者觉得第 5 章在复述第 3 章。
- 建议：
  - 第 3 章只讲“硬件系统具备什么能力、验证到什么程度”。
  - 第 5 章只讲“这些能力为什么足以支撑在线实验前提”。
  - 最好在第 5 章加一个总表，把“已完成基础验证 -> 对应支撑的在线环节”一一映射。

### C. 低优先级问题

#### C1. 第 4 章是当前最强章节，但“低通道改进”仍需再提炼成更显式的结论

- 位置：
  - [chap04.tex:117](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap04.tex#L117)
  - [chap04.tex:182](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap04.tex#L182)
  - [chap04.tex:237](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap04.tex#L237)
- 现状：
  - 低通道退化、任务收束、配置优化、稳健性验证都已经具备。
  - 但“到底改进了什么、为什么适合端侧”还可以在节末和章末再说得更集中。
- 建议：
  - 在 4.3 或本章小结中加一个“本章形成的 3 条确定性结论”。
  - 明确“端侧”体现在哪里：复杂度受控、量化友好、低通道适配，而非板端实测。

#### C2. 排版层面还有少量 Overfull / Underfull 警告，但当前不构成主要阻塞

- 位置：[thesis.log](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/thesis.log)
- 现状：存在若干 `Underfull \vbox` 与少量 `Overfull \hbox` 警告。
- 风险：主要影响细节美观，不影响主线判断。
- 建议：
  - 等正文结构稳定后再统一做一轮排版清理。
  - 当前不宜为微小排版问题打断结构收口。

## 三、按章节的完成度判断

- [chap01.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap01.tex)：约 80%  
  主线已对，但还可增强叙述逻辑与研究不足的映射张力。

- [chap02.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap02.tex)：约 88%  
  结构较稳，后续只需继续压缩无关综述感，强化“为何选这条路线”。

- [chap03.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap03.tex)：约 82%  
  工程基础扎实，主要不足是长时稳定性与功耗仍未形成强量化结果。

- [chap04.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap04.tex)：约 92%  
  当前最成熟，已具备论文核心技术章的形态。

- [chap05.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap05.tex)：约 72%  
  结构和口径已比早期版本好很多，但仍需继续区分“完成结果”和“设计边界”。

- [chap06.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/chap06.tex)：约 5%  
  仍为空骨架。

- [abstract.tex](C:/Users/qzwsw/Documents/thesis/01_Thesis_LaTeX/data/abstract.tex)：约 5%  
  仍为占位。

## 四、最建议的收口顺序

### 第一优先级

1. 先把第 5 章“结果 / pilot / 计划”三层口径拆清。
2. 明确哪些在线结果可直接主张，哪些只能作为探索性说明。

### 第二优先级

3. 写第 6 章，用统一语言归拢 3 条主贡献与 3 条边界。
4. 写中英文摘要，确保其与第 1、4、5、6 章口径完全一致。

### 第三优先级

5. 回头增强第 1 章叙述张力，把问题链再压实。
6. 最后再统一做排版、措辞和小范围重复清理。

## 五、我当前的总体意见

现在**不需要再推翻重做结构**。真正需要的是：

- 继续巩固第 4 章作为核心技术章的地位；
- 把第 5 章从“有很多想做的验证”收成“已完成什么、验证到何程度、还有什么边界”；
- 用第 6 章和摘要把全文真正闭环。

换句话说，当前论文的问题已经不是“方向不对”，而是“收口不够干净”。只要把第 5 章证据边界、第 6 章结论提炼和摘要写好，这篇论文就会从“完成了很多工作”变成“形成了一篇能讲清楚自身价值的论文”。
