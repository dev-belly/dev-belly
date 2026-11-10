<div align="center">
  <img src="assets/profile-signal-v3.svg" width="100%" alt="dev-belly — Follow the numbers. Financial research built with Python and SQL. CUFE data science." />
  <br /><br />
  <a href="https://dev-belly.github.io/StatementTrace/cashflow/"><b>READ A STUDY</b></a> &nbsp; / &nbsp;
  <a href="FOR_RECRUITERS.md"><b>FOR RECRUITERS · 招聘速览</b></a> &nbsp; / &nbsp;
  <a href="CATALOG.md"><b>PROJECT INDEX</b></a>
</div>

<br />

I'm **dev-belly**, studying **Data Science & Big Data Technology at Central University of Finance and Economics (CUFE), Class of 2029**.
I use **Python, SQL and statistics** to turn financial questions into research someone else can inspect and rerun.

中央财经大学数据科学本科在读，关注**金融数据分析、企业研究与量化研究方法**。
希望把数据整理、统计分析和研究实现能力用在券商、基金与研究团队的实习中。

## Selected work

Three projects, three questions: **understand the business → evaluate a model → reconstruct the data behind a decision**.

<a href="https://github.com/dev-belly/StatementTrace"><img src="assets/statementtrace-v4.svg" width="100%" alt="StatementTrace — compare profit and free cash flow using 24 public filing facts across Apple, Microsoft and Alphabet; Python and SQL arithmetic." /></a>

**Why can profit rise much faster than free cash flow?** A historical FY2023–FY2024 study compares three issuers using 24 curated SEC filing facts. Alphabet's profit grew **35.67%**, while FCF grew **4.70%**; the report reconciles the operating cash-flow increase with higher cash capex.

[Read the report](https://dev-belly.github.io/StatementTrace/cashflow/) · [中文研究简报](https://github.com/dev-belly/StatementTrace/blob/main/docs/CASHFLOW_STUDY.zh-CN.md) · [24 source facts](https://github.com/dev-belly/StatementTrace/blob/main/examples/cashflow/source_facts.csv) · [SQL](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/data/cashflow_compare.sql)

<sub>Historical case, filed-date cutoff 2025-02-05. Different fiscal windows; Apple's FY2023 has 53 weeks. Compare each issuer with its own prior year. FCF is CFO minus cash capex.</sub>

<a href="https://github.com/dev-belly/CreditVintage"><img src="assets/creditvintage-v3.svg" width="100%" alt="CreditVintage — 35,000 observed SBA loans, later funding cohorts, probability calibration and fixed review capacity." /></a>

**Does a better probability estimate make a better review queue?** On **35,000 observed SBA loans**, separate training, calibration and later funding cohorts expose a tradeoff: calibration can improve probability error while weakening ranking and event capture at the same review capacity. Saved predictions support independent SQL analysis.

[Compare review budgets](https://dev-belly.github.io/CreditVintage/sba-brief/) · [Study and assumptions](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md) · [SQL exercise](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_REVIEW_SQL.md)

<sub>Retrospective funding-cohort research with mature outcome windows. The final source snapshot lacks historical publication and revision records.</sub>

<a href="https://github.com/dev-belly/PITBridge"><img src="assets/pitbridge-v3.svg" width="100%" alt="PITBridge — reconstruct the facts available at a decision, with publication time, ingestion time and revisions." /></a>

**Was that information available when the decision was made?** Change one invoice's arrival time in the browser, inspect the selected record, then download the scenario and replay it in Python. The implementation separates event time from knowledge time and checks SQL against a separate Python path.

[Try one timestamp](https://dev-belly.github.io/PITBridge/try/) · [Replay the scenario](START_HERE.md#download-and-replay-your-browser-scenario) · [Implementation](https://github.com/dev-belly/PITBridge/blob/main/src/pitbridge/core.py)

<sub>Small synthetic invoice/event examples make the temporal rules visible.</sub>

## Research bench

| Project | What to inspect | Current evidence |
| :--- | :--- | :--- |
| [AlphaForge](https://github.com/dev-belly/alphaforge) | Factor evaluation, walk-forward splits, portfolio constraints and costs | [Small evaluation counterexample](INTERVIEW_PLAYBOOK.zh-CN.md#共同样本与分组口径). Archived backtests await refitting under the corrected trading-session split protocol. |
| [TradeForge](https://github.com/dev-belly/TradeForge) | C++20 order-book logic and Python execution analysis | [Public-market case](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md). Public depth supports hypothetical execution, not observed fills. |
| [StressAtlas](https://github.com/dev-belly/StressAtlas) | Portfolio tail loss, attribution and simulation uncertainty | [Methods](https://github.com/dev-belly/StressAtlas/blob/main/docs/METHODOLOGY.md). Synthetic portfolios with stated scenario assumptions. |

<img src="assets/stack-v3.svg" width="100%" alt="Working tools: Python, SQL, statistics, scikit-learn; C++20 for execution research." />

## Explore further

[All 19 projects and their data scope](CATALOG.md) · [Run a project](START_HERE.md) · [Project briefs](PROJECT_BRIEFS.md) · [Current priorities](OPEN_SOURCE_ROADMAP.zh-CN.md)

<details>
<summary>Implementation history and review notes</summary>

[Validation archive](PROJECT_REVIEW.md) · [Changelog](CHANGELOG.md) · [Interview workbook](INTERVIEW_PLAYBOOK.zh-CN.md) · [Contribution guide](CONTRIBUTING.md)

</details>
