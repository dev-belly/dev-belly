# Portfolio review · 2026-10-06

9 月 30 日复查了六个原主项目的展示入口、方法说明、保存的结果文件与 `main` CI；10 月 1 日发布 PITBridge 和 StressAtlas，10 月 2 日新增时点滚动特征、组合尾部风险精度诊断及 PITBridge 到 CreditVintage 的源记录溯源案例。10 月 3 日合并三项数值边界修复和 ControlTrace 底稿 JSON 校验修复；10 月 4 日合并 CreditVintage 报告核验、AlphaForge 成交配置、TradeForge 精确数值转换和 AuditLens 复核快照修复。10 月 6 日补齐后两项的主页证据，并将联合案例依赖更新至已修复的 PITBridge 提交。项目定位由可以运行和核验的内容支撑；合成数据上的分数仅用于展示实验流程。

## Lead with the role

| 目标方向 | 主讲项目 | 最值得展示的证据 | 需要讲清的边界 |
| :--- | :--- | :--- | :--- |
| 金融数据工程 | [PITBridge](https://github.com/dev-belly/PITBridge) | SQL 时点关联、独立枚举、修订/删除/新鲜度、滚动 sum/mean/count 和逐成员溯源；标量信贷特征实际接入 CreditVintage。 | 依赖可信源时间和逻辑事件身份；成员数量不等于经营数据完整；集成约定为 UTC 日终，没有生产采集。 |
| 组合风控 / 压力测试 | [StressAtlas](https://github.com/dev-belly/StressAtlas) | 借款人共享违约、离散尾部 ES、可加总贡献和完整路径配对 bootstrap 的 VaR/ES 精度。 | 合成 PD/LGD/EAD；区间仅诊断固定模型下的抽样误差，不能覆盖参数校准误差或未出现的稀有损失。 |
| 银行数据 / 信贷风控 | [CreditVintage](https://github.com/dev-belly/CreditVintage) | 申请时点特征、180 天标签成熟、分离校准、跨期测试；从 PIT 源记录重建特征并重拟合模型，保留逐笔预测溯源。 | 合成借款人；联合案例与原评估样本不同；损失场景中的 LGD 是假设值；标签并非完整监管违约定义。 |
| 量化数据 / 研究工程 | [AlphaForge](https://github.com/dev-belly/alphaforge) | 从因子到组合、交易成本及报告的完整流程；信号与成交时点分离。 | 范围较大，面试优先深讲一个完整数据路径；公开样例未证明可交易优势。 |
| 金融技术 / 执行工程 | [TradeForge](https://github.com/dev-belly/TradeForge) | C++20 核心与 Python 逐事件对照，因果检查及执行成本比较。 | L2 队列近似、成交模型和合成市场会影响结论。 |
| 财务数据分析 | [AuditLens](https://github.com/dev-belly/AuditLens) | 30,128 笔凭证、九项程序、SQL 仓库、可解释评分和 300 笔复核底稿。 | 注入异常与规则口径关联，合成命中率不能作为真实舞弊识别率。 |
| IT 控制 / 证据工程 | [ControlTrace](https://github.com/dev-belly/ControlTrace) | HR、权限、工单、代码与部署关联；追加复核历史、底稿校验与规则重放。 | 记录关联不能证明源系统抽取完整，规则命中仍需要人工判断。 |
| 账务 / 数据一致性 | [LedgerX](https://github.com/dev-belly/LedgerX) | Decimal 双重记账、确定性重放与独立报价估值。 | 当前是单币种、仅做多的研究账本；尚未完成与真实券商账单的对账。 |

## What changed in this review

- 主页采用独立的 `db` 标记、黑白与荧光绿视觉，以及三张全宽重点项目面板；其他项目集中在表格中，每项直接连接源码、演示或可检查的成果。
- 银行与风控方向优先展示 CreditVintage；AlphaForge 和 TradeForge 体现研究工程与底层实现能力。
- 三个重点项目分别链接在线报告；真实更新以带日期的工作记录呈现，探索性研究和早期应用收进折叠区。
- [PROJECT_BRIEFS.md](PROJECT_BRIEFS.md) 保留有来源的简历表述和面试问题。
- 10 月 2 日复查确认八个主项目的最近 `main` CI 均成功；整理此前冲突的主页 PR，补齐 SVG 可重建性、项目卡片对应关系、本地文件和章节入口的自动检查。在线网站的可用性需要另外检查，离线 CI 不宣称覆盖外部链接。
- 新增 [PITBridge 滚动报告](https://dev-belly.github.io/PITBridge/rolling/)：4 个合成决策、12 条特征结果、28 条源成员关联；30 天净流入从 1,500 变为 4,300 的案例解释修订的可得时点。
- 新增 [StressAtlas 精度报告](https://dev-belly.github.io/StressAtlas/precision/)：20,000 条路径、300 次配对重采样、30 条区间结果及 1,500 条情景重采样记录；区分 99% 风险水平和 95% 近似区间置信水平。
- 新增 [CreditVintage × PITBridge 联合案例](https://dev-belly.github.io/CreditVintage/lineage/)：默认生成 480 笔合成申请、1,440 个源特征、192 条决策后才可得记录及 120 笔测试预测；原始事件、模型输入、预测和交互页面都保留在生成目录的固定清单中，并支持完整重放。已补齐在线交互和完整 ZIP 下载；发布流程从源码生成合成案例，核验后上线，生成数据不提交进 Git 历史。
- 已发布 [PITBridge 数值契约修复](https://github.com/dev-belly/PITBridge/pull/3)：SQLite 与独立实现统一采用有限 binary64 输入；均值和最终有限的求和不再因中间溢出被误拒绝。原始整数仍留在输入证据中，浮点计算不替代精确账务。
- 已发布 [StressAtlas 尾部秩修复](https://github.com/dev-belly/StressAtlas/pull/3)与 [LedgerX Decimal 隔离及金额精度修复](https://github.com/dev-belly/LedgerX/pull/1)：外部程序改变 Decimal 精度、舍入、指数边界或异常设置，不应改变项目自身的尾部秩或账务重放；现金和费用会核对原始金额中的非零小数位。
- 已发布 [ControlTrace 底稿 JSON 修复](https://github.com/dev-belly/ControlTrace/pull/2)：类型错误的清单或源表行返回退出码 1；重复键和非有限数值在重放前被拒绝。13 项新增回归包含更新哈希后仍不合法的输入。
- 在 GitHub 实际主页核对了新版主图和旗舰项目卡片；主页的主分支检查已成功。页面可见性与仓库方法验证分开核对。

## Main commits and CI

本轮更新 CreditVintage 的依赖修复提交，以及 TradeForge、AuditLens 后续修复的成功主分支检查。AlphaForge 保留已完成的 Python 3.10–3.12 常规检查和完整流水线/API 集成记录；其余未变更项目保留先前核对的成功记录。链接固定到所列提交的运行，后续变化以各仓库 Actions 页面为准。

| Project | Main commit | CI evidence |
| :--- | :--- | :--- |
| PITBridge | `ed19dc6` | [Successful CI](https://github.com/dev-belly/PITBridge/actions/runs/37089437109) |
| StressAtlas | `b8fa33a` | [Successful CI](https://github.com/dev-belly/StressAtlas/actions/runs/37089449943) |
| CreditVintage | `50623a4` | [Main CI](https://github.com/dev-belly/CreditVintage/actions/runs/37400017422) |
| AlphaForge | `513abc6` | [Successful main CI](https://github.com/dev-belly/alphaforge/actions/runs/37167641845) |
| TradeForge | `2685c4b` | [Successful CI](https://github.com/dev-belly/TradeForge/actions/runs/37191280682) |
| AuditLens | `8333060` | [Successful CI](https://github.com/dev-belly/AuditLens/actions/runs/37191026460) |
| ControlTrace | `5c42038` | [Successful CI](https://github.com/dev-belly/ControlTrace/actions/runs/37089393347) |
| LedgerX | `b66c8c5` | [Successful CI](https://github.com/dev-belly/LedgerX/actions/runs/37089464841) |

## Recent validation

以下七项修复均已合并。10 月 6 日补齐 TradeForge 和 AuditLens 的回归案例与主分支记录；测试数量对应各 PR 的验证版本，合并后的检查链接列在上方。

| Project / PR | Reproduced problem and resulting behavior | Validation |
| :--- | :--- | :--- |
| [PITBridge #3](https://github.com/dev-belly/PITBridge/pull/3) | Python 可接受的大整数在 SQLite 绑定时报错；改为显式 binary64 数值契约，并支持中间求和溢出但最终均值或抵消结果有限的滚动计算。 | 75 tests；原快照与滚动报告逐字节重放一致。 |
| [StressAtlas #3](https://github.com/dev-belly/StressAtlas/pull/3) | 调用方的低精度 Decimal 环境会改变离散分位点和尾部质量；用整数比例确定尾部秩，隔离外部精度、指数范围及 traps。 | 70 tests；20,000 路径和 300 次 bootstrap 报告重放一致。 |
| [CreditVintage #4](https://github.com/dev-belly/CreditVintage/pull/4) | 更新哈希后的伪造置信区间或页面可能通过验证；独立重算 300 次整月重采样，按核验数据重建 HTML，并拒绝重复 JSON 键。 | 70 tests、5 subtests；评估、无标签监控、公开报告和完整源到预测链路全部核验；[Python 3.12/3.13 CI](https://github.com/dev-belly/CreditVintage/actions/runs/37089359255) 成功。 |
| [AlphaForge #2](https://github.com/dev-belly/alphaforge/pull/2) | 1.9 个成交延迟日被截为 1；字符串 `"false"` 开启零股；负成本增加净值。配置在成交前校验整数、布尔值和成本范围。 | 本地 1,267 tests 全部通过，含完整流水线与 API，覆盖率 96%；合并后的 Python 3.10–3.12 常规测试、lint、format、mypy、文档入口检查以及完整流水线/API 集成检查均成功，见 [主分支 CI](https://github.com/dev-belly/alphaforge/actions/runs/37167641845)。 |
| [LedgerX #1](https://github.com/dev-belly/LedgerX/pull/1) | 外部 Decimal traps 使部分卖出失败；极深小数位可能绕过记账量子约束。隔离算术环境，并把原始金额与可记账单位精确比较。 | 38 tests；格式、lint、mypy 通过，原估值案例保持一致。 |
| [TradeForge #2](https://github.com/dev-belly/TradeForge/pull/2) | Decimal 精度 2 让有效价格转换报错，并把 39.12 × 13 从 508.56 变成 510；默认精度也可能把略低于半 tick 的长小数推过边界。价格舍入改为精确整数比，tick 价格与逐笔成交名义金额由十进制系数构造。 | 48 项领域测试；完整本地套件 755 passed、150 项可选检查 skipped。main 的 Python 3.11–3.13、编译 C++ 单元/逐事件对照、ASan/UBSan 和重现性检查通过。 |
| [AuditLens #3](https://github.com/dev-belly/AuditLens/pull/3) | 哈希计算后再次打开 CSV，可能把更新后的异常复核数量与旧底稿的 SHA-256 绑定。清单、复核结果和摘要统一解析用于摘要哈希的同一份字节快照。 | 替换文件的并发回归验证摘要与其哈希版本一致；464 项本地 pytest 和含 15 条 SQL 查询的完整流程通过。main 的 Python 3.11/3.12 检查通过。 |

这些修复补充实现层面的核验，不改变合成数据结果的业务适用边界。各 PR 提供变更文件、回归案例和远端 CI 状态。

## Newly filled gaps and the next step

PITBridge 从标量快照扩展到决策时点的滚动经营统计，导出每条贡献记录并以独立枚举核验；StressAtlas 从尾部点估计扩展到配对抽样精度诊断，重放全部情景和重采样统计。数值边界修复后，PITBridge 75 项、StressAtlas 70 项测试通过；CI 同时核验原报告和新增报告，并从输入重新生成案例。

PITBridge 的标量特征现通过明确的身份、单位、七天新鲜度和 UTC 日终约定接入 CreditVintage。联合案例从源记录选择一直核对到模型重拟合后的每条测试预测；核验还拒绝更新哈希后的伪造特征、溯源、模型输入摘要、页面内容及不一致模型配置。CreditVintage 当前的 70 项测试包含 18 项集成回归和 12 项新增报告篡改回归，并有 5 项子测试通过；格式、lint 和类型检查也纳入 CI。

ControlTrace 的 59 项测试核对底稿重放、证据关联和非法 JSON 的命令行错误行为。LedgerX 的 38 项测试涵盖不利 Decimal 调用环境、完整账本重放、独立报价估值，以及工作精度之后仍存在非零金额小数位的拒绝行为；lint、格式与严格类型检查通过。

PITBridge 的滚动现金流与 StressAtlas 仍是单独的研究路径，联合案例没有声称把它们接进信贷模型或组合风险引擎。下一步引入真实公开数据时，需要保留许可、发布时间、标签定义和复现配置。

## Online evidence publication

[在线联合案例](https://dev-belly.github.io/CreditVintage/lineage/)可选择测试申请查看源记录；[完整 ZIP](https://dev-belly.github.io/CreditVintage/lineage/evidence.zip)包含源事件、模型输入、预测和清单。发布构建同时核验原评估、监控和完整联合案例；PR 只构建、主分支才部署。联合案例有 480 笔总申请、120 笔测试预测；原始风险报告的 480 笔测试申请属于另一份样例。

首次发布构建对应提交 `e9a259d`，见 [PR #5](https://github.com/dev-belly/CreditVintage/pull/5)。10 月 6 日合入 [依赖更新 PR #6](https://github.com/dev-belly/CreditVintage/pull/6)，将集成 CI、Pages 构建、安装说明和联合案例元数据统一固定到 PITBridge `ed19dc6`，保留原有 fraction/count 范围。70 项测试和 5 项子测试、完整源到模型重放均通过；七份输入、预测与指标 CSV 和此前发布样例逐字节一致，依赖元数据及其哈希随版本更新。新 [发布构建与部署](https://github.com/dev-belly/CreditVintage/actions/runs/37400017383)对应 `50623a4`。
