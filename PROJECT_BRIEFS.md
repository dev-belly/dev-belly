# Project evidence and interview notes

These are **candidate resume bullets**, not claims about live customers or realized investment returns. Every quoted result is from a linked synthetic run. Choose two projects that fit the role and rehearse the assumptions and code path before using the wording in an interview.

## Audit / risk consulting

### [AuditLens](https://github.com/dev-belly/AuditLens)

> 构建合成凭证审计分析流程：对 30,128 笔凭证运行九项审计规则、Benford 检验与 Isolation Forest，输出可追溯的规则证据、SQLite 查询结果和 Streamlit 风险看板；按规则覆盖、风险排序与概率抽样生成 300 笔复核工作底稿，并验证人工复核结果与抽样来源。

- **Evidence:** [reports and the 300-row workpaper](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports), [methodology](https://github.com/dev-belly/AuditLens/blob/main/docs/methodology.md), [CI](https://github.com/dev-belly/AuditLens/actions/workflows/ci.yml).
- **Discuss:** Why the random inclusion probability applies only to the non-targeted frame; why an anomaly flag is not a confirmed fraud finding; how the workpaper checksum and input fingerprint differ.
- **Boundary:** The 919 injected anomalies and all detection metrics come from synthetic data. No client ledger or real fraud labels were used.

## Bank credit / model validation

### [CreditVintage](https://github.com/dev-belly/CreditVintage)

> 实现申请时点可得特征和 180 天逾期标签成熟校验，以分离的训练、校准及跨期测试批次评估信贷风险基线；在 480 笔合成测试申请上得到 ROC-AUC 0.747、Brier 0.155，并保留独立校准后 Brier 变差的结果；早期监控路径仅用当期申请分数计算分布漂移，不偷用尚未成熟的逾期结果。

- **Evidence:** [test report](https://dev-belly.github.io/CreditVintage/demo/), [row-level predictions](https://github.com/dev-belly/CreditVintage/blob/main/docs/demo/predictions.csv), [early monitor](https://dev-belly.github.io/CreditVintage/monitor/), [CI](https://github.com/dev-belly/CreditVintage/actions/workflows/ci.yml).
- **Discuss:** `observed_at` versus `available_at`; why missing six-report coverage is not a nondefault; why PSI cannot establish realized default or calibration drift; why isotonic calibration was retained as a negative result.
- **Boundary:** The 90+ DPD within 180 days is a research label. The synthetic AUC and probability × principal × assumed LGD scenario are not regulatory default or expected credit loss estimates.

### [Interval Financial Risk](https://github.com/dev-belly/interval-financial-risk)

> 将四季度点值扩展为分布与波动区间特征，对 300 家模拟公司、4,800 条季度记录进行扩展窗口测试及消融；同一 Logistic 算法加入区间特征后，三个测试折的平均 AUC 从 0.7243 降至 0.6857，保留负结果并公开逐笔预测和切分记录。

- **Evidence:** [interactive report](https://dev-belly.github.io/interval-financial-risk/), [fold splits](https://github.com/dev-belly/interval-financial-risk/blob/main/docs/demo/fold_splits.csv), [predictions](https://github.com/dev-belly/interval-financial-risk/blob/main/docs/demo/predictions.csv).
- **Discuss:** Why test-fold averages differ from a pooled ROC curve; why nominal 90% conformal coverage with a near-unit-width interval is not useful discrimination; why same-company quarters weaken independence.
- **Boundary:** Labels are synthetic contemporaneous outcomes, not real future defaults. Financial statement publication timing remains unvalidated.

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

- **Audit / IT audit:** AuditLens first; CreditVintage or Interval Financial Risk second.
- **Bank data / risk analytics:** CreditVintage first; AuditLens or Interval Financial Risk second.
- **Quant engineering:** TradeForge first; AlphaForge or LedgerX second.

The remaining repositories include exploratory research and application prototypes. Their READMEs describe the implemented scope and limitations; do not present every repository as an equal-depth flagship project.
