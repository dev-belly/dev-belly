# dev-belly

Building reproducible tools for **audit analytics, credit risk, and quantitative research**.

关注审计数据分析、信贷风险与量化研究，把方法做成可以运行、检查和复现的项目。

## Start with the role

| Interested in | Start here | Evidence to inspect |
| --- | --- | --- |
| Audit analytics / IT risk consulting | [AuditLens](https://github.com/dev-belly/AuditLens) · [ControlTrace](https://github.com/dev-belly/ControlTrace) | [Financial review workpaper](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports) · [IT control case](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md) · CI |
| Bank credit / model validation | [CreditVintage](https://github.com/dev-belly/CreditVintage) · [Interval Financial Risk](https://github.com/dev-belly/interval-financial-risk) | [Out-of-time report](https://dev-belly.github.io/CreditVintage/demo/) · [negative interval result](https://dev-belly.github.io/interval-financial-risk/) |
| Quant research / execution | [TradeForge](https://github.com/dev-belly/TradeForge) · [AlphaForge](https://github.com/dev-belly/alphaforge) · [LedgerX](https://github.com/dev-belly/LedgerX) | [Execution comparison](https://github.com/dev-belly/TradeForge#sixty-second-tour) · [backtest record](https://dev-belly.github.io/alphaforge/sample-run/) · [ledger reconciliation](https://github.com/dev-belly/LedgerX#point-in-time-portfolio-marks) |

[Project evidence and interview notes](PROJECT_BRIEFS.md) collects concise, source-linked results and the assumptions worth challenging. All published financial examples use synthetic data; none demonstrate production performance.

## Selected projects

### [AuditLens](https://github.com/dev-belly/AuditLens)

An audit analytics workflow for a synthetic 30,000-voucher ledger: nine review
procedures, Benford analysis, Isolation Forest, an explainable risk score, a
queryable SQLite warehouse, a six-page reviewer dashboard, and a budgeted
review workpaper with validated human outcomes.

**Start here:** [Source & setup](https://github.com/dev-belly/AuditLens#quickstart) ·
[Methodology and limitations](https://github.com/dev-belly/AuditLens/blob/main/docs/methodology.md) ·
[Review workpaper](https://github.com/dev-belly/AuditLens#audit-review-workpaper) ·
[Reproducible reports](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports)

Its injected anomalies match the rule definitions; the benchmark measures the
workflow, not real-world fraud detection.

### [ControlTrace](https://github.com/dev-belly/ControlTrace)

A synthetic IT audit workbench connecting HR events, access requests, roles,
change tickets, code commits, and production deployments. Five control tests
produce evidence-linked review candidates; analysts record append-only decisions
and export workpapers with source hashes and a replay check.

**Start here:** [Run the demo](https://github.com/dev-belly/ControlTrace) ·
[Control definitions](https://github.com/dev-belly/ControlTrace/blob/main/docs/CONTROL_CATALOG.md) ·
[Reviewed case](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md) ·
[CI](https://github.com/dev-belly/ControlTrace/actions/workflows/ci.yml)

All source records are fictional. A rule hit is a review candidate, not an audit
opinion; a missing whole-system extract cannot be detected from these records.

### [CreditVintage](https://github.com/dev-belly/CreditVintage)

A point-in-time credit cohort workflow: application-time features, fully mature
180-day delinquency labels, separate training and calibration vintages, untouched
out-of-time testing, early score monitoring before labels mature, and reviewable
static reports with downloadable rows.

**Start here:** [Live synthetic report](https://dev-belly.github.io/CreditVintage/demo/) ·
[Early score monitor](https://dev-belly.github.io/CreditVintage/monitor/) ·
[Methodology & run instructions](https://github.com/dev-belly/CreditVintage#what-is-actually-evaluated) ·
[Predictions](https://github.com/dev-belly/CreditVintage/blob/main/docs/demo/predictions.csv) ·
[CI runs](https://github.com/dev-belly/CreditVintage/actions/workflows/ci.yml)

All published data is synthetic. The independent calibration worsened Brier in
this run; the negative result is reported rather than tuned away.

### [AlphaForge](https://github.com/dev-belly/alphaforge)

A Python research pipeline connecting factor evaluation, walk-forward modeling, portfolio construction, transaction costs, and HTML reports. Includes a FastAPI service and a Streamlit dashboard.

**Start here:** [Documentation](https://dev-belly.github.io/alphaforge/) · [Computed sample](https://dev-belly.github.io/alphaforge/sample-run/) · [Source & tests](https://github.com/dev-belly/alphaforge)

The bundled sample data is synthetic; its results demonstrate the workflow and do not establish a tradable edge.

### [TradeForge](https://github.com/dev-belly/TradeForge)

An event-driven market microstructure and execution research platform with a C++20
book core and Python reference model. Its published cost comparisons use synthetic
sessions and report both arrival-price and interval-VWAP benchmarks.

**Explore:** [Reproducible demo](https://github.com/dev-belly/TradeForge#sixty-second-tour) ·
[Design and test evidence](https://github.com/dev-belly/TradeForge#what-makes-the-numbers-defensible) ·
[Transaction cost guide](https://github.com/dev-belly/TradeForge/blob/main/docs/guides/tca.md)

### [LedgerX](https://github.com/dev-belly/LedgerX)

A double-entry ledger for research fills with exact USD accounting, deterministic
replay, a hash-chained JSONL journal, optional external head checkpoints, and
separate point-in-time quote marks for open positions. The synthetic demo
reconciles historical cost, realized P&L, and marked unrealized P&L without
claiming live trading performance.

**Explore:** [Accounting model](https://github.com/dev-belly/LedgerX#python-api) ·
[Valuation example](https://github.com/dev-belly/LedgerX/blob/main/examples/valuation.json) ·
[Reproducible demo](https://github.com/dev-belly/LedgerX#run-it) ·
[CI runs](https://github.com/dev-belly/LedgerX/actions/workflows/ci.yml)

## More work

| Project | Focus |
| --- | --- |
| [FactorLab · A-share Multi-Factor Research](https://github.com/dev-belly/ashare-multifactor-research) | [Live report](https://dev-belly.github.io/ashare-multifactor-research/), [中文文档](https://github.com/dev-belly/ashare-multifactor-research/blob/main/README.zh-CN.md), and purged evaluation. The default run is synthetic; real-market point-in-time statement normalization is still in progress. |
| [High-dimensional Causal Allocation Lab](https://github.com/dev-belly/highdim-causal-allocation-lab) | [Browser demo](https://dev-belly.github.io/highdim-causal-allocation-lab/) for simulated covariate adjustment, causal estimation, and robust allocation. |
| [Interval Financial Risk](https://github.com/dev-belly/interval-financial-risk) | [Experiment report](https://dev-belly.github.io/interval-financial-risk/) comparing point and distributional features, with temporal validation and downloadable predictions. |
| [Investor Network GNN](https://github.com/dev-belly/investor-network-gnn) | [Three-seed benchmark](https://github.com/dev-belly/investor-network-gnn/tree/main/experiments/2026-09-17): fixed-checkpoint graph ablations, saved predictions and independent metric checks. |
| [WeCom Agent Platform](https://github.com/dev-belly/wecom-agent-platform) | Document retrieval and query workflows with a Python backend and React interface. |

[Personal AI Chat](https://github.com/dev-belly/personal-ai-chat) also provides a local simulated chat mode and a separately configured private model connection.

Other prototypes: [Digital Craftsman](https://github.com/dev-belly/digital-craftsman) (WeChat mini program for student credentials), [Ranxin](https://github.com/dev-belly/ranxin-mini-program) (team-built tie-dye mini program, local Mock mode), and [Goose Leg Auntie case study](https://github.com/dev-belly/goose-leg-auntie-site) (static analysis site). They are separate from the financial research work above.

## Tools & research practice

| Project | Stack |
|---|---|
| AuditLens | Python, pandas, scikit-learn, SQLite / SQLAlchemy, Streamlit |
| ControlTrace | Python, DuckDB, Streamlit, pytest |
| CreditVintage | Python, NumPy, scikit-learn, HTML/CSS, pytest, Ruff, mypy |
| AlphaForge | Python, LightGBM, CVXPY, Parquet / DuckDB, FastAPI, Streamlit |
| TradeForge | C++20, pybind11, Python, Parquet / DuckDB, FastAPI, Streamlit |
| LedgerX | Python standard library, Decimal, pytest, Ruff, mypy |

Across the other projects I also use PyTorch, TypeScript and React.

I focus on explicit data provenance, reproducible experiments, baseline comparisons, and tests that check model and application behavior. Each repository documents its setup and current limitations.
