# Portfolio review · 2026-10-01

此前六个主项目的复查记录保留如下。本次补齐 PITBridge 与 StressAtlas 的实现、保存结果、双语文档和反例测试，并将八个项目按银行数据与风控主线展示。新项目 CI 状态以发布后的 Actions 运行记录为准。项目定位应由可以运行和核验的内容支撑；合成数据上的分数仅用于展示实验流程。

## Lead with the role

| 目标方向 | 主讲项目 | 最值得展示的证据 | 需要讲清的边界 |
| :--- | :--- | :--- | :--- |
| 银行数据 / 信贷风控 | [CreditVintage](https://github.com/dev-belly/CreditVintage) | 申请时点特征、180 天标签成熟、分离校准、跨期测试；提前监控与独立报告核验。 | 合成借款人；损失场景中的 LGD 是假设值；标签并非完整监管违约定义。 |
| 量化数据 / 研究工程 | [AlphaForge](https://github.com/dev-belly/alphaforge) | 从因子到组合、交易成本及报告的完整流程；信号与成交时点分离。 | 范围较大，面试优先深讲一个完整数据路径；公开样例未证明可交易优势。 |
| 金融技术 / 执行工程 | [TradeForge](https://github.com/dev-belly/TradeForge) | C++20 核心与 Python 逐事件对照，因果检查及执行成本比较。 | L2 队列近似、成交模型和合成市场会影响结论。 |
| 财务数据分析 | [AuditLens](https://github.com/dev-belly/AuditLens) | 30,128 笔凭证、九项程序、SQL 仓库、可解释评分和 300 笔复核底稿。 | 注入异常与规则口径关联，合成命中率不能作为真实舞弊识别率。 |
| IT 控制 / 证据工程 | [ControlTrace](https://github.com/dev-belly/ControlTrace) | HR、权限、工单、代码与部署关联；追加复核历史、底稿校验与规则重放。 | 记录关联不能证明源系统抽取完整，规则命中仍需要人工判断。 |
| 账务 / 数据一致性 | [LedgerX](https://github.com/dev-belly/LedgerX) | Decimal 双重记账、确定性重放与独立报价估值。 | 当前是单币种、仅做多的研究账本；尚未完成与真实券商账单的对账。 |

## What changed in this review

- 主页采用统一的深色横幅和八张项目卡片；每张卡片直接连接源码、演示或可检查的成果。
- 银行与风控方向优先展示 CreditVintage；AlphaForge 和 TradeForge 体现研究工程与底层实现能力。
- 在线报告集中放在一个入口；探索性研究和早期应用收进折叠区，便于读者迅速找到主线。
- [PROJECT_BRIEFS.md](PROJECT_BRIEFS.md) 保留有来源的简历表述和面试问题。

## Verified main-branch CI

以下链接固定到本次核对的实际运行记录。后续状态应查看各仓库 Actions 页面。

| Project | Main commit | CI evidence |
| :--- | :--- | :--- |
| CreditVintage | `55f79fe` | [Successful CI](https://github.com/dev-belly/CreditVintage/actions/runs/36735178230) |
| AlphaForge | `a1d3b03` | [Successful CI](https://github.com/dev-belly/alphaforge/actions/runs/36516317652) |
| TradeForge | `c692717` | [Successful CI](https://github.com/dev-belly/TradeForge/actions/runs/36516132505) |
| AuditLens | `1a483b7` | [Successful CI](https://github.com/dev-belly/AuditLens/actions/runs/36733072243) |
| ControlTrace | `f7cc605` | [Successful CI](https://github.com/dev-belly/ControlTrace/actions/runs/36511726878) |
| LedgerX | `ba94961` | [Successful CI](https://github.com/dev-belly/LedgerX/actions/runs/36420275411) |

## New components completed on 2026-10-01

| Component | Implemented evidence | Boundary |
| :--- | :--- | :--- |
| [PITBridge](https://github.com/dev-belly/PITBridge) | 发生/公开/入库时点、已知修订、撤销、有效期；SQL 与独立 Python 对照；45 次查询的逐条证据。 | 合成标量数据；不宣称分布式吞吐量或已接入 CreditVintage。 |
| [StressAtlas](https://github.com/dev-belly/StressAtlas) | 160 笔贷款、80 个借款人、20,000 条公共随机路径；五个情景、离散 ES 和行业可加总贡献。 | 一周期高斯模型及假设压力；没有宏观校准或监管资本计算。 |

新项目在本地通过反例与合同测试、保存证据重放和可安装命令行检查。发布后的 CI 记录见各仓库 Actions 页面。

## Next evidence gap

现有作品较好地覆盖了模型评估、研究流程、财务异常、执行模拟与记账。PITBridge 与 StressAtlas 已补上两项可以深入解释的能力：

1. **金融数据工程：** 多来源数据在决策时点的可得性、迟到与修订记录、质量约束、SQL 特征计算、源记录级溯源。
2. **组合风控：** 明确的一年期 PD/LGD/EAD 假设、违约相关性、压力情景、尾部损失及可重算的分组贡献。

这些组件目前分别演示，不能宣称已有集成业务链条。下一步的证据缺口是可许可、可保存发布时间的公开真实数据。增加真实公开数据时，还需要同时保存许可、发布时间、标签定义和复现配置。

