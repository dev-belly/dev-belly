# 项目目录 / Project directory

<!-- Generated from portfolio.json; run python scripts/build_project_catalog.py. -->

这里收录 **19 个公开项目**，按使用目的组织。先打开 README 确认环境，再按对应证据复现。
目录不把公开源码、静态演示或 CI 通过等同于生产部署、实盘表现或第三方认证。

| 你想做什么 | 推荐路线 |
| :--- | :--- |
| 不安装环境，先改一个输入 | [PITBridge 浏览器发票案例](https://colab.research.google.com/github/dev-belly/PITBridge/blob/main/examples/decision_time.ipynb) |
| 看信贷分析或数据岗位作品 | CreditVintage → PITBridge → StatementTrace |
| 看量化研究与工程 | AlphaForge → TradeForge → StressAtlas；再看保留负结果的图模型与区间实验 |
| 看审计、会计与内控 | AuditLens → ControlTrace → LedgerX |
| 看应用开发 | WeCom Agent → Personal AI Chat → 两个微信小程序 |

[空目录安装与逐步试用](START_HERE.md) · [成果与代码](PROJECT_BRIEFS.md) · [验证记录](PROJECT_REVIEW.md)

## 先试这三个 / Start here

| 项目与入口 | 解决的问题 / 技术 | 数据与使用边界 |
| :--- | :--- | :--- |
| [**CreditVintage**](https://github.com/dev-belly/CreditVintage) · [README](https://github.com/dev-belly/CreditVintage/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/CreditVintage/sba-credit/) · [证据 / 方法](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md) | 跨期信贷验证、客群 SQL 分析与人工复核<br />Python · SQL · scikit-learn | SBA 放款分期回溯、UCI 静态数据与合成事件实验分别解释。 |
| [**PITBridge**](https://github.com/dev-belly/PITBridge) · [README](https://github.com/dev-belly/PITBridge/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/PITBridge/try/) · [证据 / 方法](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md) | 按事件与获知时间重建历史快照和滚动特征<br />Python · SQLite | 合成发票与事件示例；演示数据可用性规则。 |
| [**StressAtlas**](https://github.com/dev-belly/StressAtlas) · [README](https://github.com/dev-belly/StressAtlas/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/StressAtlas/) · [证据 / 方法](https://github.com/dev-belly/StressAtlas/blob/main/docs/METHODOLOGY.md) | 相关违约、组合尾部损失和估计精度<br />Python · NumPy | 合成贷款组合；压力情景和重采样不代表真实损失预测。 |

## 财务、审计与清偿 / Financial systems

| 项目与入口 | 解决的问题 / 技术 | 数据与使用边界 |
| :--- | :--- | :--- |
| [**StatementTrace**](https://github.com/dev-belly/StatementTrace) · [README](https://github.com/dev-belly/StatementTrace/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/StatementTrace/) · [证据 / 方法](https://github.com/dev-belly/StatementTrace/blob/main/docs/SOURCES.md) | 从公开财报到可追溯的财务指标<br />Python · SQL | 精选公开财报摘录；保留期间、来源与可用时间。 |
| [**NetworkClear**](https://github.com/dev-belly/NetworkClear) · [README](https://github.com/dev-belly/NetworkClear/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/NetworkClear/) · [证据 / 方法](https://github.com/dev-belly/NetworkClear/blob/main/docs/METHODOLOGY.md) | 交易对手冲击、债务清偿与外部损失勾稽<br />Python | 合成金融网络；模型假设见清偿方法。 |
| [**ControlTrace**](https://github.com/dev-belly/ControlTrace) · [README](https://github.com/dev-belly/ControlTrace/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md) | 把内控结论绑定到当前证据版本<br />Python | 审计工作流案例；不等于真实审计意见。 |
| [**AuditLens**](https://github.com/dev-belly/AuditLens) · [README](https://github.com/dev-belly/AuditLens/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/AuditLens/tree/main/outputs/reports/) | 总账异常、可解释风险排序与审计底稿<br />Python · SQL · Streamlit | 合成总账和规则实验；结果用于人工审阅。 |
| [**LedgerX**](https://github.com/dev-belly/LedgerX) · [README](https://github.com/dev-belly/LedgerX/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/LedgerX/blob/main/examples/valuation.json) | 成交、复式记账与估值的精确勾稽<br />Python | 示例交易与会计规则；许可证以仓库声明为准。 |

## 量化与研究实验 / Research experiments

| 项目与入口 | 解决的问题 / 技术 | 数据与使用边界 |
| :--- | :--- | :--- |
| [**alphaforge**](https://github.com/dev-belly/alphaforge) · [README](https://github.com/dev-belly/alphaforge/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/alphaforge/sample-run/) · [证据 / 方法](https://github.com/dev-belly/alphaforge/blob/main/docs/research-comparison.md) | 因子、逐步前推验证、组合约束与交易成本<br />Python · NumPy | 旧回测的自然日缓冲与交易日标签不一致；尚未按修正协议重拟合，不能作为无泄漏样本外证据。 |
| [**TradeForge**](https://github.com/dev-belly/TradeForge) · [README](https://github.com/dev-belly/TradeForge/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md) | C++ 订单簿、执行事件与 Python 独立核验<br />C++20 · Python | 公开报价只支持假设成交；不代表真实委托或可交易收益。 |
| [**investor-network-gnn**](https://github.com/dev-belly/investor-network-gnn) · [README](https://github.com/dev-belly/investor-network-gnn/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/investor-network-gnn/tree/main/experiments/2026-09-17/) | 投资者网络、图模型消融与多种子预测<br />Python · PyTorch | 合成数据；保留 GCN 未显示稳定优势的结果。 |
| [**highdim-causal-allocation-lab**](https://github.com/dev-belly/highdim-causal-allocation-lab) · [README](https://github.com/dev-belly/highdim-causal-allocation-lab/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/highdim-causal-allocation-lab/) | 高维因果估计、Monte Carlo 与稳健配置<br />Python · React | 模拟因果与配置实验；不建立现实因果结论。 |
| [**interval-financial-risk**](https://github.com/dev-belly/interval-financial-risk) · [README](https://github.com/dev-belly/interval-financial-risk/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/interval-financial-risk/) | 区间和分布特征的风险识别实验<br />Python | 合成实验中的负结果：区间特征未改善 AUC。 |
| [**ashare-multifactor-research**](https://github.com/dev-belly/ashare-multifactor-research) · [README](https://github.com/dev-belly/ashare-multifactor-research/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/ashare-multifactor-research/blob/main/README.zh-CN.md) | A 股因子研究、purged 验证与数据接入<br />Python · SQL | 默认合成数据；真实 A 股结果须按对应数据路径单独验证。 |

## 应用与早期作品 / Applications

| 项目与入口 | 解决的问题 / 技术 | 数据与使用边界 |
| :--- | :--- | :--- |
| [**wecom-agent-platform**](https://github.com/dev-belly/wecom-agent-platform) · [README](https://github.com/dev-belly/wecom-agent-platform/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/wecom-agent-platform/blob/main/docs/business-workflow.md) | 合同全量筛选、持仓汇总与企业微信 Agent 原型<br />Python · FastAPI · React | 静态界面和离线业务试验；模型、企微回复及部署有独立边界。 |
| [**personal-ai-chat**](https://github.com/dev-belly/personal-ai-chat) · [README](https://github.com/dev-belly/personal-ai-chat/blob/main/README.md) | 本地聊天模拟与单独配置的私有模型连接<br />Next.js · Cloudflare Workers | 默认固定本地模拟；真实服务需要独立配置与访问口令。 |
| [**digital-craftsman**](https://github.com/dev-belly/digital-craftsman) · [README](https://github.com/dev-belly/digital-craftsman/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/digital-craftsman/blob/main/%E9%A1%B9%E7%9B%AE%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.md) | 学生能力档案、企业评价与作品集小程序<br />微信小程序 · 云函数 | 小程序及云环境需单独部署验收；不上线状态承诺。 |
| [**ranxin-mini-program**](https://github.com/dev-belly/ranxin-mini-program) · [README](https://github.com/dev-belly/ranxin-mini-program/blob/main/README.md) · [证据 / 方法](https://github.com/dev-belly/ranxin-mini-program/blob/main/ONBOARDING.md) | MBTI、纹样收集与 DIY 创作比赛原型<br />微信小程序 · JavaScript | 默认本地 Mock；云函数和真实数据库需单独验收。 |
| [**goose-leg-auntie-site**](https://github.com/dev-belly/goose-leg-auntie-site) · [README](https://github.com/dev-belly/goose-leg-auntie-site/blob/main/README.md) · [试用 / 报告](https://dev-belly.github.io/goose-leg-auntie-site/) | 校园传播案例的信息组织与页面呈现<br />HTML · CSS | 公开报道与分析推断分开；不是独立经营审计。 |

## 反馈与参与 / Feedback and contribution

主页导航、文字与目录问题请到 [主页 Issues](https://github.com/dev-belly/dev-belly/issues/new/choose)；
项目运行错误请到对应仓库的 Issues，附 commit 或版本、系统环境、完整命令和最小合成输入。
仓库内的 SUPPORT、CONTRIBUTING 与 SECURITY 文件分别说明试用、贡献和安全报告路径。
许可证与数据使用条件以各仓库的实际声明为准。

维护目录时编辑 [portfolio.json](portfolio.json)，然后运行 `python scripts/build_project_catalog.py`。
`--check` 和主页 CI 离线核对结构与生成结果；不会把远端站点的实时可用性作为已通过的结论。
