# dev-belly

**把界面、接口和数据处理连成可运行的应用。**

中央财经大学 · 数据科学与大数据技术本科在读 · 当前方向：全栈开发

[English](README.en.md) · [开发项目速览](FOR_RECRUITERS.md) · [数据工作台](#数据工作台) · [本地运行](START_HERE.md) · [全部项目](CATALOG.md)

## 先看应用与接口

面向 **2027 年暑期开发实习**积累作品，当前系统学习 HTML、CSS 与 JavaScript。
下面的入口可以直接查看现有实现、运行命令与验证方法。

| 项目 | 已实现的开发能力 | 先看哪里 |
| --- | --- | --- |
| **[Personal AI Chat](https://github.com/dev-belly/personal-ai-chat)** | Next.js 16.4 / React 19.3 / TypeScript 7 / AI SDK 7；Dexie 多会话与草稿保护、Streamdown / Shiki 流式 Markdown、双模型协议 | [本地运行与工程说明](https://github.com/dev-belly/personal-ai-chat/blob/main/README.md) · [本机会话](https://github.com/dev-belly/personal-ai-chat/blob/main/docs/LOCAL_CONVERSATIONS.zh-CN.md) · [架构与协议](https://github.com/dev-belly/personal-ai-chat/blob/main/docs/ARCHITECTURE.zh-CN.md) |
| **[StatementTrace](https://github.com/dev-belly/StatementTrace)** | 财报浏览器通过 FastAPI 按公司和财年读取固定快照，从自由现金流追到原始申报 | [在线财报浏览器](https://dev-belly.github.io/StatementTrace/explorer/) · [本地运行](START_HERE.md#query-the-verified-financial-api) · [页面实现](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/data/explorer/explorer.js) |
| **[CreditVintage](https://github.com/dev-belly/CreditVintage)** | 网页领取、结案和重开复核任务，查看 SQLite 事件历史；版本检查防止两个标签页覆盖同一案件 | [在线案件复核台](https://dev-belly.github.io/CreditVintage/review/) · [本地运行](START_HERE.md#creditvintage-review-workbench) · [复核实现](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/reviews.py) |
| **[WeCom Agent](https://github.com/dev-belly/wecom-agent-platform)** | React 合同筛选与 FastAPI 分页，按索引版本保持结果一致，每条合同可查来源页码 | [在线试用](https://dev-belly.github.io/wecom-agent-platform/?view=contracts) · [接口与测试](FOR_RECRUITERS.md#复核对账与合同查询) |
| **[PITBridge](https://github.com/dev-belly/PITBridge)** | 浏览器交互、URL 状态、JSON 下载与 Python / SQLite 独立重放 | [立即试用](https://dev-belly.github.io/PITBridge/try/) · [下载后重放](START_HERE.md#download-and-replay-your-browser-scenario) |
| **[LedgerX](https://github.com/dev-belly/LedgerX)** | JSONL 批量导入、重复批次回执、逐笔复式分录和对账快照下载 | [本地对账工作台](START_HERE.md#ledgerx-reconciliation-workbench) · [导入与重放实现](https://github.com/dev-belly/LedgerX/blob/main/src/ledgerx/ingestion.py) |
| **[NetworkClear](https://github.com/dev-belly/NetworkClear)** | 比较清算场景，按机构筛回收率、连锁违约和外部债权人损失 | [在线清算控制台](https://dev-belly.github.io/NetworkClear/) · [清算算法](https://github.com/dev-belly/NetworkClear/blob/main/src/networkclear/engine.py) |

Personal AI Chat 的本地演示使用固定回复。

<a id="selected-work"></a>

## 三个代表作

### [StatementTrace](https://github.com/dev-belly/StatementTrace)

**利润增长，为什么没有变成同幅度的自由现金流增长？**

从三家公司的 24 条公开财报事实出发，统一财年、申报日与金额，生成六个公司年度的比较。Alphabet 的净利润增长 **35.67%**，自由现金流增长 **4.70%**；现金流桥逐项解释经营现金流和资本开支的贡献。

**看什么：** 来源追溯、精确金额、现金流归因，以及 Python / SQL / dbt 的计算核对。历史申报日截止 2025-02-05；财年窗口不同，FCF 为 CFO 减现金资本开支。

[中文报告](https://dev-belly.github.io/StatementTrace/cashflow/zh/) · [项目说明](https://github.com/dev-belly/StatementTrace/blob/main/README.zh-CN.md) · [来源事实](https://github.com/dev-belly/StatementTrace/blob/main/examples/cashflow/source_facts.csv)

[继续拆解净利润到 CFO](https://dev-belly.github.io/StatementTrace/cashflow/profit-bridge/)：六个年度逐项勾稽，分开税款、收购与融资租赁；116 个选中值及 8 个明确缺失，Python / SQLite 核对 144 个字段。

### [CreditVintage](https://github.com/dev-belly/CreditVintage)

**更准确的违约概率，会带来更好的人工复核队列吗？**

在 **35,000 条观察到的 SBA 贷款**上分开训练、校准与更晚放款批次，比较相同复核名额下的排序和事件捕获。概率误差改善与业务排序改善并不等价；保存的预测可以继续用 SQL 检查。

**看什么：** 时间切分、概率校准、固定处理容量与可重放的人工复核。它是成熟结果窗口下的回溯研究；最终来源快照没有历史发布与修订记录。

[调整复核名额](https://dev-belly.github.io/CreditVintage/sba-brief/) · [研究口径](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md) · [SQL 练习](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_REVIEW_SQL.md)

### [PITBridge](https://github.com/dev-belly/PITBridge)

**做出决策的那一刻，这条数据真的已经可得了吗？**

改一张发票的到达时间，查看决策时点选中的版本，再下载输入，用 Python 独立重放。把事件时间、获知时间和决策时间分开，用 SQLite 与另一条 Python 路径核对。

**看什么：** 迟到数据、修订版本、历史快照与来源级解释。交互案例使用小规模合成发票，便于直接观察时间规则。

[改一个时间](https://dev-belly.github.io/PITBridge/try/) · [重放下载的情景](START_HERE.md#download-and-replay-your-browser-scenario) · [实现](https://github.com/dev-belly/PITBridge/blob/main/src/pitbridge/core.py)

## 数据工作台

这些页面可以按条件筛选、打开单条证据，并下载筛选结果。浏览器样例随仓库保存，打开对应目录的 `index.html` 即可离线试用。

| 项目 | 浏览器里可以做什么 | 入口 |
| --- | --- | --- |
| **TradeForge** | 对比立即执行与十批 TWAP，在 18 个费率和延迟组合里拆解成本 | [执行回放](https://github.com/dev-belly/TradeForge/tree/main/docs/workbench) |
| **AuditLens** | 从 300 条复核凭证筛出风险或随机样本，检查入选理由 | [审计复核](https://github.com/dev-belly/AuditLens/tree/main/docs/workbench) |
| **ControlTrace** | 逐条核对五项内控规则命中的事件时间线和来源记录 | [证据工作台](https://github.com/dev-belly/ControlTrace/tree/main/docs/workbench) |
| **NetworkClear** | 切换 15 个冲击与注资情景，追踪传染违约和精确付款 | [清算工作台](https://github.com/dev-belly/NetworkClear/tree/main/docs/workbench) |
| **StressAtlas** | 比较尾部损失和违约相关性，并把 ES 分解到行业 | [在线尾部风险工作台](https://dev-belly.github.io/StressAtlas/workbench/) · [源码](https://github.com/dev-belly/StressAtlas/tree/main/demo/workbench) |
| **AlphaForge** | 对照 22 组市场实验，查看净夏普、成本拖累和标签边界 | [在线量化实验工作台](https://dev-belly.github.io/alphaforge/workbench/) · [源码](https://github.com/dev-belly/alphaforge/tree/main/docs/workbench) |
| **Investor Network GNN** | 切换模型和种子，核对样本外指标与删边对照 | [图模型实验](https://github.com/dev-belly/investor-network-gnn/tree/main/docs/workbench) |
| **LedgerX** | 导入批次、验证安全重试，从流水查看借贷分录 | [本地对账台](START_HERE.md#ledgerx-reconciliation-workbench) |

## 从研究结果读到工程实现

| 路线 | 已实现的能力 | 阅读入口 |
| --- | --- | --- |
| 财务数据管道 | Polars / Parquet / DuckDB / dbt；明确金额和日期类型，每条 SQL 路径核对 138 个字段 | [管道说明](https://github.com/dev-belly/StatementTrace/blob/main/docs/WAREHOUSE.zh-CN.md) |
| 研究 API | FastAPI / Pydantic；六个只读接口、分页、精确金额字符串与同一快照标识 | [接口与请求示例](https://github.com/dev-belly/StatementTrace/blob/main/docs/API.zh-CN.md) |
| 量化实验对照 | 六个交易日隔离窗口；五种方法、三个模型种子、两档成本，共 22 个结果组合 | [AlphaForge 重训与窗口核查](https://dev-belly.github.io/alphaforge/research-comparison.zh-CN/) |
| 审计分析 | 可解释的风险排序、人工复核与来源绑定的工作底稿 | [AuditLens 中文入口](https://github.com/dev-belly/AuditLens/blob/main/README.zh-CN.md) |
| 执行分析 | C++20 订单簿、Python 交易成本分析、公开市场假设成交案例 | [TradeForge](https://github.com/dev-belly/TradeForge/blob/main/docs/PUBLIC_MARKET_CASE.md) |

管道与 API 使用同一组 24 条人工整理的财报事实；计算一致性与来源抄录准确性分别审阅。API 在本地运行，静态页面托管研究报告。

<details>
<summary>更多研究与复现记录</summary>

- [CurveShift 曲线风险实验](https://dev-belly.github.io/StressAtlas/curveshift/)：平行 DV01 近似为零，曲线扭转仍可产生损失。
- [AlphaForge 重训对照](https://dev-belly.github.io/alphaforge/experiments/real-sp500-session-v2/)：同一份 84 万行监督数据，按交易日隔离重新拟合全部模型；保存 22 个结果和六个窗口的标签结束日。Ridge 的 Sharpe 低于简单等权基准。历史成员与披露时点缺口继续单独说明。
- [19 个项目与各自数据范围](CATALOG.md) · [运行指南](START_HERE.md) · [当前优先事项](OPEN_SOURCE_ROADMAP.zh-CN.md)。
- [验证记录](PROJECT_REVIEW.md) · [变更记录](CHANGELOG.md) · [参与维护](CONTRIBUTING.md)。

</details>
