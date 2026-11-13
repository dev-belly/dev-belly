# dev-belly

**Follow the numbers.** Financial research built with Python and SQL.

[中文](README.md) · [Project index](CATALOG.md) · [Run a project](START_HERE.md)

## A hedge with a budget

**What should you trade after finding the risk?**

[CurveShift's hedge laboratory](https://dev-belly.github.io/StressAtlas/curveshift/hedge/) keeps a hypothetical $10m-face 7Y target fixed and optimizes four hedge maturities under face caps and entry costs. Change the budget, inspect residual key-rate risk and download the trades.

| Same hypothetical target | 2025 scenario ES, 97.5% | One-time entry cost |
| --- | ---: | ---: |
| Unhedged | $71,789.20 | $0 |
| $6m gross hedge-face budget | $29,039.70 | $1,200, separate |

QuantLib prices the cash flows; SciPy sparse matrices and HiGHS solve a 513-variable CVaR program. Fit on 504 changes through 2024, then evaluate fixed trades on 249 changes in 2025. ES is before the separate entry cost. Historical estimated curves and hypothetical bonds support a scenario study, not realized trading returns.

[Method](https://github.com/dev-belly/StressAtlas/blob/main/labs/curveshift/docs/HEDGING.zh-CN.md) · [Optimizer](https://github.com/dev-belly/StressAtlas/blob/main/labs/curveshift/src/curveshift/hedge.py) · [Saved decisions](https://github.com/dev-belly/StressAtlas/tree/main/labs/curveshift/reports/hedge)

## Selected work

### [StatementTrace](https://github.com/dev-belly/StatementTrace)

**Why can profit rise much faster than free cash flow?**

Compare Apple, Microsoft and Alphabet across six issuer-years, using 24 curated SEC filing facts. Alphabet's profit grew **35.67%**, while FCF grew **4.70%**. An exact cash-flow bridge explains the contributions of operating cash flow and cash capex.

Inspect source lineage, fiscal windows, exact values and Python/SQL arithmetic. Historical filed-date cutoff: 2025-02-05. Fiscal windows differ; FCF means CFO minus cash capex.

[Report](https://dev-belly.github.io/StatementTrace/cashflow/) · [Source facts](https://github.com/dev-belly/StatementTrace/blob/main/examples/cashflow/source_facts.csv) · [SQL](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/data/cashflow_compare.sql)

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
| Audit workflow | Explainable risk ordering and source-bound review workpapers | [AuditLens](https://github.com/dev-belly/AuditLens) |
| Execution analysis | C++20 order book, Python costs and a public-depth hypothetical matching case | [TradeForge](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md) |

The pipeline and local API use the same 24 curated facts. Arithmetic parity does not independently verify transcription; production scale is unmeasured.

<details>
<summary>Research bench and implementation history</summary>

- [CurveShift curve laboratory](https://dev-belly.github.io/StressAtlas/curveshift/): parallel DV01 neutrality can leave curve-shape risk.
- [AlphaForge evaluation method](https://github.com/dev-belly/alphaforge/blob/main/docs/modules/factor_research.md#evaluation-correction-2026-11-08): shared finite pairs, Rank-IC and trading-session splits. Archived returns await a corrected-protocol refit.
- [All 19 projects](CATALOG.md) · [First-run guide](START_HERE.md) · [Priorities](OPEN_SOURCE_ROADMAP.zh-CN.md).
- [Validation archive](PROJECT_REVIEW.md) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md).

</details>
