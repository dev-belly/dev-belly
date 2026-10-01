# Portfolio review · 2026-10-01

9 月 30 日复查了六个原主项目的展示入口、方法说明、保存的结果文件与 `main` CI；10 月 1 日增加了 PITBridge 和 StressAtlas 的源码复查、全量测试、报告回放和在线发布。项目定位应由可以运行和核验的内容支撑；合成数据上的分数仅用于展示实验流程。

## Lead with the role

| 目标方向 | 主讲项目 | 最值得展示的证据 | 需要讲清的边界 |
| :--- | :--- | :--- | :--- |
| 金融数据工程 | [PITBridge](https://github.com/dev-belly/PITBridge) | SQL 时点关联、独立枚举、修订/删除/新鲜度、逐记录溯源；可检查的未来信息反例。 | 标量特征和可信源时间合同；还没有生产采集、滚动聚合与模型系统集成。 |
| 组合风控 / 压力测试 | [StressAtlas](https://github.com/dev-belly/StressAtlas) | 借款人共享违约、全局/行业因子、配对情景差异、离散尾部 ES 和可加总贡献。 | 合成 PD/LGD/EAD；固定期限和情景参数；公开 CSV 是 200 条检查样本，全路径通过输入与种子重放。 |
| 银行数据 / 信贷风控 | [CreditVintage](https://github.com/dev-belly/CreditVintage) | 申请时点特征、180 天标签成熟、分离校准、跨期测试；提前监控与独立报告核验。 | 合成借款人；损失场景中的 LGD 是假设值；标签并非完整监管违约定义。 |
| 量化数据 / 研究工程 | [AlphaForge](https://github.com/dev-belly/alphaforge) | 从因子到组合、交易成本及报告的完整流程；信号与成交时点分离。 | 范围较大，面试优先深讲一个完整数据路径；公开样例未证明可交易优势。 |
| 金融技术 / 执行工程 | [TradeForge](https://github.com/dev-belly/TradeForge) | C++20 核心与 Python 逐事件对照，因果检查及执行成本比较。 | L2 队列近似、成交模型和合成市场会影响结论。 |
| 财务数据分析 | [AuditLens](https://github.com/dev-belly/AuditLens) | 30,128 笔凭证、九项程序、SQL 仓库、可解释评分和 300 笔复核底稿。 | 注入异常与规则口径关联，合成命中率不能作为真实舞弊识别率。 |
| IT 控制 / 证据工程 | [ControlTrace](https://github.com/dev-belly/ControlTrace) | HR、权限、工单、代码与部署关联；追加复核历史、底稿校验与规则重放。 | 记录关联不能证明源系统抽取完整，规则命中仍需要人工判断。 |
| 账务 / 数据一致性 | [LedgerX](https://github.com/dev-belly/LedgerX) | Decimal 双重记账、确定性重放与独立报价估值。 | 当前是单币种、仅做多的研究账本；尚未完成与真实券商账单的对账。 |

## What changed in this review

- 主页采用统一的深色横幅和六张项目卡片；每张卡片直接连接源码、演示或可检查的成果。
- 银行与风控方向优先展示 CreditVintage；AlphaForge 和 TradeForge 体现研究工程与底层实现能力。
- 在线报告集中放在一个入口；探索性研究和早期应用收进折叠区，便于读者迅速找到主线。
- [PROJECT_BRIEFS.md](PROJECT_BRIEFS.md) 保留有来源的简历表述和面试问题。

## Verified main-branch CI

以下链接固定到实际运行记录。六个原项目保留 9 月 30 日的核对快照；两个新项目列出 10 月 1 日发布后的运行。后续状态应查看各仓库 Actions 页面。

| Project | Main commit | CI evidence |
| :--- | :--- | :--- |
| PITBridge | `bc3b747` | [Successful CI](https://github.com/dev-belly/PITBridge/actions/runs/36827044068) |
| StressAtlas | `b158dfc` | [Successful CI](https://github.com/dev-belly/StressAtlas/actions/runs/36827087042) |
| CreditVintage | `55f79fe` | [Successful CI](https://github.com/dev-belly/CreditVintage/actions/runs/36735178230) |
| AlphaForge | `a1d3b03` | [Successful CI](https://github.com/dev-belly/alphaforge/actions/runs/36516317652) |
| TradeForge | `c692717` | [Successful CI](https://github.com/dev-belly/TradeForge/actions/runs/36516132505) |
| AuditLens | `1a483b7` | [Successful CI](https://github.com/dev-belly/AuditLens/actions/runs/36733072243) |
| ControlTrace | `f7cc605` | [Successful CI](https://github.com/dev-belly/ControlTrace/actions/runs/36511726878) |
| LedgerX | `ba94961` | [Successful CI](https://github.com/dev-belly/LedgerX/actions/runs/36420275411) |

## Newly filled gaps and the next step

PITBridge 补上了金融数据可得性、修订与源记录溯源；StressAtlas 补上了借款人级组合风险、相关性敏感度和尾部归因。两个仓库均已合并核心实现，并加上公式形态文本的 CSV 导出保护和在线报告；PITBridge 44 项、StressAtlas 48 项测试通过，保存的演示结果均可回放。

两者与 CreditVintage 形成可以解释的数据、模型与组合风险主线，目前仍是独立组件。下一步增加真实公开数据或系统集成时，需要保留许可、发布时间、标签定义和复现配置；不能把合成实验包装成真实银行落地业绩。
