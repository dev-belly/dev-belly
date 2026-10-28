# Project evidence and interview notes

These are **candidate resume bullets**, not claims about live customers or realized investment returns. Quoted results identify public-filing excerpts, observed dated/static credit samples, or a synthetic run. Choose two projects that fit the role and rehearse the assumptions and code path before using the wording in an interview.

## Public financial statement analysis

### [StatementTrace](https://github.com/dev-belly/StatementTrace)

> 构建公开财报的申报截止日快照与财务指标血缘工具，按实际财年起止日处理 53 周财年和后续申报中的比较期记录；使用 Apple 两份公开年报的 33 条人工摘录生成六组快照及九类财务指标，以独立 SQL 查询和语义复算核验取数、公式与来源，覆盖 42 项自动化测试。

- **Evidence:** [live report](https://dev-belly.github.io/StatementTrace/), [source ledger](https://github.com/dev-belly/StatementTrace/blob/main/docs/SOURCES.md), [selected facts](https://github.com/dev-belly/StatementTrace/blob/main/examples/demo/selected_facts.csv), [metric lineage](https://github.com/dev-belly/StatementTrace/blob/main/examples/demo/lineage.csv), [main CI and deployment](https://github.com/dev-belly/StatementTrace/actions/runs/39931468275).
- **Discuss:** Why filing `fy` cannot replace start/end; why filing date and acceptance timestamp differ; why missing is not zero; why reported annual growth is not week-normalized; why rehashed output corruption still fails replay.
- **Boundary:** Eleven configured US-GAAP USD concepts, date-granularity availability and a manually curated CompanyFacts-shaped excerpt. No raw-API-download, actual-restatement, universal-XBRL, credit-rating or investment-performance claim.

- **Report maintenance:** [#5](https://github.com/dev-belly/StatementTrace/pull/5) protects CSV labels and uses explicit browser identity keys. Main CI includes four real-Chrome selections; saved financial/source tables retain their original bytes.
- **Fiscal-calendar check:** [#6](https://github.com/dev-belly/StatementTrace/pull/6) requires adjacent configured periods for reported revenue growth. A skipped year or calendar gap keeps the current-period facts and other ratios but omits the non-adjacent growth base. The 53/52-week demo retains all nine saved files byte for byte; [main CI and deployment](https://github.com/dev-belly/StatementTrace/actions/runs/40066128539) pass.

## Counterparty network risk

### [NetworkClear](https://github.com/dev-belly/NetworkClear)

> 实现精确有理数债务清算与交易对手传染分析，在八家合成机构的 15 组压力情景中区分直接与连锁违约、内部未偿债务与外部债权人短缺；建立固定点证书和全网络资金勾稽，以独立违约集合穷举复核全部情景及 100 个随机小网络，覆盖 42 项自动化测试。

- **Evidence:** [live report](https://dev-belly.github.io/NetworkClear/), [method and schema](https://github.com/dev-belly/NetworkClear/blob/main/docs/METHODOLOGY.md), [payments](https://github.com/dev-belly/NetworkClear/blob/main/examples/demo/payments.csv), [individual debt flows](https://github.com/dev-belly/NetworkClear/blob/main/examples/demo/flows.csv), [main CI and deployment](https://github.com/dev-belly/NetworkClear/actions/runs/39931475585).
- **Discuss:** Debtor rows versus creditor columns; why outside debt ensures the implemented regularity contract; why rounds are not elapsed time; why fractional cents are a continuous-model output; why gross internal unpaid debt is not outside social loss.
- **Boundary:** Synthetic exposures, pro-rata one-period clearing and a stronger sufficient uniqueness condition. Exhaustive oracle limited to eight nodes; no collateral, seniority, fire sales, global-optimal capital allocation or real-bank risk estimate.

- **Report maintenance:** [#5](https://github.com/dev-belly/NetworkClear/pull/5) preserves exact scenario identities in CSV and browser selectors. Main CI includes five real-Chrome selections and refreshed report replay; numerical/source files are unchanged.

## Financial data engineering

### [PITBridge](https://github.com/dev-belly/PITBridge)

> 构建金融多源数据的时点特征引擎，区分观测、发布与入库时间，以 SQLite 选择当时可见的修订并处理删除、新鲜度与滚动窗口；实现 sum/mean/count 和逐源记录成员表，通过独立 Python 枚举、60 组随机历史与手算案例核验，覆盖 146 项自动化测试。

- **Evidence:** [snapshot report](https://dev-belly.github.io/PITBridge/), [rolling report](https://dev-belly.github.io/PITBridge/rolling/), [rolling members](https://github.com/dev-belly/PITBridge/blob/main/demo/rolling/members.csv), [hand-calculated case](https://github.com/dev-belly/PITBridge/blob/main/docs/ROLLING.md), [counterexample comparison](https://github.com/dev-belly/PITBridge/blob/main/demo/comparison.csv), [CI](https://github.com/dev-belly/PITBridge/actions/workflows/ci.yml).
- **Numeric validation:** Merged [PR #3](https://github.com/dev-belly/PITBridge/pull/3) brings the suite to 75 tests. Discuss SQLite's signed-integer boundary, binary64 rounding above 2⁵³, and why two values of 10³⁰⁸ have a finite mean even when their sum overflows. Original example artifacts replay unchanged.
- **Discuss:** Why availability must include publication and ingestion; why eligibility comes before revision ranking; why a tombstone must not revive an earlier revision; why the same 30-day inflow is 1,500 on February 10 and 4,300 on February 11; why member count does not establish business-data completeness; why zero differs from no history.
- **Boundary:** Scalar and rolling observations with source-supplied timestamps and revisions. A logical event is entity/source/feature/event time, so independent transactions sharing that identity need upstream aggregation or distinct features. The optional [CreditVintage adapter](https://github.com/dev-belly/CreditVintage/blob/main/docs/LINEAGE.md) consumes scalar credit features under an explicit UTC day-end contract; rolling cash-flow outputs remain a separate example. No production ingestion or distributed-scale benchmark is claimed. The original 11 leakage counterexamples are fixture counts, not a population rate.

- **Installed table intake:** [#19](https://github.com/dev-belly/PITBridge/pull/19) adds `build --csv-dir` and `aggregate --csv-dir` without pandas, with exact revisions, explicit null/boolean rules and pre-write validation. [#20](https://github.com/dev-belly/PITBridge/pull/20) preserves CSV/browser identities. The current suite has 146 tests; distribution jobs verify four installed JSON/CSV paths and the precision boundary, and the browser job checks the reports and interactive lesson. [CSV contract](https://github.com/dev-belly/PITBridge/blob/main/docs/CSV_INPUTS.md).
- **Checked release:** [#29](https://github.com/dev-belly/PITBridge/pull/29) publishes the timestamp-safe [v0.2.1 wheel](https://github.com/dev-belly/PITBridge/releases/tag/v0.2.1), with installed boundary checks and exact-commit evidence. [First run](START_HERE.md#pitbridge-historical-feature-selection). [#21](https://github.com/dev-belly/PITBridge/pull/21) introduced the checked release process; [#22](https://github.com/dev-belly/PITBridge/pull/22) and [#23](https://github.com/dev-belly/PITBridge/pull/23) repaired documentation and browser-start reliability.

## Credit portfolio risk

### [StressAtlas](https://github.com/dev-belly/StressAtlas)

> 实现含全局与行业因子的信用组合压力模拟，同一借款人的多笔贷款共享违约事件，以共同随机驱动比较情景；对 160 笔合成贷款、80 个借款人运行 5 组各 20,000 条路径，计算离散尾部 ES 与行业贡献；新增 300 次完整路径配对 bootstrap，诊断 VaR/ES 和情景变化的抽样精度，支持全量重放，覆盖 80 项自动化测试。

- **Evidence:** [scenario report](https://dev-belly.github.io/StressAtlas/), [tail precision report](https://dev-belly.github.io/StressAtlas/precision/), [all bootstrap estimates](https://github.com/dev-belly/StressAtlas/blob/main/demo/precision/resamples.csv), [precision method and case](https://github.com/dev-belly/StressAtlas/blob/main/docs/PRECISION.md), [sector attribution](https://github.com/dev-belly/StressAtlas/blob/main/demo/sector_es.csv), [CI](https://github.com/dev-belly/StressAtlas/actions/workflows/ci.yml).
- **Numeric validation:** Merged [PR #3](https://github.com/dev-belly/StressAtlas/pull/3) brings the suite to 70 tests. Integer-ratio rank calculation keeps discrete VaR/ES independent of a caller's Decimal precision and traps; low-precision and extreme-confidence regressions preserve the published simulation and bootstrap artifacts.
- **Discuss:** Why splitting a loan must not create extra independent defaults; why averaging all losses at or above VaR can mismeasure ES; why resampling whole paths preserves within-path borrower/factor dependence; why every scenario shares bootstrap indices; why a difference of two ES estimates is not ES of their pathwise loss difference; why a narrow interval cannot validate PD/LGD assumptions.
- **Boundary:** Synthetic parameters, one-period Gaussian factors and deterministic scenario LGD/EAD. Percentile intervals approximate Monte Carlo sampling uncertainty under fixed assumptions; discrete/sparse tails and unseen rare losses limit coverage. No calibration-error estimate, real borrower forecast or regulatory capital is claimed. Original path CSVs retain 200 inspection rows; full 20,000-path and 300-resample replay comes from saved inputs and seeds.

- **Report maintenance:** [#6](https://github.com/dev-belly/StressAtlas/pull/6) preserves CSV and browser identities. [Main CI](https://github.com/dev-belly/StressAtlas/actions/runs/39931491066) includes ten real-Chrome selections across the scenario and precision reports. The suite has 80 tests; all simulated losses, source inputs and bootstrap evidence retain their original bytes.

## Bank credit / model validation

### [CreditVintage](https://github.com/dev-belly/CreditVintage)

> 真实放款跨期验证侧表述：从两份共 1,236,084 条的官方 SBA 贷款 CSV 构建可重建的 35,000 条冻结样本，按真实放款期分成 20,000/5,000/10,000 训练、校准与测试记录，阶段间保留完整 24 月表现期；四项批准时输入只在训练集拟合填补、缩放和类别编码。测试 AUC 0.6723，同 1,000 个复核名额捕获 26/89 个记录内核销事件；保留校准后排名下降、逐年结果及 300 次成对月份重采样，以来源重拟合核验逐笔分数和完整证据 ZIP。

**Observed dates:** [SBA report](https://dev-belly.github.io/CreditVintage/sba-credit/) · [source, native target and protocol](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md) · [fit/refit implementation](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/sba_credit.py) · [checked v0.8.1](https://github.com/dev-belly/CreditVintage/releases/tag/v0.8.1) · [first run](START_HERE.md#creditvintage-validate-observed-loans-across-time).

**Explain before using the wording:** Why calendar maturity differs from a row-count gap; why 15,250 missing training interest rates remain visible; why calibration improves Brier but can hurt AUC and queue capture; why 89 events imply substantial uncertainty; why recorded charge-off is not 180-day DPD. Hash-based sampling is outcome-independent and borrower groups are an imperfect recorded-identity heuristic. The final snapshot lacks historical first-publication and feature-revision records: retrospective validation does not establish historical availability, savings, deployment or independent adoption. These notes do not establish that the author has already rehearsed the code.

> 信用卡建模与验证侧表述：以 30,000 条公开信用卡记录构建五组固定训练/校准/测试划分，训练集内拟合 19 项金融历史特征的缩放与编码，比较常数、Logistic、独立校准和梯度提升树；保存 12 万个模型分数及 60 组同预算复核结果，以来源重拟合核验逐笔分数、无标签队列及下载包。树模型五次平均 AUC 为 0.781、Brier 为 0.135；交付经隔离安装验证的版本包。

**Larger observed cohort:** [30,000-account report](https://dev-belly.github.io/CreditVintage/card-credit/) · [protocol and source conversion](https://github.com/dev-belly/CreditVintage/blob/main/docs/CARD_CREDIT.md) · [model/refit code](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/card_credit.py) · [v0.4.0 distributions](https://github.com/dev-belly/CreditVintage/releases/tag/v0.4.0). The five test sets overlap; 120,000 scores do not mean 120,000 independent borrowers. A single historical Taiwan cohort and its native subsequent-default target do not establish future-vintage, current-China or 180-day DPD performance.

**Editable event inputs:** [CreditVintage #20](https://github.com/dev-belly/CreditVintage/pull/20) adds a complete synthetic CSV starter and model-free diagnostics with file/physical-line locations, duplicate/revision/reference checks and mature-cohort gates. The installed wheel is checked by generating the files, evaluating their actual CSV paths, verifying 120 holdout records and locating a deliberately invalid principal at line 2. [Input code](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/inputs.py) · [Run with your own compatible records](https://github.com/dev-belly/CreditVintage/blob/main/docs/CUSTOM_INPUTS.md). This is reuse support, not evidence of independent users or real bank deployment.

**Before early monitoring:** [Model-free monitoring preflight](https://github.com/dev-belly/CreditVintage/pull/28) checks mature historical cohorts and visible current applications without requiring current outcomes. The installed editable case verifies 80 visible and 40 not-yet-visible current applications, then the actual monitor verifies the same 80. This checks input readiness, with no fitting, scores or PSI; it does not establish model quality. [Run the check](START_HERE.md#creditvintage-check-early-monitoring-before-training).

**Which inputs changed?** [v0.5.0 feature monitoring](https://github.com/dev-belly/CreditVintage/pull/32) requires neither historical nor current outcomes. It compares four numeric decision-time inputs and segment composition, marks small monthly samples as insufficient, and rebuilds its evidence from retained events. [Report](https://dev-belly.github.io/CreditVintage/feature-monitor/) · [Run it](START_HERE.md#creditvintage-inspect-input-distributions-without-labels).

**What was unavailable at the decision?** [v0.6.0 feature coverage](https://github.com/dev-belly/CreditVintage/pull/33) keeps all expected application-feature slots, including incomplete cases. It separates known late arrivals, post-decision observations and no event visible by the report cutoff; future events cannot explain earlier gaps. The synthetic case retains 320 current applications, 316 complete and four incomplete, with 160 future applications excluded. No outcomes or fitted model are needed. A verified diagnostic can still report incomplete coverage; scoring and distribution checks continue to reject missing inputs. [Report](https://dev-belly.github.io/CreditVintage/feature-quality/) · [Method](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_QUALITY.md) · [Run it](START_HERE.md#creditvintage-diagnose-missing-decision-time-features).

**Do the inputs meet explicit conditions?** [v0.7.0 coverage policies](https://github.com/dev-belly/CreditVintage/pull/34) check overall or named-month coverage and minimum sample counts using exact fractions. Every failed/insufficient rule is retained with the complete source diagnostic. A trusted policy digest can pin approved rules; a verified failed bundle is not a policy pass, and tolerant coverage does not permit incomplete scoring. [Report](https://dev-belly.github.io/CreditVintage/feature-check/) · [Run it](START_HERE.md#creditvintage-check-explicit-coverage-conditions).

> 规则验收侧表述：在时点特征覆盖诊断上增加显式规则检查，按整体或月份约束最低覆盖和申请数；用整数计数避免显示比例舍入误判，保留失败及证据不足结果、规则与来源台账。通过外部策略摘要核对批准规则，区分规则通过、证据一致和评分就绪；合成案例的三个规则失败全部保留，不把它当作实际业务效果。

> 数据质量侧表述：为信贷事件数据实现决策时点特征覆盖诊断，保留完整申请分母及逐月计数，区分迟到、决策后观测与截止日仍不可见的记录，并以首次可见到达计算迟延；保存逐申请特征台账和可重建报告，核验重新计算哈希后的虚假完整人数。合成示例包含 320 笔当前申请，其中 4 笔输入不完整；不把报告核验通过当作评分准备就绪。

> 输入监控侧表述：为信贷分析工具增加无需标签和模型拟合的五项决策时输入分布检查，保留原始事件、所选快照、累计计数与逐月样本口径；以手算及 SciPy 独立实现核对描述性距离，并在隔离安装包中验证两表接入和修改结果后重新计算哈希的失败路径。分布变化不等于预测失效，合成案例不证明业务效果。

> 公开数据验证侧表述：基于 UCI 1,000 条历史德国信贷记录建立固定 600/200/200 分层随机切分，只用训练集拟合缩放与类别编码，独立校准并导出逐笔证据；200 条测试记录的 Logistic AUC 为 0.774，保留校准后 Brier 由 0.162 变为 0.169 的负结果；实现原始数据重拟合核验与自定义时间窗口接入。

**Observed data:** [public credit comparison](https://dev-belly.github.io/CreditVintage/public-credit/) · [source, protocol and limits](https://github.com/dev-belly/CreditVintage/blob/main/docs/PUBLIC_CREDIT.md) · [custom event inputs](https://github.com/dev-belly/CreditVintage/blob/main/docs/CUSTOM_INPUTS.md). The UCI good/bad classification has no decision dates or 180-day DPD target. Its 200-record test sample and random split do not establish out-of-time performance; keep it separate from the synthetic evidence below.

> 公开数据对照侧表述：在 UCI 1,000 行历史信贷数据上，为常数基线、逻辑回归与梯度提升树建立五组相同的分层训练/测试划分，训练集内拟合标准化和类别编码，保存全部 15 组指标与 3,000 条测试分数；逻辑回归平均 AUC 约 0.767，并同时报告观察范围、Brier 和固定 Top-20 名额的结果。

**Public-data evidence:** [在线比较](https://dev-belly.github.io/CreditVintage/public-credit-comparison/) · [协议与来源](https://github.com/dev-belly/CreditVintage/blob/main/docs/PUBLIC_CREDIT_COMPARISON.md) · [训练代码](https://github.com/dev-belly/CreditVintage/blob/main/examples/german_credit.py)。这是独立的静态 good/bad-risk 分类，原始数据没有时间戳；五次测试有重叠，3,000 条预测不是 3,000 名独立客户。不得与下方合成 180 天逾期结果混用。

> 业务分析侧表述：为信贷风险项目增加可复现的 SQL 分组分析，按放款批次与客群生成 21 个聚合组及 48 笔无未来标签的复核清单；以独立 Python 重算验证指标分母、分组覆盖和排序，在 480 笔合成成熟测试申请上展示风险分析与报告核验流程。

**Business analysis:** [SQL cohort report](https://dev-belly.github.io/CreditVintage/analysis/) · [中文业务案例与面试追问](https://github.com/dev-belly/CreditVintage/blob/main/docs/BUSINESS_CASE.md) · [executed cohort SQL](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/business_groups.sql). 21 行覆盖四种分析视角，不能跨视角重复合计；48 笔复核清单不含未来标签。复核精确率为 25/48，事件捕获率为 25/107，不宣称减少实际损失。全体 10% 容量不等于每个客群各选 10%。

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
- **Priority and source integrity:** [#7](https://github.com/dev-belly/AuditLens/pull/7) fixes two source inputs one floating-point step apart producing the same hash despite selecting different vouchers. The versioned fingerprint retains full binary64 priority precision. [#8](https://github.com/dev-belly/AuditLens/pull/8) preserves fullwidth/multiline identities in the review queue and high-risk CSV, with a completed-workpaper handoff regression. Completed [#6](https://github.com/dev-belly/AuditLens/pull/6) retains conflicting voucher evidence and handles nonfinite/overflowing amounts. The full local suite has 519 tests; default reports retain their bytes apart from the new source-fingerprint record.
- **Discuss:** Why the random inclusion probability applies only to the non-targeted frame; why an anomaly flag is not a confirmed fraud finding; how the workpaper checksum and input fingerprint differ; why hashing and parsing a file in separate reads can cite inconsistent versions.
- **Boundary:** The 919 injected anomalies and all detection metrics come from synthetic data. No client ledger or real fraud labels were used.

### [ControlTrace](https://github.com/dev-belly/ControlTrace)

> 构建系统访问与生产变更的合成审计平台：以稳定 ID 连接 HR、账号、授权、审批、代码提交和部署记录，执行五项内控测试；逐条保留规则口径、时间线和来源证据，支持追加式人工复核，并导出可校验与重放的工作底稿。

- **Evidence:** [control catalog](https://github.com/dev-belly/ControlTrace/blob/main/docs/CONTROL_CATALOG.md), [worked review case](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md), [CI](https://github.com/dev-belly/ControlTrace/actions/workflows/ci.yml).
- **Versioned CSV policy:** [#7](https://github.com/dev-belly/ControlTrace/pull/7) adds visible spreadsheet-text protection in 0.2.9 / bundle format 4 while retaining exact format-2/3 replay. A real export produced by the unmodified 0.2.8 code is retained as a synthetic test fixture, including formula/multiline review notes. All 108 local tests and [main CI](https://github.com/dev-belly/ControlTrace/actions/runs/40066173324) pass; the compatibility path does not give format 2 evidence-binding guarantees.
- **UTC chronology and old reviews:** completed [#6](https://github.com/dev-belly/ControlTrace/pull/6) brings the current package to 0.2.10 / format 5 and 113 local tests. Fractional seconds and mixed offsets are ordered by actual UTC instants; old formats 2–4 retain their original order with an explicit notice. An actual 0.2.9 fixture verifies both historical replay and the requirement for a fresh review under the corrected timeline. All 28 source files remain byte-identical in the demonstrated upgrade.
- **Discuss:** Why a missing join is a data gap rather than proof of control failure; why approval must follow request and precede grant or deployment; why the workpaper hash checks internal consistency but does not prove external source authenticity.
- **Boundary:** The twelve seeded observations are synthetic test cases, not a measured detection rate. Full extract completeness and real access effectiveness need separate procedures.

## Quant research / execution engineering

### [TradeForge](https://github.com/dev-belly/TradeForge)

> 构建 C++20 订单簿与 Python 研究层，对四种执行策略在同一合成事件流下进行可复现对比；同时报告到达价与区间 VWAP 的交易成本，并用 Python/C++ 逐事件对照、因果测试和 CI sanitizers 检查结果可靠性。

- **Evidence:** [deterministic synthetic cost table](https://github.com/dev-belly/TradeForge#sixty-second-tour), [verified public-quote matching case](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md), [verification contract](https://github.com/dev-belly/TradeForge#what-makes-the-numbers-defensible), [CI](https://github.com/dev-belly/TradeForge/actions/workflows/ci.yml).
- **Real-quote validation (separate from synthetic OMS):** [Merged #14](https://github.com/dev-belly/TradeForge/pull/14) freezes a 40-second public DOGEUSDT depth episode and replays complete L2 packets offline. All 18 aggressive matching cells use the same 1,000-DOGE / 20-second decision window: immediate vs ten equal-time slices, assumed 0/1/10-ms latency and 0/5/10-bps taker fees. At 0 fee/latency the costs are 1.724 vs 1.914 bps relative to the same arrival midpoint; in this episode none of the three latency assumptions changes execution price. This is not measured order latency, real fills, passive-queue fidelity or evidence of a trading edge.
- **Numeric validation:** [PR #2](https://github.com/dev-belly/TradeForge/pull/2) converts human prices to half-up integer ticks by exact integer ratios and constructs decimal notionals without intermediate rounding. Low-precision Decimal contexts and arithmetic traps cannot change those conversions; [main CI](https://github.com/dev-belly/TradeForge/actions/runs/37191280682) also passes the C++ differential, sanitizer and deterministic replay jobs.
- **Fee validation:** [PR #3](https://github.com/dev-belly/TradeForge/pull/3) charges the broker minimum once per child order while retaining venue fees and rebates. [PR #5](https://github.com/dev-belly/TradeForge/pull/5) makes fee amounts independent of caller Decimal settings; [PR #4](https://github.com/dev-belly/TradeForge/pull/4) rejects negative/non-finite parameters, booleans and malformed fill inputs, including negative decimals that underflow to signed zero. Together, 78 targeted cases include 400 mixed maker/taker partial-fill partitions reconciled to independent whole-order totals; [repair CI](https://github.com/dev-belly/TradeForge/actions/runs/37654829165) passes the Python matrix, native differential, sanitizer and deterministic replay jobs. The [combined main CI](https://github.com/dev-belly/TradeForge/actions/runs/37711097927) also passed all six jobs.
- **Discuss:** Why one execution can beat arrival price but lose to interval VWAP; exact L3 FIFO versus approximate L2 queue; why a synthetic cost difference is not a venue performance claim; why a very long decimal just below half a tick must not round upward before tick conversion.
- **Fee questions:** Why three fills on one child order share one minimum; why a broker commission cannot floor away a venue rebate; why zero-notional quotes still validate quantities and parameters; why low precision can erase a small incremental commission when two cumulative amounts are subtracted.
- **Window integrity:** Merged [PR #7](https://github.com/dev-belly/TradeForge/pull/7) separates replay warm-up from parent-window volume and isolates post-window markout observations from arrival/terminal benchmarks. A missing tick at `parent.end_ns` uses a deadline timer and the last eligible in-window book, not a later market state; a window without any eligible quote cannot invent a sweep. Six normalized-CSV regressions exercise delayed starts, empty windows, later markouts and sparse end ticks. One synthetic check reconciles 50 filled units against 100 in-window units as 50% participation. Both [PR-head CI](https://github.com/dev-belly/TradeForge/actions/runs/37712196848) and [post-merge main CI](https://github.com/dev-belly/TradeForge/actions/runs/37738744500) passed Python 3.11–3.13, C++ differential, sanitizers and reproducibility.
- **Combined regression check:** All 113 fee/window cases passed locally against the published `PR #7` tree, including the six normalized-CSV harness regressions. The subsequent README correction in [PR #8](https://github.com/dev-belly/TradeForge/pull/8) also passed [all six main CI jobs](https://github.com/dev-belly/TradeForge/actions/runs/37739802938).
- **Window questions:** Why must warm-up trades rebuild the book but not count toward parent participation? Why can future prices measure markout without entering execution benchmarks? What goes wrong when the feed skips the exact deadline? Why is an execution percentage sensitive to the denominator's time window?
- **Lifecycle validation:** Merged [PR #9](https://github.com/dev-belly/TradeForge/pull/9) repairs cancellation of children still in transit. A 100-unit synthetic parent previously filled 150 units when a late child and its replacement sweep both executed; cancellation now closes the original child before computing the replacement. Terminal children ignore delayed callbacks, and the open-order guard counts live orders rather than stale scheduled actions. Eight normalized-CSV cases reconcile quantities, child states and timestamps across cancel, sweep, leave, exact-deadline arrival and one-/ten-order limits. [Repair CI](https://github.com/dev-belly/TradeForge/actions/runs/37772324785) passed all six jobs; [merged main CI](https://github.com/dev-belly/TradeForge/actions/runs/37773367077) also passed all six jobs. Configured latency still applies to a new terminal sweep.
- **Lifecycle questions:** Why an order awaiting venue acceptance must still be cancellable; why cancellation releases both working quantity and order capacity; why a scheduled callback is not necessarily a live order; why an arrival exactly at the deadline is processed before computing the final remainder.
- **Cash-cost reconciliation:** [PR #10](https://github.com/dev-belly/TradeForge/pull/10) carries explicit cash fees and net rebates through total shortfall, attribution, Parquet and SQL. A USD 5 fee against 100 requested shares at a USD 100 arrival price contributes 5 bps on BUY or SELL, even if only half fills; filled-leg attribution uses its own filled arrival-notional denominator. Twenty regression cases prevent fees from disappearing into an offsetting residual, including hostile Decimal contexts. [Merged fee-repair CI](https://github.com/dev-belly/TradeForge/actions/runs/37774684223) passed all six jobs.
- **CLI evidence:** [PR #11](https://github.com/dev-belly/TradeForge/pull/11) refreshes all eight demo rows and the guide's report, including passive TWAP's -8.0246 bps total and 0.0003 bps unexplained residual. Three additional cases compare the quoted columns and report rows with the documented `demo` and `run` commands; the full local suite passed 859 cases, with 152 compiled/optional skips. [PR CI](https://github.com/dev-belly/TradeForge/actions/runs/37865674865) and [merged main CI](https://github.com/dev-belly/TradeForge/actions/runs/37866454671) passed the Python matrix, C++ differential, sanitizers and reproducibility checks.
- **Cost questions:** Why fees worsen both BUY and SELL even though signed price costs reverse; why total and filled-leg shortfall have different denominators on a partial fill; why a net rebate lowers total cost without becoming unexplained impact; why price-only benchmarks and fee-inclusive totals can differ.

### [AlphaForge](https://github.com/dev-belly/alphaforge) and [LedgerX](https://github.com/dev-belly/LedgerX)

> 在 AlphaForge 因子研究平台中将信号日与成交日分离，以逐信号执行队列处理重叠调仓和样本边界；另在 LedgerX 中实现独立的 Decimal 双重记账日志，以时点可得的外部报价核对已实现与未实现损益。两个仓库目前是分别演示的研究组件。

- **Evidence:** [AlphaForge backtest mechanics](https://github.com/dev-belly/alphaforge/blob/main/docs/modules/backtesting.md), [real-price comparison & limits](https://github.com/dev-belly/alphaforge/blob/main/docs/research-comparison.md), [synthetic backtest record](https://dev-belly.github.io/alphaforge/sample-run/), [LedgerX valuation example](https://github.com/dev-belly/LedgerX/blob/main/examples/valuation.json), their CI runs.
- **Archived real-price comparison:** [AlphaForge #4](https://github.com/dev-belly/alphaforge/pull/4) freezes 551,698 forecasts and all 22 seed/cost comparisons. The [protocol correction in #5](https://github.com/dev-belly/alphaforge/pull/5) identifies calendar-day purge/embargo buffers applied to trading-session labels. Those historical artifacts have not been refitted with the corrected splitter and do not establish leakage-free out-of-sample results. Their recorded net Sharpes of 1.141 (equal weight), 1.005 (Ridge) and 1.337 (LightGBM three-seed mean) remain historical figures, not corrected estimates. Recalculating daily-return arithmetic cannot validate the original model split. Incomplete historical constituents/delistings, assumed filing lags and a dollar-volume size proxy remain separate limits.
- **Correctness repairs · 2026-10-27:** [#5](https://github.com/dev-belly/alphaforge/pull/5) counts supplied trading sessions; [#6](https://github.com/dev-belly/alphaforge/pull/6) compounds the first complete rolling-return window; [#7](https://github.com/dev-belly/alphaforge/pull/7) fits factor returns with a transposed pseudoinverse, reconstructs residuals in asset space and aligns both covariance axes by factor labels. Local regression groups pass 87, 85 and 49 cases respectively; [validation](PROJECT_REVIEW.md#financial-correctness-repairs--2026-10-27) separates these code checks from archived model performance.
- **Discuss:** Why a signal formed at today's close cannot fill on that same close; historical cost versus external mark; what a hash chain can detect only when its head is checked against an independent checkpoint.
- **Execution validation:** Merged [AlphaForge PR #2](https://github.com/dev-belly/alphaforge/pull/2) rejects fractional session counts and negative cost assumptions, and makes the string `"false"` disable fractional fills. Its complete pipeline and API suite passes 1,267 tests; the local coverage run measures 96%.
- **Drawdown and installation validation:** Merged [AlphaForge PR #3](https://github.com/dev-belly/alphaforge/pull/3) includes pre-first-session capital in summary, rolling, episode and chart drawdowns; returns of -20% then +10% imply a 20% maximum drawdown and a 12% loss from starting wealth. Packaged defaults support wheel installs outside the checkout. Its [PR CI](https://github.com/dev-belly/alphaforge/actions/runs/38111341159) and [post-merge main CI](https://github.com/dev-belly/alphaforge/actions/runs/38186528393) both pass all checks; the main run confirms 1,273 full-suite tests and 96% coverage, alongside Windows fast checks and Linux pipeline/API checks.
- **Drawdown questions:** Why can a first-period loss vanish if the first observed NAV is treated as the initial peak? Why does a 10% gain after a 20% loss leave wealth at 88%? Which default configuration is selected inside a checkout, outside it, or with an explicit path?
- **Accounting validation:** Merged [LedgerX PR #1](https://github.com/dev-belly/LedgerX/pull/1) isolates the accounting Decimal context and rejects sub-quantum amounts even when nonzero digits occur far beyond ordinary precision. Its 38 tests make the numeric contract part of the reproducibility evidence.
- **Boundary:** AlphaForge's *sample* and LedgerX's fills/quotes are synthetic; AlphaForge also has a **separate, exploratory historical-price study** with documented source-availability limits. Neither is evidence of a live trading edge or actual brokerage reconciliation.

## Choosing what goes on a resume

- **Financial audit analytics:** AuditLens first; ControlTrace or CreditVintage second.
- **IT audit / technology risk:** ControlTrace first; AuditLens second.
- **Financial statement / financial data analysis:** StatementTrace first; PITBridge second.
- **Financial data engineering:** PITBridge first; CreditVintage or StatementTrace second.
- **Bank model validation:** CreditVintage first; PITBridge second.
- **Portfolio risk analytics:** StressAtlas first; CreditVintage second.
- **Counterparty / network risk:** NetworkClear first; StressAtlas second.
- **Quant engineering:** TradeForge first; AlphaForge or LedgerX second.

The remaining repositories include exploratory research and application prototypes. Their READMEs describe the implemented scope and limitations; do not present every repository as an equal-depth flagship project.
