# 开源项目对照与演进路线

数据质量方向官方资料核查日期：**2026-10-25**；Qlib、scorecardpy 和 Feast
沿用 2026-10-24 的核查。本页比较相近方向的公开能力与当前可检查证据。
本轮关注能落实的功能和使用路径，不用 Star 比值换算技术差距，
也不把自己的测试运行当作外部采用。

## 对照哪些项目

| 参考项目 | 可借鉴的具体能力 | 本项目组合的对应入口 | 仍有的差距 |
| --- | --- | --- | --- |
| [Evidently](https://docs.evidentlyai.com/metrics/preset_data_summary) · [Tests](https://docs.evidentlyai.com/docs/library/tests) | 按列汇总数据质量和分布，可配置测试与参考条件 | CreditVintage 保留输入分布/时点覆盖诊断，v0.7.0 增加三特征整体/月度覆盖与最小样本规则 | 仍是固定事件模式，没有通用指标/阈值组合或监控服务；描述性距离不等于显著性判断 |
| [Great Expectations](https://docs.greatexpectations.io/docs/reference/learn/data_quality_use_cases/missingness/) | 列非空、非空比例和可容忍缺失范围等 Expectations | 保留完整申请分母及逐特征台账，区分晚到、决策后观测及截止日不可见记录 | 事件槽位缺失不同于 CSV 空值；已有显式覆盖检查，仍没有任意列 Expectations、Checkpoint/Action 体系或完整质量规则 |
| [TensorFlow Data Validation](https://www.tensorflow.org/tfx/data_validation/get_started) · [validate_statistics](https://www.tensorflow.org/tfx/data_validation/api_docs/python/tfdv/validate_statistics) | 模式、特征存在率和异常检查；结合前期/服务统计检查 drift 与 skew | 按整体和月份保留特征覆盖计数，空人群率为 null；从源事件重建时间口径和报告 | 没有模式推断、TFX 流水线或通用 drift/skew 验证器；三项固定特征诊断不能替代这些能力 |
| [Qlib](https://qlib.readthedocs.io/en/stable/component/workflow.html) | 配置化研究工作流、训练/评价产物与实验管理 | AlphaForge 真实价格对照，CreditVintage 五组切分与完整逐笔模型结果 | 历史成分与财务可得时间不完整；缺少同范围的大规模实验管理 |
| [scorecardpy](https://github.com/ShichenXie/scorecardpy) | 分箱、WOE、评分卡缩放与性能评价的可调用组件 | CreditVintage 的 WOE 对照、同复核容量比较和独立 UCI 实验 | 仍是固定特征和客群的研究案例，不能作为通用评分卡工具使用 |
| [Feast](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) | 历史特征、TTL、存储与服务接入；可选创建时间过滤 | PITBridge 的多时间字段、修订/删除规则与独立回放，支持原生 CSV | 缺少在线服务、多存储适配、部署和真实复用证据；不能声称其他工具不支持知识时间 |

这些工具解决的问题与维护范围不同。本轮没有运行同数据、同协议的跨框架
性能比较，也没有把功能表当作性能排名。代码和数值正确性可以自动核查，
业务适配、真实跨期表现和独立使用仍需单独证据。

## 当前最需要补什么

| 维度 | 已有证据 | 仍缺少的证据 | 可以验收的下一步 |
| --- | --- | --- | --- |
| 真实数据有效性 | AlphaForge 历史价格对照、TradeForge 短段公开盘口；CreditVintage 已有 1,000 行德国信贷及 30,000 行信用卡观察的固定对照 | 真实信贷中的决策时点、特征可用时间、成熟标签及时间外表现；更长且跨情景的行情 | 数据来源与时间口径可核查；固定基线、时间外划分和失败结果一起保留 |
| 独立复用 | PITBridge v0.2.0 CSV 接入、CreditVintage v0.7.0 两表诊断、显式覆盖规则与分布检查、干净环境 wheel 重放、逐行诊断和首次运行入口 | 独立使用者用自己的数据完成任务，以及由此暴露的适配问题 | 一名外部读者完成一次有记录的试用，保留输入契约、命令和预期/实际结果 |
| 功能深度 | 时间边界、SQL 对照、来源追溯、人工复核重试等路径已有实现和回归 | 广泛数据模式、生产数据规模及业务系统集成；TradeForge 尚不能代替成熟排队/延迟框架 | 围绕一个真实任务补适配与对照，先明确输入和输出，再扩展支持范围 |
| 社区证据 | PITBridge #8 有 GreedyC 账号贡献；#7 有 ylc22 的校验建议，#24 落实后续边界修复 | 账号关系、独立试用与生产采用仍未由这些记录证明 | 继续保存可复现反馈、实际修复和试用结果，分别解释贡献、使用与部署 |
| 展示聚焦 | 主页保留三个主推项目，其他项目和详细历史折叠；新增首次运行路线 | 用户能否迅速理解“选哪个、解决什么问题、如何开始”的实际反馈 | 让首次读者只选一个任务并完成一次运行；据反馈精简入口 |

CI、测试数量和摘要核验帮助定位工程错误；真实数据验证、业务有效性和
独立采用仍需各自的证据。现有合成测试有助于制造迟到、修订、缺失等边界
条件，应继续保留其用途，同时补充真实数据实验。

## 本轮已经补上的内容

- **2026-10-25 · [CreditVintage #34](https://github.com/dev-belly/CreditVintage/pull/34)：**
  在已核验诊断上增加明确的人群、月份、特征、最低覆盖和最小样本规则。
  精确计数避免舍入误判；失败/不足保留为结果，核验与策略通过分别解释。
  外部策略摘要能拒绝规则替换；它不认证事件真假，也不放宽评分缺失检查。
  376 项测试及 28 个子测试通过，隔离安装覆盖通过/失败/不足三条路径。
  [失败示例](https://dev-belly.github.io/CreditVintage/feature-check/) ·
  [首次运行](START_HERE.md#creditvintage-check-explicit-coverage-conditions) ·
  [范围与契约](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_POLICY.md)。
  参考 [Evidently Tests](https://docs.evidentlyai.com/docs/library/tests) 和
  [GX Checkpoints](https://docs.greatexpectations.io/docs/core/trigger_actions_based_on_results/create_a_checkpoint_with_actions/)
  区分统计、条件与后续步骤；仍不是通用质量框架，未发送消息或运行跨框架性能基准。

- **2026-10-25 · [CreditVintage #33](https://github.com/dev-belly/CreditVintage/pull/33)：**
  不依赖结果文件和模型，诊断三项决策时特征的覆盖、可见迟到及逐月计数。
  合成案例保留 320 笔当前申请，316 笔完整、4 笔不完整，另排除 160 笔未来申请。
  337 项测试和 28 个子测试通过；旧版六个报告文件与单独安装的公开 v0.5.0
  逐字节一致。缺失特征仍阻止评分/分布检查，诊断核验成功不等于数据完整。
  [在线案例](https://dev-belly.github.io/CreditVintage/feature-quality/) ·
  [首次运行](START_HERE.md#creditvintage-diagnose-missing-decision-time-features) ·
  [方法和范围](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_QUALITY.md)。

以下为 2026-10-24 完成记录：

- [CreditVintage #32](https://github.com/dev-belly/CreditVintage/pull/32)：
  只读申请和特征事件，比较五项决策时输入；保存可重建的快照、累计计数和页面。
  手算与 SciPy 独立实现对照，310 项测试和 28 个子测试通过；隔离安装后在没有
  结果文件的情况下运行，且拒绝修改结果后重新计算哈希的报告。
- [PITBridge #24](https://github.com/dev-belly/PITBridge/pull/24)：
  收紧可选 pandas 示例的数值文本校验，修复超长前导零版本号；137 项本地测试
  和十项 PR CI 检查通过。原生安装包的已有严格输入规则继续保留。
- [首次运行](START_HERE.md#creditvintage-inspect-input-distributions-without-labels)
  接到 v0.5.0 受检安装包、新报告及源码；可以直接解释输入变化和分数变化的区别。

## 此前完成的基础

1. 合并主页 [#29](https://github.com/dev-belly/dev-belly/pull/29)：固定源码快照，
   提供从空目录安装、生成报告和核验的入口。
2. 合并 PITBridge [#15](https://github.com/dev-belly/PITBridge/pull/15)：说明旧
   release 与 main 的功能差异；三决策示例另行断言固定业务结果。
3. 合并 CreditVintage [#16](https://github.com/dev-belly/CreditVintage/pull/16)，接通包内公开数据实验与自定义时间窗口；在其同一份数据、加载器和 17 个建模属性上增加 [五次公开信贷比较](https://github.com/dev-belly/CreditVintage/blob/main/docs/PUBLIC_CREDIT_COMPARISON.md)：
   复用已冻结并署名的 UCI 源数据；三种固定模型共享五组分层划分；保存全部预测、
   分组结果、参数、环境和划分归属；自动复核输出。

4. [CreditVintage #18](https://github.com/dev-belly/CreditVintage/pull/18) 将公开验证扩展到 30,000 条信用卡观察：五次固定训练/校准/测试划分、四种方法、12 万个模型分数及 60 组同预算结果；增加离线重拟合、完整证据 ZIP 和通过主分支 CI 后发布的固定版本包。原数据转换、安装包、版本/提交与文件摘要均可核查。

公开比较中，逻辑回归五次平均 AUC 约 0.767，梯度提升树约 0.771；树模型
在平均 AUC、AP 和 Brier 上略优；逻辑回归的 Top-20 精确率略高。报告保留全部结果，没有因此宣布普遍赢家。
UCI 数据没有时点信息，这一新增实验仍未完成真实信贷的时间外验证。

**2026-10-16：** [CreditVintage #20](https://github.com/dev-belly/CreditVintage/pull/20) 增加 `init-inputs` 和 `check-inputs`，把手工构造三份 CSV 的门槛变为可编辑的完整样例，并在训练前按文件和行号收集错误。检查真实记录类型、时点特征与成熟标签，后续被阻断的检查会明确标注；隔离安装会从生成文件跑到实际评估与错误行定位。这里新增的是复用能力，仍不计为外部采用。

## 接下来的工作顺序

优先沿 **CreditVintage × PITBridge** 做深一条链：真实输入 → 可用时间 →
评分与 SQL 分析 → 有限名额复核 → 可交付证据。每增加一个功能，先说明
哪类使用者在什么输入下需要它，以及怎样验证它解决了问题。

当前适合优先收集一次独立试用反馈，并寻找时间口径可靠的公开或合法脱敏
数据；复用反馈和真实时间外评估不能通过继续美化 README 来替代。
保留 [首次运行](START_HERE.md) 和 [业务讲解](INTERVIEW_PLAYBOOK.zh-CN.md)
两条入口，让使用、审阅和面试练习都能回到实际产物。
