<div align="center">
  <img src="assets/profile-signal-v3.svg" width="100%" alt="dev-belly — Finance. Data. Evidence. CUFE data science student building inspectable financial systems." />
  <br /><br />
  <a href="https://colab.research.google.com/github/dev-belly/PITBridge/blob/main/examples/decision_time.ipynb"><b>RUN IN BROWSER</b></a> &nbsp; / &nbsp;
  <a href="https://dev-belly.github.io/CreditVintage/sba-credit/"><b>LIVE DEMO</b></a> &nbsp; / &nbsp;
  <a href="PROJECT_BRIEFS.md"><b>RESULTS &amp; CODE</b></a> &nbsp; / &nbsp;
  <a href="#research-in-public"><b>RECENT WORK</b></a>
</div>

<br />

I'm **dev-belly**, a **Data Science & Big Data Technology** student at **Central University of Finance and Economics**. I build tools for credit risk, financial data analysis and quantitative research.

把金融问题拆成能运行、能检验、能追溯的系统：从 SQL 客群分析和人工复核，到决策时点的数据、财报指标与组合风险。

**New here?** [Change one invoice timestamp in your browser](START_HERE.md#try-in-your-browser), [install a project from an empty directory](START_HERE.md#try-a-project), or [review a business decision and its code](START_HERE.md#review-the-work). 新访客可先在浏览器核对三次固定决策，再改一个时间；招聘与面试审阅可沿业务问题、结果和代码查看。

## Start with a business question

| Question | Open the result | Follow the code |
| :--- | :--- | :--- |
| Does a model hold up on later funding cohorts? | [35,000 observed SBA loans](https://dev-belly.github.io/CreditVintage/sba-credit/) | [Training and refitting](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/sba_credit.py) · [Protocol](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md) |
| Which credit cohorts need attention? | [SQL credit analysis](https://dev-belly.github.io/CreditVintage/analysis/) | [Cohort SQL](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/business_groups.sql) · [Review workflow](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_WORKFLOW.md) |
| Do the inputs meet explicit coverage rules? | [Policy check](https://dev-belly.github.io/CreditVintage/feature-check/) · [Coverage and delays](https://dev-belly.github.io/CreditVintage/feature-quality/) | [Rules and replay](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/feature_policy.py) · [Contract](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_POLICY.md) |
| What could a decision know before a late correction arrived? | [Run three decisions in your browser](https://colab.research.google.com/github/dev-belly/PITBridge/blob/main/examples/decision_time.ipynb) | [Three-decision example](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md) |
| How does clustered default change portfolio losses? | [Stress report](https://dev-belly.github.io/StressAtlas/) | [Tail math and uncertainty](https://github.com/dev-belly/StressAtlas/blob/main/docs/METHODOLOGY.md) |

**A useful result includes its limits.** The [SBA study](https://dev-belly.github.io/CreditVintage/sba-credit/) uses real funding dates and a native 24-month recorded charge-off target. Logistic AUC is 0.6723 on 10,000 later loans; calibration improves Brier while reducing ranking performance. The final snapshot cannot establish historical first-publication times. Separate UCI static and synthetic event experiments retain their own targets. [Project evidence](PROJECT_BRIEFS.md) connects each claim to inputs, code and validation.

## Flagship projects

<a href="https://github.com/dev-belly/CreditVintage"><img src="assets/creditvintage-v3.svg" width="100%" alt="CreditVintage — chronological credit evaluation with separate training, calibration and holdout cohorts, plus source-record lineage." /></a>

**01 · CreditVintage — Credit analysis that reaches a review decision.**

训练、校准、测试分期隔离；标签等待完整表现期。SQL 按放款月份和客群对照风险事件与预测偏差；固定容量清单不含未来标签。SQLite 复核工作区记录认领、结案、理由和材料引用，并处理并发版本冲突与重复请求。

新增 **35,000 笔 SBA 真实放款分期研究**：2 万训练、5 千校准、1 万跨期测试，阶段间等待完整 24 个月记录内核销表现期；同一归一化借款人键只留一笔。四项批准时输入只在训练集拟合预处理。测试 89 个事件，1,000 个复核名额找到 26 个；保留校准后排名下降、逐年结果和 300 次配对月份重采样。官方原始 CSV 可完整重建冻结样本，安装包可离线重拟合；缺失的历史首次发布/修订记录不补造。

公开信用卡实验覆盖 30,000 条 UCI 记录、五次固定划分和四种方法，保留 12 万个模型分数、三档相同复核预算及无标签队列；全部来源、分数和下载包均可重新拟合核验。历史单一客群的随机切分与上面的合成时序验证分开解释，原德国信贷实验继续保留。

新增可编辑 CSV 输入样例与训练前诊断：按文件、行号定位多处错误，检查重复修订、决策时可用特征与成熟标签；诊断过程不修改输入、不训练模型。

早期监控可先用 `preflight --as-of` 检查历史成熟样本与当前可见申请，当前客群不需要违约标签；预检不训练模型，也不计算 PSI。

输入检查先诊断三项特征的时点覆盖与可见迟到，再按显式规则检查整体/月份的最低覆盖及样本数，并可比较五项输入分布。无需标签或拟合；保留事件、规则与逐项判定。失败策略仍能核验，宽松规则通过也不等于评分就绪。

[Source](https://github.com/dev-belly/CreditVintage) · [30,000-account comparison](https://dev-belly.github.io/CreditVintage/card-credit/) · [Dated-loan study](https://dev-belly.github.io/CreditVintage/sba-credit/) · [Checked release v0.8.0](https://github.com/dev-belly/CreditVintage/releases/tag/v0.8.0) · [Coverage policy](https://dev-belly.github.io/CreditVintage/feature-check/) · [Input distributions](https://dev-belly.github.io/CreditVintage/feature-monitor/) · [SQL analysis](https://dev-belly.github.io/CreditVintage/analysis/) · [Lineage](https://dev-belly.github.io/CreditVintage/lineage/)

<br />

<a href="https://github.com/dev-belly/PITBridge"><img src="assets/pitbridge-v3.svg" width="100%" alt="PITBridge — event and knowledge time, revision-safe snapshots, rolling financial features and independent Python replay." /></a>

**02 · PITBridge — Reconstruct what a decision could actually know.**

同时考虑事件、发布、入库时间与历史修订；构造决策时点快照和 7/30 天滚动特征。每个聚合值保留源记录成员，SQLite 结果与独立 Python 实现逐项核对。先试一张发票，再接 CSV 或可选的 pandas。

[Source](https://github.com/dev-belly/PITBridge) · [Run in browser](https://colab.research.google.com/github/dev-belly/PITBridge/blob/main/examples/decision_time.ipynb) · [Invoice / CSV example](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md) · [Snapshot report](https://dev-belly.github.io/PITBridge/) · [Rolling features](https://dev-belly.github.io/PITBridge/rolling/)

<br />

<a href="https://github.com/dev-belly/StressAtlas"><img src="assets/stressatlas-v3.svg" width="100%" alt="StressAtlas — correlated defaults, discrete-tail VaR and expected shortfall, sector attribution and paired bootstrap uncertainty. Diagram is schematic." /></a>

**03 · StressAtlas — A tail estimate should come with its uncertainty.**

用借款人层面的相关违约路径比较基准与压力情景；计算离散尾部 ES 和行业贡献，再用成对重采样检查估计精度。相同借款人的多笔贷款共享一次违约事件；不把平均损失的标准误当作 VaR 的置信区间。

[Source](https://github.com/dev-belly/StressAtlas) · [Stress report](https://dev-belly.github.io/StressAtlas/) · [Tail precision](https://dev-belly.github.io/StressAtlas/precision/) · [Method](https://github.com/dev-belly/StressAtlas/blob/main/docs/METHODOLOGY.md)

<sub>Examples identify their public-filing, public static-credit or synthetic inputs. Static and synthetic experiments do not establish future borrower risk or live investment performance.</sub>

## More financial systems

<details>
<summary><b>Explore financial statements, execution, accounting and audit tools</b></summary>

<br />

| Project | What to inspect | Result / walkthrough |
| :--- | :--- | :--- |
| [StatementTrace](https://github.com/dev-belly/StatementTrace) | Public filings → availability cutoff → exact fiscal periods → financial metrics | [Live report](https://dev-belly.github.io/StatementTrace/) · [SEC source ledger](https://github.com/dev-belly/StatementTrace/blob/main/docs/SOURCES.md) |
| [NetworkClear](https://github.com/dev-belly/NetworkClear) | Counterparty shocks, exact debt clearing and outside-loss reconciliation | [Live report](https://dev-belly.github.io/NetworkClear/) · [Clearing method](https://github.com/dev-belly/NetworkClear/blob/main/docs/METHODOLOGY.md) |
| [AlphaForge](https://github.com/dev-belly/alphaforge) | Factor signals, walk-forward validation, portfolio constraints and costs | [Real-price comparison](https://github.com/dev-belly/alphaforge/blob/main/docs/research-comparison.md) · [Synthetic sample run](https://dev-belly.github.io/alphaforge/sample-run/) |
| [TradeForge](https://github.com/dev-belly/TradeForge) | C++ execution events checked against an independent Python reference | [Public-quote matching case](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md) · [Synthetic demo](https://github.com/dev-belly/TradeForge#sixty-second-tour) |
| [ControlTrace](https://github.com/dev-belly/ControlTrace) | Audit conclusions tied to the current evidence version | [Case study](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md) |
| [AuditLens](https://github.com/dev-belly/AuditLens) | Anomaly detection → an explainable review item | [Workpapers](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports) |
| [LedgerX](https://github.com/dev-belly/LedgerX) | Trading fills, accounting entries and valuation reconciled exactly | [Valuation example](https://github.com/dev-belly/LedgerX/blob/main/examples/valuation.json) |

</details>

**Know the data boundary:** StatementTrace uses curated public-filing excerpts; AlphaForge's separate comparison uses historical mirrored equity prices but incomplete membership/publication histories; TradeForge's public depth capture powers hypothetical fills. CreditVintage's dated-event demonstrations, StressAtlas and NetworkClear remain synthetic. Its SBA study is retrospective funding-cohort validation with absent historical publication/revision records. UCI card and German experiments retain their distinct native targets; random customer splits do not establish future-period performance. [Read the matching assumptions](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md) before quoting a market cost.

<img src="assets/stack-v3.svg" width="100%" alt="Core tools: Python, SQL, C++20, scikit-learn, LightGBM and NumPy." />

## Research in public

<details>
<summary><b>Inspect recent changes and their validation</b></summary>

<br />

Recent changes connect the demonstrations to concrete operational checks:

- **Observed loans across time:** [CreditVintage #35](https://github.com/dev-belly/CreditVintage/pull/35) reconstructs 35,000 loans from two complete official SBA CSVs, retains mature calendar gaps and separate calibration, and refits its full portable evidence. All methods, both test years and weaker calibrated ranking remain visible. [Run it](START_HERE.md#creditvintage-validate-observed-loans-across-time) · [Method and limits](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md).

- **Check explicit coverage rules:** [CreditVintage #34](https://github.com/dev-belly/CreditVintage/pull/34) checks retained diagnostics with exact overall/monthly counts, preserves failed/insufficient rules and separates policy outcome from evidence replay. An independently saved digest can pin approved rules. [Run it](START_HERE.md#creditvintage-check-explicit-coverage-conditions) · [Validation](PROJECT_REVIEW.md#explicit-coverage-acceptance--2026-10-25).

- **Diagnose unavailable inputs:** [CreditVintage #33](https://github.com/dev-belly/CreditVintage/pull/33) keeps every expected feature slot and separates visible late arrivals, post-decision observations and still-unseen events. Its evidence replays without outcomes or fitting, while strict scoring/distribution gates retain their missing-feature failures. [Run it](START_HERE.md#creditvintage-diagnose-missing-decision-time-features) · [Validation](PROJECT_REVIEW.md#decision-time-feature-coverage--2026-10-25).

- **Explain input changes before fitting:** [CreditVintage #32](https://github.com/dev-belly/CreditVintage/pull/32) adds two-table feature monitoring without any outcome file: four numeric KS distances, segment total variation, monthly sample gates and replay from retained decision-time events. [Run it](START_HERE.md#creditvintage-inspect-input-distributions-without-labels) · [Validation and scope](PROJECT_REVIEW.md#input-distribution-monitoring--2026-10-24).

- **Check early monitoring before training:** [CreditVintage #28](https://github.com/dev-belly/CreditVintage/pull/28) adds model-free `preflight --as-of`: mature historical populations, a visible label-free current cohort and explicit future-application counts. [Exact source and validation](PROJECT_REVIEW.md#monitoring-input-readiness--2026-10-23) retain the 273-test result and installed-wheel replay.

- **Consistent calendar inputs:** [CreditVintage #26](https://github.com/dev-belly/CreditVintage/pull/26) applies the same `YYYY-MM-DD` contract to CSV diagnostics, monitoring cutoffs and saved report evidence. The fix is included in the [checked v0.3.2 release](https://github.com/dev-belly/CreditVintage/releases/tag/v0.3.2); [validation and upgrade notes](PROJECT_REVIEW.md#checked-calendar-patch-release--2026-10-22) connect installation to its evidence.

- **Observed data, explicitly bounded:** [AlphaForge #4](https://github.com/dev-belly/alphaforge/pull/4) retains all 22 historical-price comparison cases and independently rechecks reported returns; [TradeForge #14](https://github.com/dev-belly/TradeForge/pull/14) replays public quote packets offline into 18 hypothetical matching/fee/latency scenarios. Neither proves a tradable edge or actual order fills.

- **Installed packages:** [CreditVintage #12](https://github.com/dev-belly/CreditVintage/pull/12) and [PITBridge #13](https://github.com/dev-belly/PITBridge/pull/13) replay built wheels in clean environments outside their source trees on Linux and Windows.
- **Credit review:** [CreditVintage #11](https://github.com/dev-belly/CreditVintage/pull/11) adds ownership, recorded reasons and retry protection; [#14](https://github.com/dev-belly/CreditVintage/pull/14) delivers evidence that replays without the database.
- **Failure paths:** [LedgerX #4](https://github.com/dev-belly/LedgerX/pull/4) stages whole retriable batches; [AuditLens #5](https://github.com/dev-belly/AuditLens/pull/5) refuses conflicting master records; [WeCom #3](https://github.com/dev-belly/wecom-agent-platform/pull/3) keeps queries on one index generation.
- **Evidence and report access:** [ControlTrace #5](https://github.com/dev-belly/ControlTrace/pull/5) binds conclusions to evidence versions; [TradeForge #13](https://github.com/dev-belly/TradeForge/pull/13) confines report requests to the configured directory.

[Build history](CHANGELOG.md) · [Validation evidence and exact commits](PROJECT_REVIEW.md) · [Business walkthrough and interview practice](INTERVIEW_PLAYBOOK.zh-CN.md)

</details>

准备面试可先用 [60 秒讲解与五个追问](面试速讲卡.zh-CN.md)，再沿实际操作、失败场景和代码展开。

<details>
<summary><b>Experiments & earlier work</b></summary>

<br />

| Experiment | What it explores |
| :--- | :--- |
| [Investor Network GNN](https://github.com/dev-belly/investor-network-gnn) | Graph ablations and [three-seed saved predictions](https://github.com/dev-belly/investor-network-gnn/tree/main/experiments/2026-09-17). |
| [High-dimensional Causal Allocation Lab](https://github.com/dev-belly/highdim-causal-allocation-lab) | Simulated causal estimation and robust allocation; [interactive example](https://dev-belly.github.io/highdim-causal-allocation-lab/). |
| [Interval Financial Risk](https://github.com/dev-belly/interval-financial-risk) | A [retained negative result](https://dev-belly.github.io/interval-financial-risk/): distributional features reduced AUC in this synthetic experiment. |
| [FactorLab](https://github.com/dev-belly/ashare-multifactor-research) | A-share factor evaluation and purged validation; [中文文档](https://github.com/dev-belly/ashare-multifactor-research/blob/main/README.zh-CN.md). |
| [WeCom Agent Platform](https://github.com/dev-belly/wecom-agent-platform) | Contract filtering and currency-aware holding totals; [offline business trial](https://github.com/dev-belly/wecom-agent-platform/blob/main/docs/business-workflow.md). |
| [Personal AI Chat](https://github.com/dev-belly/personal-ai-chat) | Local chat plus a separately configured private model connection. |

Earlier builds: [Digital Craftsman](https://github.com/dev-belly/digital-craftsman) · [Ranxin](https://github.com/dev-belly/ranxin-mini-program) · [Goose Leg Auntie](https://github.com/dev-belly/goose-leg-auntie-site).

</details>

---

[Start here](START_HERE.md) · [Project evidence](PROJECT_BRIEFS.md) · [Business walkthrough](INTERVIEW_PLAYBOOK.zh-CN.md) · [Open-source roadmap](OPEN_SOURCE_ROADMAP.zh-CN.md) · [Portfolio review](PROJECT_REVIEW.md) · [Project adoption](PROJECT_ADOPTION.zh-CN.md) · [Design references](PROFILE_REFERENCES.md) · [Profile CI](https://github.com/dev-belly/dev-belly/actions/workflows/ci.yml)

<sub>Financial questions. Runnable code. Evidence you can inspect.</sub>
