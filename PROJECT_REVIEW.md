# Portfolio review · 2026-10-03

9 月 30 日复查了六个原主项目的展示入口、方法说明、保存的结果文件与 `main` CI；10 月 1 日发布 PITBridge 和 StressAtlas，10 月 2 日新增时点滚动特征、组合尾部风险精度诊断及 PITBridge 到 CreditVintage 的源记录溯源案例。10 月 3 日合并三项数值边界修复和 ControlTrace 底稿 JSON 校验修复，并核对八个重点项目的最新主分支检查。项目定位由可以运行和核验的内容支撑；合成数据上的分数仅用于展示实验流程。

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
- 新增 [CreditVintage × PITBridge 联合案例](https://github.com/dev-belly/CreditVintage#source-to-prediction-lineage)：默认本地生成 480 笔合成申请、1,440 个源特征、192 条决策后才可得记录及 120 笔测试预测；原始事件、模型输入、预测和交互页面都保留在生成目录的固定清单中，并支持完整重放。当前发布生成器和源码，逐笔联合案例数据包没有公开提交。
- 已发布 [PITBridge 数值契约修复](https://github.com/dev-belly/PITBridge/pull/3)：SQLite 与独立实现统一采用有限 binary64 输入；均值和最终有限的求和不再因中间溢出被误拒绝。原始整数仍留在输入证据中，浮点计算不替代精确账务。
- 已发布 [StressAtlas 尾部秩修复](https://github.com/dev-belly/StressAtlas/pull/3)与 [LedgerX Decimal 隔离及金额精度修复](https://github.com/dev-belly/LedgerX/pull/1)：外部程序改变 Decimal 精度、舍入、指数边界或异常设置，不应改变项目自身的尾部秩或账务重放；现金和费用会核对原始金额中的非零小数位。
- 已发布 [ControlTrace 底稿 JSON 修复](https://github.com/dev-belly/ControlTrace/pull/2)：类型错误的清单或源表行返回退出码 1；重复键和非有限数值在重放前被拒绝。13 项新增回归包含更新哈希后仍不合法的输入。
- 在 GitHub 实际主页核对了新版主图和旗舰项目卡片；主页的主分支检查已成功。页面可见性与仓库方法验证分开核对。

## Verified main-branch CI

以下是 2026-10-03 核对的主分支快照，链接固定到与所列提交对应的成功运行。未修改的项目保留其最新成功记录；后续状态应查看各仓库 Actions 页面。

| Project | Main commit | CI evidence |
| :--- | :--- | :--- |
| PITBridge | `ed19dc6` | [Successful CI](https://github.com/dev-belly/PITBridge/actions/runs/37089437109) |
| StressAtlas | `b8fa33a` | [Successful CI](https://github.com/dev-belly/StressAtlas/actions/runs/37089449943) |
| CreditVintage | `08ec4d4` | [Successful CI](https://github.com/dev-belly/CreditVintage/actions/runs/37030157090) |
| AlphaForge | `a1d3b03` | [Successful CI](https://github.com/dev-belly/alphaforge/actions/runs/36516317652) |
| TradeForge | `c692717` | [Successful CI](https://github.com/dev-belly/TradeForge/actions/runs/36516132505) |
| AuditLens | `1a483b7` | [Successful CI](https://github.com/dev-belly/AuditLens/actions/runs/36733072243) |
| ControlTrace | `5c42038` | [Successful CI](https://github.com/dev-belly/ControlTrace/actions/runs/37089393347) |
| LedgerX | `b66c8c5` | [Successful CI](https://github.com/dev-belly/LedgerX/actions/runs/37089464841) |

## Newly filled gaps and the next step

PITBridge 从标量快照扩展到决策时点的滚动经营统计，导出每条贡献记录并以独立枚举核验；StressAtlas 从尾部点估计扩展到配对抽样精度诊断，重放全部情景和重采样统计。数值边界修复后，PITBridge 75 项、StressAtlas 70 项测试通过；CI 同时核验原报告和新增报告，并从输入重新生成案例。

PITBridge 的标量特征现通过明确的身份、单位、七天新鲜度和 UTC 日终约定接入 CreditVintage。联合案例从源记录选择一直核对到模型重拟合后的每条测试预测；核验还拒绝更新哈希后的伪造特征、溯源、模型输入摘要、页面内容及不一致模型配置。CreditVintage 的 58 项测试包含 18 项集成回归，格式、lint 和类型检查也纳入 CI。

ControlTrace 的 59 项测试核对底稿重放、证据关联和非法 JSON 的命令行错误行为。LedgerX 的 38 项测试涵盖不利 Decimal 调用环境、完整账本重放、独立报价估值，以及工作精度之后仍存在非零金额小数位的拒绝行为；lint、格式与严格类型检查通过。

PITBridge 的滚动现金流与 StressAtlas 仍是单独的研究路径，联合案例没有声称把它们接进信贷模型或组合风险引擎。下一步引入真实公开数据时，需要保留许可、发布时间、标签定义和复现配置。
