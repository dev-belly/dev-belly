# dev-belly

Building reproducible tools for **quantitative research, causal inference, and AI applications**.

关注量化研究、因果推断与 AI 应用，把方法做成可以运行、检查和复现的项目。

## Selected projects

### [AlphaForge](https://github.com/dev-belly/alphaforge)

A Python research pipeline connecting factor evaluation, walk-forward modeling, portfolio construction, transaction costs, and HTML reports. Includes a FastAPI service and a Streamlit dashboard.

**Start here:** [Documentation](https://dev-belly.github.io/alphaforge/) · [Computed sample](https://dev-belly.github.io/alphaforge/sample-run/) · [Source & tests](https://github.com/dev-belly/alphaforge)

The bundled sample data is synthetic; its results demonstrate the workflow and do not establish a tradable edge.

### [High-dimensional Causal Allocation Lab](https://github.com/dev-belly/highdim-causal-allocation-lab)

An interactive simulation lab for high-dimensional covariate adjustment, causal estimation, and robust asset allocation.

**Explore:** [Browser demo](https://dev-belly.github.io/highdim-causal-allocation-lab/) · [Repository](https://github.com/dev-belly/highdim-causal-allocation-lab)

Experiments use simulated data and depend on the chosen data-generating assumptions.

### [FactorLab · A-share Multi-Factor Research](https://github.com/dev-belly/ashare-multifactor-research)

A factor research workflow with point-in-time feature alignment, purged out-of-sample evaluation, portfolio accounting, and browser reports.

**Explore:** [Live report](https://dev-belly.github.io/ashare-multifactor-research/) · [中文文档](https://github.com/dev-belly/ashare-multifactor-research/blob/main/README.zh-CN.md) · [Methodology](https://github.com/dev-belly/ashare-multifactor-research/blob/main/docs/methodology.md)

The default run uses synthetic data. Complete point-in-time financial statement normalization for real-market experiments is still in progress.

## More work

| Project | Focus |
| --- | --- |
| [Interval Financial Risk](https://github.com/dev-belly/interval-financial-risk) | [Experiment report](https://dev-belly.github.io/interval-financial-risk/) comparing point and distributional features, with temporal validation and downloadable predictions. |
| [Investor Network GNN](https://github.com/dev-belly/investor-network-gnn) | [Three-seed benchmark](https://github.com/dev-belly/investor-network-gnn/tree/main/experiments/2026-09-17): fixed-checkpoint graph ablations, saved predictions and independent metric checks. |
| [WeCom Agent Platform](https://github.com/dev-belly/wecom-agent-platform) | Document retrieval and query workflows with a Python backend and React interface. |

[Personal AI Chat](https://github.com/dev-belly/personal-ai-chat) also provides a local simulated chat mode and a separately configured private model connection.

## Tools & research practice

Python · NumPy · pandas · scikit-learn · PyTorch · FastAPI · TypeScript · React

I focus on explicit data provenance, reproducible experiments, baseline comparisons, and tests that check model and application behavior. Each repository documents its setup and current limitations.
