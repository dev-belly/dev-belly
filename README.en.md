# dev-belly

**Connect interfaces, APIs and data in runnable applications.**

CUFE undergraduate · Data Science & Big Data Technology · Current focus: full-stack development

[中文](README.md) · [Engineering overview](FOR_RECRUITERS.md) · [Run a project](START_HERE.md) · [Project index](CATALOG.md)

## Applications and APIs first

Working toward a **summer 2027 development internship**, currently studying HTML, CSS and JavaScript.
Explore the existing implementations, setup instructions and verification paths below.

| Project | Implemented behavior | Inspect |
| --- | --- | --- |
| **[Personal AI Chat](https://github.com/dev-belly/personal-ai-chat)** | Next.js 16.4 / React 19.3 / TypeScript 7 / AI SDK 7, with Dexie history and unsaved-work prompts, Streamdown / Shiki streaming Markdown, and two provider protocols | [Setup](https://github.com/dev-belly/personal-ai-chat/blob/main/README.md) · [Local history](https://github.com/dev-belly/personal-ai-chat/blob/main/docs/LOCAL_CONVERSATIONS.zh-CN.md) · [Architecture](https://github.com/dev-belly/personal-ai-chat/blob/main/docs/ARCHITECTURE.zh-CN.md) |
| **[StatementTrace](https://github.com/dev-belly/StatementTrace)** | Filter a verified financial snapshot by issuer and year, then trace free cash flow to its original filings through a FastAPI-backed explorer | [Online explorer](https://dev-belly.github.io/StatementTrace/explorer/) · [Run locally](START_HERE.md#query-the-verified-financial-api) · [Explorer code](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/data/explorer/explorer.js) |
| **[CreditVintage](https://github.com/dev-belly/CreditVintage)** | Claim, resolve and reopen cases in a browser with SQLite event history and version checks for concurrent edits | [Online case demo](https://dev-belly.github.io/CreditVintage/review/) · [Run locally](START_HERE.md#creditvintage-review-workbench) · [Review code](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/reviews.py) |
| **[WeCom Agent](https://github.com/dev-belly/wecom-agent-platform)** | React contract filters and FastAPI pagination with index-version checks and source page references | [Live demo](https://dev-belly.github.io/wecom-agent-platform/?view=contracts) · [API and tests](FOR_RECRUITERS.md#复核对账与合同查询) |
| **[PITBridge](https://github.com/dev-belly/PITBridge)** | Browser interaction, URL state, JSON download and independent Python / SQLite replay | [Try it](https://dev-belly.github.io/PITBridge/try/) · [Replay](START_HERE.md#download-and-replay-your-browser-scenario) |

Personal AI Chat starts with fixed local replies. Find the LedgerX reconciliation setup in the [engineering overview](FOR_RECRUITERS.md#复核对账与合同查询).

## Selected work

### [StatementTrace](https://github.com/dev-belly/StatementTrace)

**Why can profit rise much faster than free cash flow?**

Compare Apple, Microsoft and Alphabet across six issuer-years, using 24 curated SEC filing facts. Alphabet's profit grew **35.67%**, while FCF grew **4.70%**. An exact cash-flow bridge explains the contributions of operating cash flow and cash capex.

Inspect source lineage, fiscal windows, exact values and Python/SQL arithmetic. Historical filed-date cutoff: 2025-02-05. Fiscal windows differ; FCF means CFO minus cash capex.

[Report](https://dev-belly.github.io/StatementTrace/cashflow/) · [Source facts](https://github.com/dev-belly/StatementTrace/blob/main/examples/cashflow/source_facts.csv) · [SQL](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/data/cashflow_compare.sql)

[Continue from profit to CFO](https://dev-belly.github.io/StatementTrace/cashflow/profit-bridge/en/): six reconciled issuer-years, tax/acquisition/lease boundaries, 116 selected values and eight explicit missing fields; 144 exact Python/SQLite checks.

### [CreditVintage](https://github.com/dev-belly/CreditVintage)

**Does a better probability estimate make a better review queue?**

On **35,000 observed SBA loans**, separate training, calibration and later funding cohorts expose a tradeoff between probability error, ranking and event capture at the same review capacity. Saved predictions support independent SQL analysis.

Retrospective funding-cohort research with mature outcome windows. The final source snapshot lacks historical publication and revision records.

[Compare budgets](https://dev-belly.github.io/CreditVintage/sba-brief/en/) · [Study](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md) · [SQL exercise](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_REVIEW_SQL.md)

### [PITBridge](https://github.com/dev-belly/PITBridge)

**Was that information available when the decision was made?**

Change an invoice's arrival time, inspect the selected revision, then download the scenario and replay it in Python. Separate event time from knowledge time; check SQLite against a separate Python path. Small synthetic examples make the temporal rules visible.

[Try one timestamp](https://dev-belly.github.io/PITBridge/try/) · [Replay a scenario](START_HERE.md#download-and-replay-your-browser-scenario) · [Implementation](https://github.com/dev-belly/PITBridge/blob/main/src/pitbridge/core.py)

## Engineering behind the research

| Route | Implemented behavior | Inspect |
| --- | --- | --- |
| Financial pipeline | Polars → Parquet → DuckDB → dbt; 138 exact field comparisons per SQL route | [Pipeline](https://github.com/dev-belly/StatementTrace/blob/main/docs/WAREHOUSE.zh-CN.md) |
| Typed research API | Six read-only FastAPI/Pydantic routes, bounded pagination and exact money strings | [API](https://github.com/dev-belly/StatementTrace/blob/main/docs/API.zh-CN.md) |
| Model comparison | Six audited session-split folds; five methods, three model seeds and two cost scenarios | [AlphaForge refit](https://dev-belly.github.io/alphaforge/research-comparison/) |
| Audit workflow | Explainable risk ordering and source-bound review workpapers | [AuditLens](https://github.com/dev-belly/AuditLens) |
| Execution analysis | C++20 order book, Python costs and a public-depth hypothetical matching case | [TradeForge](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md) |

The pipeline and local API use the same 24 curated facts. Arithmetic parity does not independently verify transcription; production scale is unmeasured.

<details>
<summary>Research bench and implementation history</summary>

- [CurveShift curve laboratory](https://dev-belly.github.io/StressAtlas/curveshift/): parallel DV01 neutrality can leave curve-shape risk.
- [AlphaForge session-split refit](https://dev-belly.github.io/alphaforge/experiments/real-sp500-session-v2/): the same 840,736-row supervised dataset, 22 retained cases and six audited training-label boundaries. Ridge's Sharpe is below the equal-weight baseline. Historical membership and publication-time limits remain explicit.
- [All 19 projects](CATALOG.md) · [First-run guide](START_HERE.md) · [Priorities](OPEN_SOURCE_ROADMAP.zh-CN.md).
- [Validation archive](PROJECT_REVIEW.md) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md).

</details>
