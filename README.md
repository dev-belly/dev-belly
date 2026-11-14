# dev-belly

**用可追溯的数据，回答具体的金融问题。**

Financial research · Python · SQL · reproducible evidence

[English](README.en.md) · [全部项目](CATALOG.md) · [本地复现](START_HERE.md)

## 从一个有约束的对冲决策开始

**发现曲线风险后，有限的仓位和成本，应该怎么分配？**

[打开 CurveShift 对冲实验](https://dev-belly.github.io/StressAtlas/curveshift/hedge/)，调整预算，检查四个期限的交易、残余风险和全现金流重估结果，再下载情景复算。

| 同一个假设的 7 年期目标债券 | 2025 年情景 ES，97.5% | 一次建仓成本 |
| --- | ---: | ---: |
| 未对冲 | $71,789.20 | $0 |
| $6m 对冲面值预算 | $29,039.70 | $1,200，单独计入 |

**实现：** QuantLib 定价，SciPy 稀疏矩阵与 HiGHS 求解 513 变量的 CVaR 优化。用截至 2024 年底的 504 个变化拟合，用 2025 年的 249 个变化检验固定交易。曲线是历史拟合数据，债券是假设工具；表中 ES 未扣除一次成本，情景损失不是实盘收益。

[中文推导](https://github.com/dev-belly/StressAtlas/blob/main/labs/curveshift/docs/HEDGING.zh-CN.md) · [优化器](https://github.com/dev-belly/StressAtlas/blob/main/labs/curveshift/src/curveshift/hedge.py) · [保存的交易与损失](https://github.com/dev-belly/StressAtlas/tree/main/labs/curveshift/reports/hedge)

<a id="selected-work"></a>

## 三个代表作

### [StatementTrace](https://github.com/dev-belly/StatementTrace)

**利润增长，为什么没有变成同幅度的自由现金流增长？**

从三家公司的 24 条公开财报事实出发，统一财年、申报日与金额，生成六个公司年度的比较。Alphabet 的净利润增长 **35.67%**，自由现金流增长 **4.70%**；现金流桥逐项解释经营现金流和资本开支的贡献。

**看什么：** 来源追溯、精确金额、现金流归因，以及 Python / SQL / dbt 的计算核对。历史申报日截止 2025-02-05；财年窗口不同，FCF 为 CFO 减现金资本开支。

[中文报告](https://dev-belly.github.io/StatementTrace/cashflow/zh/) · [项目说明](https://github.com/dev-belly/StatementTrace/blob/main/README.zh-CN.md) · [来源事实](https://github.com/dev-belly/StatementTrace/blob/main/examples/cashflow/source_facts.csv)

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
