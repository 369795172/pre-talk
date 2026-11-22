# AGENTS.md - pre-talk 工程治理

开源仓（public）：沟通前备谈 skill「想清楚」。方法论源自黄执中《表达学院》公开课的工程化，配合 Rokid AI Glasses「听懂对方」智能体使用。

## Scope

- 本仓交付物 = `skill/`（Agent Skills 格式的备谈工作流）+ 结构校验脚本 + 文档四件套；单一产品面：沟通前的准备工序。
- 目标用户：面对重要沟通（汇报/谈判/1on1/提需求/面试）的人，自带任意支持 Agent Skills 的 AI agent。
- 生态位：三层闭环的「想清楚」层（沟通前）；沟通中归助谈设备，沟通后归用户自己的复盘，均不在本仓范围。

## What NOT to do

- 不在 README/rfc/SKILL 里宣称任何未在设备端代码验证过的联动机制（2026-11-22 review 教训：曾写「口播开场白可锚定听懂对方」，实际该智能体为单轮会话制）。
- 不引入账号/云同步/多端状态。
- 不生成让人背诵的话术模板；工作流任何改版不得把「筛除法找核心句」换成「直接挑最重要的」。
- 不出现任何私有信息、内部路径、个人数据、其他私有仓名或链接；提及「听懂对方」只指向 Rokid Agent Store 发布面。
- 方法论致谢保持中性：非官方、无隶属关系。

## Structure Routing

| 文件 | 用途 |
|---|---|
| `README.md` | 人读入口：是什么 / 上手 / 安装 / 三层闭环 / 致谢 |
| `skill/SKILL.md` | 工作流本体（Agent Skills 格式，装进用户 agent 的交付物） |
| `skill/talk-card.template.md` | 备谈卡模板（卡片契约的可读形态） |
| `skill/examples/` | 示例卡（虚构场景，人物与公司不可对应真实实体） |
| `scripts/check_card.py` | 卡片结构校验：`./scripts/check_card.sh skill/examples/*.md` 退出码 0 |
| `docs/prd.md` | What & Why（范围与非目标 SSOT） |
| `docs/rfc.md` | How（架构与决策否案） |
| `docs/test.md` | 分层验证命令 |
| `docs/working.md` | Changelog + Lessons |

## 工作流契约（skill 迭代时不可破坏）

1. 四步固定顺序：登记 → 核心句（筛除法）→ 排序 → 对方三问 → 成卡。
2. 核心句只允许通过筛除逼进（可剔除 / 可合并 / 排序低），禁止让用户直接「挑最重要的」。
3. 排序必须有「第二重要」；引导语要带试金石（答不出第二重要，第一句是口号）。
4. 卡片字段以 `skill/talk-card.template.md` 为 SSOT；改字段必须同步 examples 与 check_card.py。
5. 产出话术判据：是人话。第一句即核心诉求，终态自带验收，无编号清单腔。

## Doc Update Discipline

- 每个 meaningful change 更新 `docs/working.md`（日期键倒序、特性级 bullet、Lessons 写成可迁移原则句）；先写 working.md 再 commit。
- 契约变化（工作流四步 / 卡片字段 / 判据）全量回写：SKILL.md + template + examples + check_card.py + rfc.md。

## Git

- commit 前缀标注来源工具（如 `[OpenCode]`）；main 直推。
- commit 前检查：`./scripts/check_card.sh` 通过；无私有信息混入。

## Validation

```bash
./scripts/check_card.sh          # 无参数：全部示例卡 + 模板结构校验
./scripts/check_card.sh skill/examples/向上汇报_功能延期通报.md   # 指定卡片（透传）
```
