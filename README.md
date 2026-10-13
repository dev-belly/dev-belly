<div align="center">
  <img src="assets/profile-signal-v3.svg" width="100%" alt="dev-belly — Finance. Data. Evidence. CUFE data science student building inspectable financial systems." />
  <br /><br />
  <a href="#flagship-projects"><b>PROJECTS</b></a> &nbsp; / &nbsp;
  <a href="https://dev-belly.github.io/CreditVintage/analysis/"><b>LIVE DEMO</b></a> &nbsp; / &nbsp;
  <a href="PROJECT_BRIEFS.md"><b>RESULTS &amp; CODE</b></a> &nbsp; / &nbsp;
  <a href="#research-in-public"><b>RECENT WORK</b></a>
</div>

<br />

I'm **dev-belly**, a **Data Science & Big Data Technology** student at **Central University of Finance and Economics**. I build tools for credit risk, financial data analysis and quantitative research.

把金融问题拆成能运行、能检验、能追溯的系统：从 SQL 客群分析和人工复核，到决策时点的数据、财报指标与组合风险。

## Start with a business question

| Question | Open the result | Follow the code |
| :--- | :--- | :--- |
| Which credit cohorts need attention? | [SQL credit analysis](https://dev-belly.github.io/CreditVintage/analysis/) | [Cohort SQL](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/business_groups.sql) · [Review workflow](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_WORKFLOW.md) |
| What could a decision know before a late correction arrived? | [Source → prediction](https://dev-belly.github.io/CreditVintage/lineage/) | [Three-decision example](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md) |
| How does clustered default change portfolio losses? | [Stress report](https://dev-belly.github.io/StressAtlas/) | [Tail math and uncertainty](https://github.com/dev-belly/StressAtlas/blob/main/docs/METHODOLOGY.md) |

**A useful result includes its limits.** In CreditVintage's synthetic test, calibration worsened Brier score. The result stays in the report. [Project evidence](PROJECT_BRIEFS.md) connects each claim to its inputs, implementation and validation.

## Flagship projects

<a href="https://github.com/dev-belly/CreditVintage"><img src="assets/creditvintage-v3.svg" width="100%" alt="CreditVintage — chronological credit evaluation with separate training, calibration and holdout cohorts, plus source-record lineage." /></a>

**01 · CreditVintage — Credit analysis that reaches a review decision.**

训练、校准、测试分期隔离；标签等待完整表现期。SQL 按放款月份和客群对照风险事件与预测偏差；固定容量清单不含未来标签。SQLite 复核工作区记录认领、结案、理由和材料引用，并处理并发版本冲突与重复请求。

[Source](https://github.com/dev-belly/CreditVintage) · [SQL analysis](https://dev-belly.github.io/CreditVintage/analysis/) · [Risk report](https://dev-belly.github.io/CreditVintage/demo/) · [Lineage explorer](https://dev-belly.github.io/CreditVintage/lineage/) · [中文业务案例](https://github.com/dev-belly/CreditVintage/blob/main/docs/BUSINESS_CASE.md)

<br />

<a href="https://github.com/dev-belly/PITBridge"><img src="assets/pitbridge-v3.svg" width="100%" alt="PITBridge — event and knowledge time, revision-safe snapshots, rolling financial features and independent Python replay." /></a>

**02 · PITBridge — Reconstruct what a decision could actually know.**

同时考虑事件、发布、入库时间与历史修订；构造决策时点快照和 7/30 天滚动特征。每个聚合值保留源记录成员，SQLite 结果与独立 Python 实现逐项核对。先试一张发票，再接 CSV 或可选的 pandas。

[Source](https://github.com/dev-belly/PITBridge) · [Invoice / CSV example](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md) · [Snapshot report](https://dev-belly.github.io/PITBridge/) · [Rolling features](https://dev-belly.github.io/PITBridge/rolling/)

<br />

<a href="https://github.com/dev-belly/StressAtlas"><img src="assets/stressatlas-v3.svg" width="100%" alt="StressAtlas — correlated defaults, discrete-tail VaR and expected shortfall, sector attribution and paired bootstrap uncertainty. Diagram is schematic." /></a>

**03 · StressAtlas — A tail estimate should come with its uncertainty.**

用借款人层面的相关违约路径比较基准与压力情景；计算离散尾部 ES 和行业贡献，再用成对重采样检查估计精度。相同借款人的多笔贷款共享一次违约事件；不把平均损失的标准误当作 VaR 的置信区间。

[Source](https://github.com/dev-belly/StressAtlas) · [Stress report](https://dev-belly.github.io/StressAtlas/) · [Tail precision](https://dev-belly.github.io/StressAtlas/precision/) · [Method](https://github.com/dev-belly/StressAtlas/blob/main/docs/METHODOLOGY.md)

<sub>Examples identify their public-filing or synthetic inputs. Synthetic scores and loss scenarios demonstrate methods; they do not establish real borrower risk or live investment performance.</sub>

## More financial systems

| Project | What to inspect | Result / walkthrough |
| :--- | :--- | :--- |
| [StatementTrace](https://github.com/dev-belly/StatementTrace) | Public filings → availability cutoff → exact fiscal periods → financial metrics | [Live report](https://dev-belly.github.io/StatementTrace/) · [SEC source ledger](https://github.com/dev-belly/StatementTrace/blob/main/docs/SOURCES.md) |
| [NetworkClear](https://github.com/dev-belly/NetworkClear) | Counterparty shocks, exact debt clearing and outside-loss reconciliation | [Live report](https://dev-belly.github.io/NetworkClear/) · [Clearing method](https://github.com/dev-belly/NetworkClear/blob/main/docs/METHODOLOGY.md) |
| [AlphaForge](https://github.com/dev-belly/alphaforge) | Factor signals, walk-forward validation, portfolio constraints and costs | [Computed sample run](https://dev-belly.github.io/alphaforge/sample-run/) |
| [TradeForge](https://github.com/dev-belly/TradeForge) | C++ execution events checked against an independent Python reference | [60-second tour](https://github.com/dev-belly/TradeForge#sixty-second-tour) |
| [ControlTrace](https://github.com/dev-belly/ControlTrace) | Audit conclusions tied to the current evidence version | [Case study](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md) |
| [AuditLens](https://github.com/dev-belly/AuditLens) | Anomaly detection → an explainable review item | [Workpapers](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports) |
| [LedgerX](https://github.com/dev-belly/LedgerX) | Trading fills, accounting entries and valuation reconciled exactly | [Valuation example](https://github.com/dev-belly/LedgerX/blob/main/examples/valuation.json) |

StatementTrace uses a **curated public Apple filing excerpt**; NetworkClear uses **synthetic exposures**. Both have an offline CLI and inspectable CSV/JSON outputs.

<img src="assets/stack-v3.svg" width="100%" alt="Core tools: Python, SQL, C++20, scikit-learn, LightGBM and NumPy." />

## Research in public

Recent changes connect the demonstrations to concrete operational checks:

- **Installed packages:** [CreditVintage #12](https://github.com/dev-belly/CreditVintage/pull/12) and [PITBridge #13](https://github.com/dev-belly/PITBridge/pull/13) replay built wheels in clean environments outside their source trees on Linux and Windows.
- **Credit review:** [CreditVintage #11](https://github.com/dev-belly/CreditVintage/pull/11) adds case ownership, recorded reasons, version conflicts and retry protection.
- **Evidence and report access:** [ControlTrace #5](https://github.com/dev-belly/ControlTrace/pull/5) binds conclusions to evidence versions; [TradeForge #13](https://github.com/dev-belly/TradeForge/pull/13) confines report requests to the configured directory.

[Build history](CHANGELOG.md) · [Validation evidence and exact commits](PROJECT_REVIEW.md) · [Business walkthrough and interview practice](INTERVIEW_PLAYBOOK.zh-CN.md)

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

[Project evidence](PROJECT_BRIEFS.md) · [Business walkthrough](INTERVIEW_PLAYBOOK.zh-CN.md) · [Portfolio review](PROJECT_REVIEW.md) · [Project adoption](PROJECT_ADOPTION.zh-CN.md) · [Design references](PROFILE_REFERENCES.md) · [Profile CI](https://github.com/dev-belly/dev-belly/actions/workflows/ci.yml)

<sub>Financial questions. Runnable code. Evidence you can inspect.</sub>
