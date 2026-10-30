<div align="center">
  <img src="assets/profile-signal-v3.svg" width="100%" alt="dev-belly — Finance. Data. Evidence. CUFE data science student building inspectable financial systems." />
  <br /><br />
  <a href="https://dev-belly.github.io/PITBridge/try/"><b>TRY LIVE</b></a> &nbsp; / &nbsp;
  <a href="https://dev-belly.github.io/CreditVintage/sba-brief/en/"><b>CREDIT STUDY</b></a> &nbsp; / &nbsp;
  <a href="FOR_RECRUITERS.md"><b>FOR RECRUITERS</b></a> &nbsp; / &nbsp;
  <a href="PROJECT_BRIEFS.md"><b>RESULTS &amp; CODE</b></a> &nbsp; / &nbsp;
  <a href="#research-in-public"><b>RECENT WORK</b></a>
</div>

<br />

I'm **dev-belly**, a **Data Science & Big Data Technology** student at **Central University of Finance and Economics**. I build tools for credit risk, financial data analysis and quantitative research.

**Open to internships in data analysis, credit risk and financial data engineering.**
[招聘速览：按岗位查看项目、结果与代码](FOR_RECRUITERS.md) · [Try one invoice without sign-in](https://dev-belly.github.io/PITBridge/try/).

把金融问题拆成能运行、能检验、能追溯的系统：从 SQL 客群分析和人工复核，到决策时点的数据、财报指标与组合风险。

**New here?** [Change one invoice timestamp](START_HERE.md#try-in-your-browser), [compare fixed credit review budgets](START_HERE.md#compare-credit-review-budgets), [install a project from an empty directory](START_HERE.md#try-a-project), or [review a business decision and its code](START_HERE.md#review-the-work). 新访客可先在浏览器核对三次固定决策，再改一个时间；招聘与面试审阅可沿业务问题、结果和代码查看。

## Start with a business question

**Pick a route:** credit & data → **CreditVintage / PITBridge**; quantitative research → **AlphaForge / TradeForge / StressAtlas**; accounting & audit → **AuditLens / ControlTrace / LedgerX**. The [complete project directory](CATALOG.md) connects all public projects to their README, methods, demos and data boundaries.

| Question | Open the result | Follow the code |
| :--- | :--- | :--- |
| Does a model hold up on later funding cohorts? | [Interactive SBA comparison](https://dev-belly.github.io/CreditVintage/sba-brief/en/) · [Full report](https://dev-belly.github.io/CreditVintage/sba-credit/) | [Training and refitting](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/sba_credit.py) · [Protocol](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md) |
| Which credit cohorts need attention? | [SQL credit analysis](https://dev-belly.github.io/CreditVintage/analysis/) | [Cohort SQL](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/business_groups.sql) · [Review workflow](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_WORKFLOW.md) |
| Do the inputs meet explicit coverage rules? | [Policy check](https://dev-belly.github.io/CreditVintage/feature-check/) · [Coverage and delays](https://dev-belly.github.io/CreditVintage/feature-quality/) | [Rules and replay](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/feature_policy.py) · [Contract](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_POLICY.md) |
| What could a decision know before a late correction arrived? | [Run three decisions in your browser](https://dev-belly.github.io/PITBridge/try/) | [Three-decision example](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md) |
| How does clustered default change portfolio losses? | [Stress report](https://dev-belly.github.io/StressAtlas/) | [Tail math and uncertainty](https://github.com/dev-belly/StressAtlas/blob/main/docs/METHODOLOGY.md) |

**A useful result includes its limits.** The [SBA study](https://dev-belly.github.io/CreditVintage/sba-credit/) uses real funding dates and a native 24-month recorded charge-off target. Logistic AUC is 0.6723 on 10,000 later loans; calibration improves Brier while reducing ranking performance. The final snapshot cannot establish historical first-publication times. Separate UCI static and synthetic event experiments retain their own targets. [Project evidence](PROJECT_BRIEFS.md) connects each claim to inputs, code and validation.

## Flagship projects

<a href="https://github.com/dev-belly/CreditVintage"><img src="assets/creditvintage-v3.svg" width="100%" alt="CreditVintage — 35,000 observed SBA loans across separate funding cohorts and mature 24-month charge-off horizons; retrospective validation." /></a>

**01 · CreditVintage — Credit analysis with evidence you can refit.**

**35,000 笔 SBA 真实放款跨期研究**：2 万训练、5 千校准、1 万测试，阶段间等待完整 24 月记录内核销表现期。四项批准时输入只在训练集拟合预处理；测试 AUC 0.6723，同 1,000 个复核名额找到 26/89 个事件。保留校准后排名下降、逐年结果和 300 次配对月份重采样；原始官方 CSV 可完整重建，安装包可离线重拟合。

最终快照没有历史首次发布或特征修订记录，因此作为回溯放款研究；原合成时点控制实验和静态 UCI 目标分开解释。核验成功不代表生产部署或避免损失。

[Try in English](https://dev-belly.github.io/CreditVintage/sba-brief/en/) · [中文交互速览](https://dev-belly.github.io/CreditVintage/sba-brief/) · [Observed-loan report](https://dev-belly.github.io/CreditVintage/sba-credit/) · [Run it](START_HERE.md#creditvintage-validate-observed-loans-across-time) · [Source](https://github.com/dev-belly/CreditVintage) · [Checked v0.8.1](https://github.com/dev-belly/CreditVintage/releases/tag/v0.8.1)

<details>
<summary>More experiments: static credit, input quality and human review</summary>

公开信用卡实验覆盖 30,000 条 UCI 记录、五次固定划分和四种方法，保留 12 万个模型分数、三档相同复核预算及无标签队列；历史单一客群的随机切分与 SBA 放款分期研究及合成时序验证分开解释。

合成事件流程用 SQL 按放款月份和客群对照预测与成熟事件；固定容量队列不含未来标签。SQLite 复核记录认领、结案、理由和材料引用，并处理并发版本冲突与重复请求。

可编辑 CSV 样例在训练前按文件、行号诊断；早期预检无需当前结果标签。两表输入诊断覆盖、迟到和分布，显式整体/月度规则保留失败与证据不足；宽松规则通过仍不等于评分就绪。

[30,000-account comparison](https://dev-belly.github.io/CreditVintage/card-credit/) · [Coverage policy](https://dev-belly.github.io/CreditVintage/feature-check/) · [Input distributions](https://dev-belly.github.io/CreditVintage/feature-monitor/) · [SQL analysis](https://dev-belly.github.io/CreditVintage/analysis/) · [Synthetic lineage](https://dev-belly.github.io/CreditVintage/lineage/)

</details>

<br />

<a href="https://github.com/dev-belly/PITBridge"><img src="assets/pitbridge-v3.svg" width="100%" alt="PITBridge — event and knowledge time, revision-safe snapshots, rolling financial features and independent Python replay." /></a>

**02 · PITBridge — Reconstruct what a decision could actually know.**

同时考虑事件、发布、入库时间与历史修订；构造决策时点快照和 7/30 天滚动特征。每个聚合值保留源记录成员，SQLite 结果与独立 Python 实现逐项核对。先试一张发票，再接 CSV 或可选的 pandas。

[Source](https://github.com/dev-belly/PITBridge) · [Checked v0.2.2](https://github.com/dev-belly/PITBridge/releases/tag/v0.2.2) · [Editable CSV first run](START_HERE.md#pitbridge-create-editable-csv-inputs) · [Run in browser](https://dev-belly.github.io/PITBridge/try/) · [Invoice / CSV example](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md) · [Snapshot report](https://dev-belly.github.io/PITBridge/) · [Rolling features](https://dev-belly.github.io/PITBridge/rolling/)

<br />

<a href="https://github.com/dev-belly/StressAtlas"><img src="assets/stressatlas-v3.svg" width="100%" alt="StressAtlas — correlated defaults, discrete-tail VaR and expected shortfall, sector attribution and paired bootstrap uncertainty. Diagram is schematic." /></a>

**03 · StressAtlas — A tail estimate should come with its uncertainty.**

用借款人层面的相关违约路径比较基准与压力情景；计算离散尾部 ES 和行业贡献，再用成对重采样检查估计精度。相同借款人的多笔贷款共享一次违约事件；不把平均损失的标准误当作 VaR 的置信区间。

可选流式驱动保留相同随机指纹和报告字节。本地 50,000 路径、400 个借款人、3 个合成情景的进程峰值内存从约 352 MiB 降至 140 MiB，用时从 4.58 秒增至 5.44 秒；完整损失路径仍占内存。[运行与复现](START_HERE.md#stressatlas-replay-with-less-driver-memory)。

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
| [AlphaForge](https://github.com/dev-belly/alphaforge) | Trading-session splits, rolling returns and factor covariance | [Archived comparison and protocol correction](https://github.com/dev-belly/alphaforge/blob/main/docs/research-comparison.md) · [Synthetic sample run](https://dev-belly.github.io/alphaforge/sample-run/) |
| [TradeForge](https://github.com/dev-belly/TradeForge) | C++ execution events checked against an independent Python reference | [Public-quote matching case](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md) · [Synthetic demo](https://github.com/dev-belly/TradeForge#sixty-second-tour) |
| [ControlTrace](https://github.com/dev-belly/ControlTrace) | Audit conclusions tied to the current evidence version | [Case study](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md) |
| [AuditLens](https://github.com/dev-belly/AuditLens) | Anomaly detection → an explainable review item | [Workpapers](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports) |
| [LedgerX](https://github.com/dev-belly/LedgerX) | Trading fills, accounting entries and valuation reconciled exactly | [Valuation example](https://github.com/dev-belly/LedgerX/blob/main/examples/valuation.json) |

</details>

**Know the data boundary:** StatementTrace uses curated public-filing excerpts. AlphaForge's archived price and synthetic runs used calendar-day buffers for trading-session labels; they have not been refitted under the corrected splitter and do not establish leakage-free out-of-sample performance. Historical membership/publication records are also incomplete. TradeForge's public depth capture powers hypothetical fills. CreditVintage's dated-event demonstrations, StressAtlas and NetworkClear remain synthetic. Its SBA study is retrospective funding-cohort validation with absent historical publication/revision records. UCI card and German experiments retain their distinct native targets; random customer splits do not establish future-period performance. [Read the matching assumptions](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md) before quoting a market cost.

<img src="assets/stack-v3.svg" width="100%" alt="Core tools: Python, SQL, C++20, scikit-learn, LightGBM and NumPy." />

## Research in public

<details>
<summary><b>Inspect recent changes and their validation</b></summary>

<br />

Recent changes connect the demonstrations to concrete operational checks:

- **Editable installed inputs · 2026-10-30:** [generate three CSV tables, edit an arrival and replay the result](START_HERE.md#pitbridge-create-editable-csv-inputs) with the checked v0.2.2 wheel. [Validation and source identity](PROJECT_REVIEW.md#editable-csv-first-runs-from-the-wheel--2026-10-30).

- **Bilingual credit study · 2026-10-29:** [English](https://dev-belly.github.io/CreditVintage/sba-brief/en/) and [中文](https://dev-belly.github.io/CreditVintage/sba-brief/) share verified results and preserve the chosen review capacity when changing language. [Checks and source identity](PROJECT_REVIEW.md#english-and-chinese-credit-study-entry--2026-10-29).

- **Input boundaries · 2026-10-28:** [precision and numeric validation](PROJECT_REVIEW.md#temporal-precision-and-credit-input-boundaries--2026-10-28) rejects timestamp truncation into a decision cutoff and unsupported credit numbers, connects the fixed source to the integration and notebook, and preserves replay of the published synthetic evidence.

- **Maintenance and application repairs · 2026-10-27:** [validation record](PROJECT_REVIEW.md#repository-maintenance-and-application-repairs--2026-10-27) connects fixed Action source commits with invalid-session rejection, recoverable initialization, consistent pagination and a dated-source review.

- **Financial correctness · 2026-10-27:** close six concrete failures across [AlphaForge #5–7](https://github.com/dev-belly/alphaforge/pull/5), [AuditLens #9](https://github.com/dev-belly/AuditLens/pull/9), [ControlTrace #8](https://github.com/dev-belly/ControlTrace/pull/8) and [TradeForge #21](https://github.com/dev-belly/TradeForge/pull/21): trading-session separation, complete rolling windows, rectangular factor exposures, decimal digit boundaries, missing approval identities and rejected-fill rollback. [Changes and checks](PROJECT_REVIEW.md#financial-correctness-repairs--2026-10-27) · [Practice the counterexamples](INTERVIEW_PLAYBOOK.zh-CN.md#用四个修复练习追问).

- **Observed loans across time:** [CreditVintage #35](https://github.com/dev-belly/CreditVintage/pull/35) reconstructs 35,000 loans from two complete official SBA CSVs, retains mature calendar gaps and separate calibration, and refits its full portable evidence. All methods, both test years and weaker calibrated ranking remain visible. [Run it](START_HERE.md#creditvintage-validate-observed-loans-across-time) · [Method and limits](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md).

- **Check explicit coverage rules:** [CreditVintage #34](https://github.com/dev-belly/CreditVintage/pull/34) checks retained diagnostics with exact overall/monthly counts, preserves failed/insufficient rules and separates policy outcome from evidence replay. An independently saved digest can pin approved rules. [Run it](START_HERE.md#creditvintage-check-explicit-coverage-conditions) · [Validation](PROJECT_REVIEW.md#explicit-coverage-acceptance--2026-10-25).

- **Diagnose unavailable inputs:** [CreditVintage #33](https://github.com/dev-belly/CreditVintage/pull/33) keeps every expected feature slot and separates visible late arrivals, post-decision observations and still-unseen events. Its evidence replays without outcomes or fitting, while strict scoring/distribution gates retain their missing-feature failures. [Run it](START_HERE.md#creditvintage-diagnose-missing-decision-time-features) · [Validation](PROJECT_REVIEW.md#decision-time-feature-coverage--2026-10-25).

- **Explain input changes before fitting:** [CreditVintage #32](https://github.com/dev-belly/CreditVintage/pull/32) adds two-table feature monitoring without any outcome file: four numeric KS distances, segment total variation, monthly sample gates and replay from retained decision-time events. [Run it](START_HERE.md#creditvintage-inspect-input-distributions-without-labels) · [Validation and scope](PROJECT_REVIEW.md#input-distribution-monitoring--2026-10-24).

- **Check early monitoring before training:** [CreditVintage #28](https://github.com/dev-belly/CreditVintage/pull/28) adds model-free `preflight --as-of`: mature historical populations, a visible label-free current cohort and explicit future-application counts. [Exact source and validation](PROJECT_REVIEW.md#monitoring-input-readiness--2026-10-23) retain the 273-test result and installed-wheel replay.

- **Consistent calendar inputs:** [CreditVintage #26](https://github.com/dev-belly/CreditVintage/pull/26) applies the same `YYYY-MM-DD` contract to CSV diagnostics, monitoring cutoffs and saved report evidence. The fix is included in the [checked v0.3.2 release](https://github.com/dev-belly/CreditVintage/releases/tag/v0.3.2); [validation and upgrade notes](PROJECT_REVIEW.md#checked-calendar-patch-release--2026-10-22) connect installation to its evidence.

- **Observed data, explicitly bounded:** [AlphaForge #4](https://github.com/dev-belly/alphaforge/pull/4) retains all 22 historical-price comparison cases and independently rechecks reported returns. Its [split-protocol correction](https://github.com/dev-belly/alphaforge/pull/5) leaves those figures archived pending refitting. [TradeForge #14](https://github.com/dev-belly/TradeForge/pull/14) replays public quote packets offline into 18 hypothetical matching/fee/latency scenarios. Neither proves a tradable edge or actual order fills.

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

想试用或参与：先选[项目目录](CATALOG.md)，运行问题到对应仓库反馈；主页导航、文字或证据链接问题可用[主页问题表单](https://github.com/dev-belly/dev-belly/issues/new/choose)。[贡献说明](CONTRIBUTING.md) · [安全报告说明](SECURITY.md)。

Follow **@dev-belly** for runnable financial-data tools and small studies with inspectable evidence.
If a tool is useful to you, star its repository to keep it handy; a concrete trial report helps shape the next improvement.

[Start here](START_HERE.md) · [All projects](CATALOG.md) · [Project evidence](PROJECT_BRIEFS.md) · [Business walkthrough](INTERVIEW_PLAYBOOK.zh-CN.md) · [Open-source roadmap](OPEN_SOURCE_ROADMAP.zh-CN.md) · [Portfolio review](PROJECT_REVIEW.md) · [Project adoption](PROJECT_ADOPTION.zh-CN.md) · [Design references](PROFILE_REFERENCES.md) · [Profile CI](https://github.com/dev-belly/dev-belly/actions/workflows/ci.yml)

<sub>Financial questions. Runnable code. Evidence you can inspect.</sub>
