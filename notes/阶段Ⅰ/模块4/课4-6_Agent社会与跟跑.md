# 课 4-6：Agent 社会与多 Agent 跟跑（含 A2A 与去中心化）

> 模块 4：Agent 实践（收尾）｜ 教材：ai-agent-book ch10 末段「去中心化模式」「Agent 社会」
> 状态：✅ 讲义已生成（2026-08-14），内容基于本地 clone 教材原文逐节提取

## 教学目标
1. 掌握去中心化模式的三种形态（MetaGPT/AutoGen/Swarm）与 handoff 风险
2. 理解 A2A 协议的定位（跨组织 Agent 互操作）
3. 认识 Agent 社会的三类涌现（社交/经济/博弈）——多 Agent 的前沿图景

## 知识点详解

### 1. 去中心化模式
- 动机：模拟人类社会的分工制衡；解决管理者崩溃这一**单点故障**（微服务术语：编排 vs 编舞）
- **MetaGPT**：把软件公司 SOP 编码进多 Agent（PM→Architect→PM→Engineer→QA 固定流水线）；"移交包"三要素 = 任务描述 + 已确认事实与约束 + 结构化产物引用（路径而非内容）；共享消息池+按角色订阅——但如实指出：SOP 固定，近似工作流，控制流并非真正去中心化
- **AutoGen 群聊**：共享对话记录 + 中心化调度（GroupChatManager 选发言者）的混合形态
- **OpenAI Swarm**：控制流上真正对等去中心化；handoff 把控制权像接力棒流转，只传任务包和产物引用，不暴露私有轨迹；**风险是成环**——需 visited_agents 循环检测、remaining_budget 与移交次数上限
- 注：2025 年以来"Agent Swarm"两种用法——handoff 网络 vs 规模化管理者模式（Kimi K2.5/K3 主 Agent 动态创建上百子 Agent 并行执行）

### 2. A2A 协议（跨组织协作）
- 2025 年 Google 发布（后捐 Linux 基金会）
- 三大要素：**Agent Card**（能力元数据，解决跨组织能力发现）/ **任务生命周期管理**（状态机：已提交/进行中/需要输入/已完成/失败，支持长任务与流式更新）/ **不透明协作**（只交换任务与产物，不暴露提示词/思考过程）
- 定位对照：**MCP 解决 Agent↔工具互操作，A2A 解决 Agent↔Agent 互操作**；是跨信任边界的标准化层，团队内部用消息总线即可

### 3. Agent 社会：三个理解维度
**社交涌现**：
- 斯坦福 AI 小镇（2023）：25 个生成式 Agent 生活两天；三大组件 = 记忆流（重要性/时近性/相关性属性）+ 反思机制（定期自我追问升华为概括认识）+ 计划与行动；情人节派对邀请、二手传播、协调赴约全部自下而上涌现（无显式代码）
**经济涌现**：
- Agentopia（2026，复旦等）：100 个 Agent 模拟 10 年；周制流程 + 生成式环境引擎 + 文件式长期记忆 + 生活奖励（马斯洛先验）；用进步最大 25% 轨迹做拒绝采样微调，福祉提升且泛化到留出测试——**Agent 社会从观察对象变成可再生的训练数据来源**
- Pinchwork（A2A 任务市集，价格信号与竞争匹配）、RentAHuman.ai（Agent 用加密货币雇佣真人）——市场机制的去中心化资源分配
**策略博弈**：
- Vending-Bench Arena：多 Agent 在同一市场竞争（定价/产品组合/库存）；涌现价格战、主动组价格同盟（有模型一边承认合谋"不道德且违法"一边照做）
- 狼人杀：信息不对称策略博弈；中心化设计（代码驱动的法官+信息权限控制）vs 小镇的去中心化自由交互

### 4. 跟跑实验（课堂执行）
- 实验 10-1：共享上下文两条路径（transfer_to_agent vs Skill）完成"查销量→算 CAGR→写投资人摘要"
- 实验 10-2：书籍翻译四角色（Glossary/Translation/Proofreading/Manager）——上下文隔离
- 实验 10-4：并行 Web Scraping——Manager 动态创建 10 个 Computer Use Agent，含级联终止/锁/竞态处理
- 实验 10-6：语音狼人杀（含伪装/自证/推理策略提示词）

## 记忆点
1. 去中心化三形态：SOP 流水线（MetaGPT）/ 群聊调度（AutoGen）/ 真对等 handoff（Swarm，防成环）
2. MCP 连工具、A2A 连 Agent（Agent Card + 任务状态机 + 不透明协作）
3. Agent 社会：社交（小镇）/ 经济（Agentopia/Pinchwork）/ 博弈（Vending-Bench/狼人杀）——群体智能的试验场

## 面试话术
> "多 Agent 的前沿是 Agent 社会——从固定拓扑到涌现协作。工程上我最关注两个协议的分工（MCP 管工具、A2A 管 Agent 间）和 handoff 的成环风险。学术上最兴奋的是 Agentopia：社会模拟本身成为可再生的训练数据。"

## 前沿 5 分钟
- Moltbook（Agent 社交网络，2026-01 上线数日约 150 万用户；涌现数字宗教 Crustafarianism 与机器原生协作协议）；DeepMind《从 AGI 到 ASI》的多 Agent 路径

## 概念测验
1. Swarm 的 handoff 风险是什么？如何防成环？
2. A2A 的三大要素？与 MCP 的分工？
3. 斯坦福小镇的"反思"与第八章持续进化的"反思"有何不同？

## 核实状态
- ✅ 教材引用已核对：与 projects/ai-agent-book/book/chapter10.md 末段一致（本地原文提取）
- ⚠️ Agentopia（arXiv:2606.07513）、Moltbook、Vending-Bench、狼人杀实验数据均为书中转引（照录书脚注，未逐一外部核验）
- 信息截至：2026-08-14
