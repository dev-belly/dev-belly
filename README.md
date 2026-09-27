# dev-belly

Building reproducible tools for **audit analytics, financial risk, and quantitative research**.

关注审计数据分析、金融风险与量化研究，把方法做成可以运行、检查和复现的项目。

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
replay, a hash-chained JSONL journal, and optional external head checkpoints.
It shows cash, historical inventory cost, and realized P&L; the synthetic demo
does not claim market valuation or live trading performance.

**Explore:** [Accounting model](https://github.com/dev-belly/LedgerX#python-api) ·
[Reproducible demo](https://github.com/dev-belly/LedgerX#run-it) ·
[Passing CI](https://github.com/dev-belly/LedgerX/actions/runs/36291902491)

### [FactorLab · A-share Multi-Factor Research](https://github.com/dev-belly/ashare-multifactor-research)

A factor research workflow with point-in-time feature alignment, purged out-of-sample evaluation, portfolio accounting, and browser reports.

**Explore:** [Live report](https://dev-belly.github.io/ashare-multifactor-research/) · [中文文档](https://github.com/dev-belly/ashare-multifactor-research/blob/main/README.zh-CN.md) · [Methodology](https://github.com/dev-belly/ashare-multifactor-research/blob/main/docs/methodology.md)

The default run uses synthetic data. Complete point-in-time financial statement normalization for real-market experiments is still in progress.

## More work

| Project | Focus |
| --- | --- |
| [High-dimensional Causal Allocation Lab](https://github.com/dev-belly/highdim-causal-allocation-lab) | [Browser demo](https://dev-belly.github.io/highdim-causal-allocation-lab/) for simulated covariate adjustment, causal estimation, and robust allocation. |
| [Interval Financial Risk](https://github.com/dev-belly/interval-financial-risk) | [Experiment report](https://dev-belly.github.io/interval-financial-risk/) comparing point and distributional features, with temporal validation and downloadable predictions. |
| [Investor Network GNN](https://github.com/dev-belly/investor-network-gnn) | [Three-seed benchmark](https://github.com/dev-belly/investor-network-gnn/tree/main/experiments/2026-09-17): fixed-checkpoint graph ablations, saved predictions and independent metric checks. |
| [WeCom Agent Platform](https://github.com/dev-belly/wecom-agent-platform) | Document retrieval and query workflows with a Python backend and React interface. |

[Personal AI Chat](https://github.com/dev-belly/personal-ai-chat) also provides a local simulated chat mode and a separately configured private model connection.

## Tools & research practice

| Project | Stack |
|---|---|
| AuditLens | Python, pandas, scikit-learn, SQLite / SQLAlchemy, Streamlit |
| AlphaForge | Python, LightGBM, CVXPY, Parquet / DuckDB, FastAPI, Streamlit |
| TradeForge | C++20, pybind11, Python, Parquet / DuckDB, FastAPI, Streamlit |
| LedgerX | Python standard library, Decimal, pytest, Ruff, mypy |

Across the other projects I also use PyTorch, TypeScript and React.

I focus on explicit data provenance, reproducible experiments, baseline comparisons, and tests that check model and application behavior. Each repository documents its setup and current limitations.
