# Project evidence and interview notes

These are **candidate resume bullets**, not claims about live customers or realized investment returns. Every quoted result is from a linked synthetic run. Choose two projects that fit the role and rehearse the assumptions and code path before using the wording in an interview.

## Financial data engineering

### [PITBridge](https://github.com/dev-belly/PITBridge)

> 构建金融多源数据的时点特征引擎，区分观测、发布与入库时间，以 SQLite 选择当时可见的修订并处理删除、新鲜度与滚动窗口；实现 sum/mean/count 和逐源记录成员表，通过独立 Python 枚举、60 组随机历史与手算案例核验，覆盖 75 项自动化测试。

- **Evidence:** [snapshot report](https://dev-belly.github.io/PITBridge/), [rolling report](https://dev-belly.github.io/PITBridge/rolling/), [rolling members](https://github.com/dev-belly/PITBridge/blob/main/demo/rolling/members.csv), [hand-calculated case](https://github.com/dev-belly/PITBridge/blob/main/docs/ROLLING.md), [counterexample comparison](https://github.com/dev-belly/PITBridge/blob/main/demo/comparison.csv), [CI](https://github.com/dev-belly/PITBridge/actions/workflows/ci.yml).
- **Numeric validation:** Merged [PR #3](https://github.com/dev-belly/PITBridge/pull/3) brings the suite to 75 tests. Discuss SQLite's signed-integer boundary, binary64 rounding above 2⁵³, and why two values of 10³⁰⁸ have a finite mean even when their sum overflows. Original example artifacts replay unchanged.
- **Discuss:** Why availability must include publication and ingestion; why eligibility comes before revision ranking; why a tombstone must not revive an earlier revision; why the same 30-day inflow is 1,500 on February 10 and 4,300 on February 11; why member count does not establish business-data completeness; why zero differs from no history.
- **Boundary:** Scalar and rolling observations with source-supplied timestamps and revisions. A logical event is entity/source/feature/event time, so independent transactions sharing that identity need upstream aggregation or distinct features. The optional [CreditVintage adapter](https://github.com/dev-belly/CreditVintage/blob/main/docs/LINEAGE.md) consumes scalar credit features under an explicit UTC day-end contract; rolling cash-flow outputs remain a separate example. No production ingestion or distributed-scale benchmark is claimed. The original 11 leakage counterexamples are fixture counts, not a population rate.

## Credit portfolio risk

### [StressAtlas](https://github.com/dev-belly/StressAtlas)

> 实现含全局与行业因子的信用组合压力模拟，同一借款人的多笔贷款共享违约事件，以共同随机驱动比较情景；对 160 笔合成贷款、80 个借款人运行 5 组各 20,000 条路径，计算离散尾部 ES 与行业贡献；新增 300 次完整路径配对 bootstrap，诊断 VaR/ES 和情景变化的抽样精度，支持全量重放，覆盖 70 项自动化测试。

- **Evidence:** [scenario report](https://dev-belly.github.io/StressAtlas/), [tail precision report](https://dev-belly.github.io/StressAtlas/precision/), [all bootstrap estimates](https://github.com/dev-belly/StressAtlas/blob/main/demo/precision/resamples.csv), [precision method and case](https://github.com/dev-belly/StressAtlas/blob/main/docs/PRECISION.md), [sector attribution](https://github.com/dev-belly/StressAtlas/blob/main/demo/sector_es.csv), [CI](https://github.com/dev-belly/StressAtlas/actions/workflows/ci.yml).
- **Numeric validation:** Merged [PR #3](https://github.com/dev-belly/StressAtlas/pull/3) brings the suite to 70 tests. Integer-ratio rank calculation keeps discrete VaR/ES independent of a caller's Decimal precision and traps; low-precision and extreme-confidence regressions preserve the published simulation and bootstrap artifacts.
- **Discuss:** Why splitting a loan must not create extra independent defaults; why averaging all losses at or above VaR can mismeasure ES; why resampling whole paths preserves within-path borrower/factor dependence; why every scenario shares bootstrap indices; why a difference of two ES estimates is not ES of their pathwise loss difference; why a narrow interval cannot validate PD/LGD assumptions.
- **Boundary:** Synthetic parameters, one-period Gaussian factors and deterministic scenario LGD/EAD. Percentile intervals approximate Monte Carlo sampling uncertainty under fixed assumptions; discrete/sparse tails and unseen rare losses limit coverage. No calibration-error estimate, real borrower forecast or regulatory capital is claimed. Original path CSVs retain 200 inspection rows; full 20,000-path and 300-resample replay comes from saved inputs and seeds.

## Bank credit / model validation

### [CreditVintage](https://github.com/dev-belly/CreditVintage)

> 实现申请时点可得特征和 180 天逾期标签成熟校验，以分离的训练、校准及跨期测试批次评估信贷风险基线；在 480 笔合成测试申请上得到 ROC-AUC 0.747、Brier 0.155，并保留独立校准后 Brier 变差的结果；早期监控路径仅用当期申请分数计算分布漂移，不偷用尚未成熟的逾期结果。

> 数据质量与验证侧表述：为信贷风险报告实现独立核验，基于逐笔预测重算模型指标、分组损失场景和分数漂移；校验标签成熟窗口、复核容量与 CSV 结构，以更新哈希后的异常报告验证核验流程能够拒绝不一致结果。

> 系统集成侧表述：连接 PITBridge 的决策时点源记录与 CreditVintage 模型，校验身份、单位、七天新鲜度和 UTC 日终边界；在 480 笔合成申请的联合案例中导出 1,440 个特征值，排除 192 条决策后才可得的记录，保留 120 笔测试预测，并从原始事件完整重放到模型输出。

联合案例与上方原始评估使用不同样本：原始评估有 480 笔测试申请，联合案例有 480 笔总申请、其中 120 笔测试申请。不要把两者的样本量和模型指标混在一起。

- **Evidence:** [test report](https://dev-belly.github.io/CreditVintage/demo/), [row-level predictions](https://github.com/dev-belly/CreditVintage/blob/main/docs/demo/predictions.csv), [early monitor](https://dev-belly.github.io/CreditVintage/monitor/), [report-contract regressions](https://github.com/dev-belly/CreditVintage/blob/main/tests/test_artifact_contract.py), [CI](https://github.com/dev-belly/CreditVintage/actions/workflows/ci.yml).
- **Integration evidence:** [online explorer](https://dev-belly.github.io/CreditVintage/lineage/), [complete evidence ZIP](https://dev-belly.github.io/CreditVintage/lineage/evidence.zip), [adapter contract](https://github.com/dev-belly/CreditVintage/blob/main/docs/LINEAGE.md), [source generator and lineage exporter](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/lineage.py), [integration regressions](https://github.com/dev-belly/CreditVintage/blob/main/tests/test_lineage.py). The public synthetic bundle is generated, verified and published by the Pages build; its generated files stay outside Git history.
- **Report validation:** Merged [PR #4](https://github.com/dev-belly/CreditVintage/pull/4) brings the suite to 70 tests. The verifier independently resamples complete origination months 300 times, checks confidence intervals, rejects duplicate JSON keys and rebuilds report HTML. Twelve new tampering cases include changed intervals and pages with recomputed hashes; original reports and the full lineage replay still verify.
- **Download validation:** Merged [PR #7](https://github.com/dev-belly/CreditVintage/pull/7) brings the suite to 75 tests and 28 subtests. The local and published explorers generate a fixed 19-file ZIP; regressions check extraction and full model replay, repeated bytes, excluded unrelated files and legacy page reconstruction. The actual published ZIP's 18 hashed members match its manifest and replay from PIT sources through every held-out prediction.
- **Discuss:** `observed_at` versus `available_at`; why missing six-report coverage is not a nondefault; why PSI cannot establish realized default or calibration drift; why isotonic calibration was retained as a negative result; why `NaN` breaks an ordinary tolerance comparison and a matching hash does not establish valid report content.
- **Integration questions:** Why a noon publication ingested at next-day midnight is unavailable at the decision; why calendar dates require an explicit UTC day-end convention; why source replay and model refitting add evidence beyond file hashes; why changed evaluation configurations must fail even when prediction values happen to remain the same.
- **Boundary:** The 90+ DPD within 180 days is a research label. The synthetic AUC and probability × principal × assumed LGD scenario are not regulatory default or expected credit loss estimates.

### [Interval Financial Risk](https://github.com/dev-belly/interval-financial-risk)

> 将四季度点值扩展为分布与波动区间特征，对 300 家模拟公司、4,800 条季度记录进行扩展窗口测试及消融；同一 Logistic 算法加入区间特征后，三个测试折的平均 AUC 从 0.7243 降至 0.6857，保留负结果并公开逐笔预测和切分记录。

- **Evidence:** [interactive report](https://dev-belly.github.io/interval-financial-risk/), [fold splits](https://github.com/dev-belly/interval-financial-risk/blob/main/docs/demo/fold_splits.csv), [predictions](https://github.com/dev-belly/interval-financial-risk/blob/main/docs/demo/predictions.csv).
- **Discuss:** Why test-fold averages differ from a pooled ROC curve; why nominal 90% conformal coverage with a near-unit-width interval is not useful discrimination; why same-company quarters weaken independence.
- **Boundary:** Labels are synthetic contemporaneous outcomes, not real future defaults. Financial statement publication timing remains unvalidated.

## Audit / risk consulting

### [AuditLens](https://github.com/dev-belly/AuditLens)

> 构建合成凭证审计分析流程：对 30,128 笔凭证运行九项审计规则、Benford 检验与 Isolation Forest，输出可追溯的规则证据、SQLite 查询结果和 Streamlit 风险看板；按规则覆盖、风险排序与概率抽样生成 300 笔复核工作底稿，并验证人工复核结果与抽样来源。

- **Evidence:** [reports and the 300-row workpaper](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports), [methodology](https://github.com/dev-belly/AuditLens/blob/main/docs/methodology.md), [CI](https://github.com/dev-belly/AuditLens/actions/workflows/ci.yml).
- **Review validation:** [PR #3](https://github.com/dev-belly/AuditLens/pull/3) binds outcome counts and file digests to the same captured CSV bytes. A concurrent save cannot make the report cite one version while counting another; [main CI](https://github.com/dev-belly/AuditLens/actions/runs/37191026460) passes the pipeline, tests and reproducibility check.
- **Discuss:** Why the random inclusion probability applies only to the non-targeted frame; why an anomaly flag is not a confirmed fraud finding; how the workpaper checksum and input fingerprint differ; why hashing and parsing a file in separate reads can cite inconsistent versions.
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
- **Numeric validation:** [PR #2](https://github.com/dev-belly/TradeForge/pull/2) converts human prices to half-up integer ticks by exact integer ratios and constructs decimal notionals without intermediate rounding. Low-precision Decimal contexts and arithmetic traps cannot change those conversions; [main CI](https://github.com/dev-belly/TradeForge/actions/runs/37191280682) also passes the C++ differential, sanitizer and deterministic replay jobs.
- **Fee validation:** [PR #3](https://github.com/dev-belly/TradeForge/pull/3) charges the broker minimum once per child order while retaining venue fees and rebates. [PR #5](https://github.com/dev-belly/TradeForge/pull/5) makes fee amounts independent of caller Decimal settings; [PR #4](https://github.com/dev-belly/TradeForge/pull/4) rejects negative/non-finite parameters, booleans and malformed fill inputs, including negative decimals that underflow to signed zero. Together, 78 targeted cases include 400 mixed maker/taker partial-fill partitions reconciled to independent whole-order totals; [repair CI](https://github.com/dev-belly/TradeForge/actions/runs/37654829165) passes the Python matrix, native differential, sanitizer and deterministic replay jobs. The [combined main CI](https://github.com/dev-belly/TradeForge/actions/runs/37711097927) also passed all six jobs.
- **Discuss:** Why one execution can beat arrival price but lose to interval VWAP; exact L3 FIFO versus approximate L2 queue; why a synthetic cost difference is not a venue performance claim; why a very long decimal just below half a tick must not round upward before tick conversion.
- **Fee questions:** Why three fills on one child order share one minimum; why a broker commission cannot floor away a venue rebate; why zero-notional quotes still validate quantities and parameters; why low precision can erase a small incremental commission when two cumulative amounts are subtracted.
- **Window integrity:** Merged [PR #7](https://github.com/dev-belly/TradeForge/pull/7) separates replay warm-up from parent-window volume and isolates post-window markout observations from arrival/terminal benchmarks. A missing tick at `parent.end_ns` uses a deadline timer and the last eligible in-window book, not a later market state; a window without any eligible quote cannot invent a sweep. Six normalized-CSV regressions exercise delayed starts, empty windows, later markouts and sparse end ticks. One synthetic check reconciles 50 filled units against 100 in-window units as 50% participation. Both [PR-head CI](https://github.com/dev-belly/TradeForge/actions/runs/37712196848) and [post-merge main CI](https://github.com/dev-belly/TradeForge/actions/runs/37738744500) passed Python 3.11–3.13, C++ differential, sanitizers and reproducibility.
- **Combined regression check:** All 113 fee/window cases passed locally against the published `PR #7` tree, including the six normalized-CSV harness regressions. The subsequent README correction in [PR #8](https://github.com/dev-belly/TradeForge/pull/8) also passed [all six main CI jobs](https://github.com/dev-belly/TradeForge/actions/runs/37739802938).
- **Window questions:** Why must warm-up trades rebuild the book but not count toward parent participation? Why can future prices measure markout without entering execution benchmarks? What goes wrong when the feed skips the exact deadline? Why is an execution percentage sensitive to the denominator's time window?
- **Lifecycle validation:** Merged [PR #9](https://github.com/dev-belly/TradeForge/pull/9) repairs cancellation of children still in transit. A 100-unit synthetic parent previously filled 150 units when a late child and its replacement sweep both executed; cancellation now closes the original child before computing the replacement. Terminal children ignore delayed callbacks, and the open-order guard counts live orders rather than stale scheduled actions. Eight normalized-CSV cases reconcile quantities, child states and timestamps across cancel, sweep, leave, exact-deadline arrival and one-/ten-order limits. [Repair CI](https://github.com/dev-belly/TradeForge/actions/runs/37772324785) passed all six jobs; [merged main CI](https://github.com/dev-belly/TradeForge/actions/runs/37773367077) also passed all six jobs. Configured latency still applies to a new terminal sweep.
- **Lifecycle questions:** Why an order awaiting venue acceptance must still be cancellable; why cancellation releases both working quantity and order capacity; why a scheduled callback is not necessarily a live order; why an arrival exactly at the deadline is processed before computing the final remainder.

### [AlphaForge](https://github.com/dev-belly/alphaforge) and [LedgerX](https://github.com/dev-belly/LedgerX)

> 在 AlphaForge 因子研究平台中将信号日与成交日分离，以逐信号执行队列处理重叠调仓和样本边界；另在 LedgerX 中实现独立的 Decimal 双重记账日志，以时点可得的外部报价核对已实现与未实现损益。两个仓库目前是分别演示的研究组件。

- **Evidence:** [AlphaForge backtest mechanics](https://github.com/dev-belly/alphaforge/blob/main/docs/modules/backtesting.md), [synthetic backtest record](https://dev-belly.github.io/alphaforge/sample-run/), [LedgerX valuation example](https://github.com/dev-belly/LedgerX/blob/main/examples/valuation.json), their CI runs.
- **Discuss:** Why a signal formed at today's close cannot fill on that same close; historical cost versus external mark; what a hash chain can detect only when its head is checked against an independent checkpoint.
- **Execution validation:** Merged [AlphaForge PR #2](https://github.com/dev-belly/alphaforge/pull/2) rejects fractional session counts and negative cost assumptions, and makes the string `"false"` disable fractional fills. Its complete pipeline and API suite passes 1,267 tests; the local coverage run measures 96%.
- **Accounting validation:** Merged [LedgerX PR #1](https://github.com/dev-belly/LedgerX/pull/1) isolates the accounting Decimal context and rejects sub-quantum amounts even when nonzero digits occur far beyond ordinary precision. Its 38 tests make the numeric contract part of the reproducibility evidence.
- **Boundary:** AlphaForge's sample and LedgerX's fills/quotes are synthetic. Neither is evidence of a live trading edge or actual brokerage reconciliation.

## Choosing what goes on a resume

- **Financial audit analytics:** AuditLens first; ControlTrace or CreditVintage second.
- **IT audit / technology risk:** ControlTrace first; AuditLens second.
- **Financial data engineering:** PITBridge first; CreditVintage second.
- **Bank model validation:** CreditVintage first; PITBridge second.
- **Portfolio risk analytics:** StressAtlas first; CreditVintage second.
- **Quant engineering:** TradeForge first; AlphaForge or LedgerX second.

The remaining repositories include exploratory research and application prototypes. Their READMEs describe the implemented scope and limitations; do not present every repository as an equal-depth flagship project.
