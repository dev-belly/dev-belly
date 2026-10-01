# Project evidence and interview notes

These are **candidate resume bullets**, not claims about live customers or realized investment returns. Every quoted result is from a linked synthetic run. Choose two projects that fit the role and rehearse the assumptions and code path before using the wording in an interview.

## Bank credit / model validation

### [CreditVintage](https://github.com/dev-belly/CreditVintage)

> 实现申请时点可得特征和 180 天逾期标签成熟校验，以分离的训练、校准及跨期测试批次评估信贷风险基线；在 480 笔合成测试申请上得到 ROC-AUC 0.747、Brier 0.155，并保留独立校准后 Brier 变差的结果；早期监控路径仅用当期申请分数计算分布漂移，不偷用尚未成熟的逾期结果。

> 数据质量与验证侧表述：为信贷风险报告实现独立核验，基于逐笔预测重算模型指标、分组损失场景和分数漂移；校验标签成熟窗口、复核容量与 CSV 结构，以更新哈希后的异常报告验证核验流程能够拒绝不一致结果。

- **Evidence:** [test report](https://dev-belly.github.io/CreditVintage/demo/), [row-level predictions](https://github.com/dev-belly/CreditVintage/blob/main/docs/demo/predictions.csv), [early monitor](https://dev-belly.github.io/CreditVintage/monitor/), [report-contract regressions](https://github.com/dev-belly/CreditVintage/blob/main/tests/test_artifact_contract.py), [CI](https://github.com/dev-belly/CreditVintage/actions/workflows/ci.yml).
- **Discuss:** `observed_at` versus `available_at`; why missing six-report coverage is not a nondefault; why PSI cannot establish realized default or calibration drift; why isotonic calibration was retained as a negative result; why `NaN` breaks an ordinary tolerance comparison and a matching hash does not establish valid report content.
- **Boundary:** The 90+ DPD within 180 days is a research label. The synthetic AUC and probability × principal × assumed LGD scenario are not regulatory default or expected credit loss estimates.

### [Interval Financial Risk](https://github.com/dev-belly/interval-financial-risk)

> 将四季度点值扩展为分布与波动区间特征，对 300 家模拟公司、4,800 条季度记录进行扩展窗口测试及消融；同一 Logistic 算法加入区间特征后，三个测试折的平均 AUC 从 0.7243 降至 0.6857，保留负结果并公开逐笔预测和切分记录。

- **Evidence:** [interactive report](https://dev-belly.github.io/interval-financial-risk/), [fold splits](https://github.com/dev-belly/interval-financial-risk/blob/main/docs/demo/fold_splits.csv), [predictions](https://github.com/dev-belly/interval-financial-risk/blob/main/docs/demo/predictions.csv).
- **Discuss:** Why test-fold averages differ from a pooled ROC curve; why nominal 90% conformal coverage with a near-unit-width interval is not useful discrimination; why same-company quarters weaken independence.
- **Boundary:** Labels are synthetic contemporaneous outcomes, not real future defaults. Financial statement publication timing remains unvalidated.

## Financial data engineering / portfolio risk

### [PITBridge](https://github.com/dev-belly/PITBridge)

> 构建金融多源数据时点特征组件，使用 SQLite 窗口函数处理公开/入库延迟、历史修订、撤销及特征有效期，保留记录级溯源；用独立 Python 枚举及随机历史对照验证 SQL 输出，在 45 次合成特征查询中识别事件时间基线的 11 次未来信息使用，并实现报告哈希校验与语义重放。

- **Evidence:** [counterexamples](https://github.com/dev-belly/PITBridge/blob/main/demo/comparison.csv), [snapshot lineage](https://github.com/dev-belly/PITBridge/blob/main/demo/snapshots.csv), [temporal tests](https://github.com/dev-belly/PITBridge/blob/main/tests/test_temporal.py), [中文面试问答](https://github.com/dev-belly/PITBridge/blob/main/docs/INTERVIEW.md).
- **Discuss:** Event time versus knowledge time; highest known revision versus latest arrival; why filtering tombstones before ranking resurrects deleted observations; why 11 future-data selections and 16 changed selections are different counts.
- **Boundary:** Compact synthetic fixture, scalar observations and no distributed benchmark. It is a separate component from CreditVintage, with no integrated pipeline claimed.

### [StressAtlas](https://github.com/dev-belly/StressAtlas)

> 构建信用组合压力测试研究组件，基于全局/行业高斯因子及借款人共享违约事件，在 160 笔贷款、80 个借款人的合成组合上复用 20,000 条随机路径比较五个情景；输出解析期望损失、99% VaR/ES、配对均值差异标准误及可加总的行业尾部贡献，验证贷款拆分不变性、离散尾部并列值和报告语义重放。

- **Evidence:** [computed scenarios](https://github.com/dev-belly/StressAtlas/blob/main/demo/scenarios.csv), [sector contributions](https://github.com/dev-belly/StressAtlas/blob/main/demo/sector_es.csv), [case study](https://github.com/dev-belly/StressAtlas/blob/main/docs/CASE_STUDY.md), [中文面试问答](https://github.com/dev-belly/StressAtlas/blob/main/docs/INTERVIEW.md).
- **Discuss:** Why correlation can change the tail while analytic EL stays constant; why loans to one obligor share a default; common random numbers and paired mean SE; fixed empirical tail mass and equal boundary-tie weights.
- **Boundary:** One-period Gaussian-factor prototype and assumed PD/LGD/EAD shocks. No regulatory-capital implementation or empirical macro calibration. Mean MC SE is not a VaR/ES confidence interval.

## Audit / risk consulting

### [AuditLens](https://github.com/dev-belly/AuditLens)

> 构建合成凭证审计分析流程：对 30,128 笔凭证运行九项审计规则、Benford 检验与 Isolation Forest，输出可追溯的规则证据、SQLite 查询结果和 Streamlit 风险看板；按规则覆盖、风险排序与概率抽样生成 300 笔复核工作底稿，并验证人工复核结果与抽样来源。

- **Evidence:** [reports and the 300-row workpaper](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports), [methodology](https://github.com/dev-belly/AuditLens/blob/main/docs/methodology.md), [CI](https://github.com/dev-belly/AuditLens/actions/workflows/ci.yml).
- **Discuss:** Why the random inclusion probability applies only to the non-targeted frame; why an anomaly flag is not a confirmed fraud finding; how the workpaper checksum and input fingerprint differ.
- **Boundary:** The 919 injected anomalies and all detection metrics come from synthetic data. No client ledger or real fraud labels were used.

### [ControlTrace](https://github.com/dev-belly/ControlTrace)

> 构建系统访问与生产变更的合成审计平台：以稳定 ID 连接 HR、账号、授权、审批、代码提交和部署记录，执行五项内控测试；逐条保留规则口径、时间线和来源证据，支持追加式人工复核，并导出可校验与重放的工作底稿。

- **Evidence:** [control catalog](https://github.com/dev-belly/ControlTrace/blob/main/docs/CONTROL_CATALOG.md), [worked review case](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md), [CI](https://github.com/dev-belly/ControlTrace/actions/workflows/ci.yml).
- **Discuss:** Why a missing join is a data gap rather than proof of control failure; why approval must follow request and precede grant or deployment; why the workpaper hash checks internal consistency but does not prove external source authenticity.
- **Boundary:** The twelve seeded observations are synthetic test cases, not a measured detection rate. Full extract completeness and real access effectiveness need separate procedures.

## Quant research / execution engineering

### [TradeForge](https://github.com/dev-belly/TradeForge)

> 构建 C++20 订单簿与 Python 研究层，对四种执行策略在同一合成事件流下进行可复现对比；同时报告到达价与区间 VWAP 的交易成本，并用 Python/C++ 逐事件对照、因果测试和 CI sanitizers 检查结果可靠性。

- **Evidence:** [deterministic cost table](https://github.com/dev-belly/TradeForge#sixty-second-tour), [verification contract](https://github.com/dev-belly/TradeForge#what-makes-the-numbers-defensible), [CI](https://github.com/dev-belly/TradeForge/actions/workflows/ci.yml).
- **Discuss:** Why one execution can beat arrival price but lose to interval VWAP; exact L3 FIFO versus approximate L2 queue; why a synthetic cost difference is not a venue performance claim.

### [AlphaForge](https://github.com/dev-belly/alphaforge) and [LedgerX](https://github.com/dev-belly/LedgerX)

> 在 AlphaForge 因子研究平台中将信号日与成交日分离，以逐信号执行队列处理重叠调仓和样本边界；另在 LedgerX 中实现独立的 Decimal 双重记账日志，以时点可得的外部报价核对已实现与未实现损益。两个仓库目前是分别演示的研究组件。

- **Evidence:** [AlphaForge backtest mechanics](https://github.com/dev-belly/alphaforge/blob/main/docs/modules/backtesting.md), [synthetic backtest record](https://dev-belly.github.io/alphaforge/sample-run/), [LedgerX valuation example](https://github.com/dev-belly/LedgerX/blob/main/examples/valuation.json), their CI runs.
- **Discuss:** Why a signal formed at today's close cannot fill on that same close; historical cost versus external mark; what a hash chain can detect only when its head is checked against an independent checkpoint.
- **Boundary:** AlphaForge's sample and LedgerX's fills/quotes are synthetic. Neither is evidence of a live trading edge or actual brokerage reconciliation.

## Choosing what goes on a resume

- **Financial audit analytics:** AuditLens first; ControlTrace or CreditVintage second.
- **IT audit / technology risk:** ControlTrace first; AuditLens second.
- **Bank data / risk analytics:** CreditVintage first; PITBridge or StressAtlas second, according to whether the role emphasizes data pipelines or portfolio risk.
- **Financial data engineering:** PITBridge first; CreditVintage second.
- **Portfolio risk analytics:** StressAtlas first; CreditVintage second.
- **Quant engineering:** TradeForge first; AlphaForge or LedgerX second.

The remaining repositories include exploratory research and application prototypes. Their READMEs describe the implemented scope and limitations; do not present every repository as an equal-depth flagship project.
