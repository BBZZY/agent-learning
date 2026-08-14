# 课 1-8：RL 进阶与 Agent 衔接（offline RL → GRPO/RLVR → agentic RL）

> 模块 1：DL 理论底座（收尾）｜ 教材：UDL ch.19.4-19.7 + ai-agent-book ch7（预告）
> 状态：✅ 讲义已生成（2026-08-14）；前沿概念经 2026-08 检索核实

## 教学目标
1. 理解 offline RL 为什么是 LLM 对齐的底层范式
2. 会用一句话解释 GRPO / RLVR（面试高频）
3. 建立"模块 1 → 模块 5（模型后训练）"的衔接地图

## 知识点详解

### 1. offline RL：从交互到数据集（UDL 19.7）
- 在线 RL：边玩边学（需要环境反复交互，昂贵）
- 离线 RL：只从历史记录学（稳定、可复用）
- RLHF 正是 offline RL：人类偏好数据是"历史记录"，奖励模型给出奖励
- Agent 后训练同理：Agent 的运行轨迹（成功/失败）作为离线数据

### 2. GRPO：组内相对奖励（Group Relative Policy Optimization）
- 动机：PPO 需要价值网络（critic），昂贵；GRPO 去掉 critic
- 做法：同一问题采样一组回答，用组内平均当基线——相对好坏定梯度方向
- 关键事实：**DeepSeek-R1 的训练即用 GRPO**（公开技术报告），面试提 DeepSeek 必背
- 类比：班级排名制——不比绝对分数，比组内名次

### 3. RLVR：可验证奖励（RL with Verifiable Rewards）
- 动机：数学/代码题有客观对错 → 不需要人标，正确答案即奖励
- 与 GRPO 常组合：GRPO-RLVR 是 2026 推理模型后训练标配
- 类比：有标准答案的作业可以自动批改

### 4. agentic RL：Agent 的后训练（衔接模块 5）
- 环境 = 真实任务（查资料/用工具/写代码），奖励 = 任务成功/过程质量
- 训练数据 = Agent 运行轨迹（trajectory）
- 这正是 DeepSeek 后训练岗 JD 的"Agent 场景评测与数据管线"、ai-agent-book ch7 全文主题
- 面试金句：预训练给知识、SFT 给指令、RL 给偏好，**agentic RL 给行动能力**

### 5. 衔接地图
```
模块1（本课终点）: 知道"模型怎么被训练"
        ↓
模块2-4: 知道"Agent 怎么被组装"（上下文/工具/多Agent）
        ↓
模块5 ch7: 闭环——知道"Agent 怎么被训练得更好"（模块5 详讲）
```

## 记忆点
1. offline RL = 从固定数据学习 → RLHF/agentic RL 的底层范式
2. GRPO：组内相对奖励、无 critic（DeepSeek-R1 所用）
3. RLVR：可验证答案当奖励；与 GRPO 组合是 2026 标配

## 面试话术
> "DeepSeek-R1 用 GRPO 在可验证奖励上做后训练，本质是 offline RL 的语言模型版。Agent 时代把这个范式搬到工具使用轨迹上——这就是 agentic RL。"

## 前沿 5 分钟
- 2026 研究热点：Agent 轨迹信用分配（多步任务中哪步该得奖励）、过程奖励模型（PRM vs ORM）——模块 5 ch7 展开

## 概念测验
1. GRPO 为什么不需要 critic？用组内平均代替了什么？
2. RLVR 能用在哪些任务？（提示：答案可验证）
3. "agentic RL 的训练数据"是什么？

## 核实状态
- ✅ UDL ch.19.4-19.7 章节号核实（MIT Press 目录）
- ✅ GRPO 为 DeepSeek-R1 训练方法（DeepSeek R1 技术报告公开信息）；GRPO/RLVR/PPO/RLHF 为 DeepSeek 后训练岗 JD 明确列出的范式（2026-08-12 招聘页检索核实）
- 信息截至：2026-08-14
