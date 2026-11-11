# dev-belly · 金融数据与研究实习

**中央财经大学｜数据科学与大数据技术｜2029 届本科｜均分 91.32 / 100**

关注券商、基金和研究团队的金融数据整理、企业研究支持、统计分析与量化研究实现。
主要工具是 **Python、SQL、统计建模**；财报项目已实现 **Polars、Parquet、DuckDB、dbt** 数据管道。
北京，2027 年 1 月初可到岗，每周可实习 6 天，年后可持续。

## 先看一个完整问题

**利润增长，为什么没有变成同幅度的自由现金流增长？**

[StatementTrace 研究页面](https://dev-belly.github.io/StatementTrace/cashflow/) ·
[中文简报](https://github.com/dev-belly/StatementTrace/blob/main/docs/CASHFLOW_STUDY.zh-CN.md)

整理 Apple、Microsoft、Alphabet 三份年报中的 24 条事实，统一金额、财年与申报日，
生成六个公司年度的对比。Alphabet 净利润增长 35.67%，FCF 增长 4.70%；
通过 CFO 与现金 capex 的增量勾稽解释差异。

可以直接检查：[来源事实](https://github.com/dev-belly/StatementTrace/blob/main/examples/cashflow/source_facts.csv)、
[Python](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/cashflow.py)、
[SQL](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/data/cashflow_compare.sql)。
这是 FY2023–FY2024 的历史案例；财年窗口不同，先比较各自同比。FCF 口径为 CFO 减现金 capex。

**工程实现可进一步展开：** [Polars → Parquet → DuckDB → dbt](https://github.com/dev-belly/StatementTrace/blob/main/docs/WAREHOUSE.zh-CN.md)。
按明确的金额和日期 schema 写入列式文件，用 SQL 窗口函数计算同比与现金流桥，
通过 dbt 的 3 个模型、21 项数据检查管理转换流程。
两条 SQL 路径分别对照 Python 核验 138 个字段；另测未来申报日拦截、缺失值、
超过浮点精度的整数金额及改值后重新计算哈希的情况。
可核查[管道代码](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/warehouse.py)、
[模型](https://github.com/dev-belly/StatementTrace/tree/main/warehouse_dbt/models)与
[CI](https://github.com/dev-belly/StatementTrace/actions/workflows/warehouse.yml)。
当前是小规模公开案例，尚未测量大规模吞吐与生产效果。

接口层进一步使用 **FastAPI / Pydantic / Uvicorn**，提供六个类型明确的只读数据接口。
调用方可以筛选公司和财年、分页查询来源事实，并用快照 ID 核对同一批数据。
金额通过 JSON 时保留为精确整数字符串，缺失值保持为空；启动前核验捕获的数据包，
启动后的请求不再混读变动的源文件。
[API 中文讲解与本地启动](https://github.com/dev-belly/StatementTrace/blob/main/docs/API.zh-CN.md) ·
[类型与实现](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/api.py)。

## 按岗位看证据

| 岗位关注 | 推荐作品 | 可以当场展开的讨论 |
| --- | --- | --- |
| 企业研究 / 财务数据分析 | **StatementTrace**：[现金流研究](https://dev-belly.github.io/StatementTrace/cashflow/) | 口径统一、财报来源、同比归因、资本开支、缺失值；哪些判断需要进一步读附注。 |
| 数据分析 / 风险研究 | **CreditVintage**：[真实放款研究](https://dev-belly.github.io/CreditVintage/sba-brief/) · [SQL](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_REVIEW_SQL.md) | 35,000 条观察贷款，跨放款期验证；概率校准与排序的取舍，固定复核名额下的精确率和事件捕获率。 |
| 金融数据处理 / 研究工程 | **PITBridge**：[浏览器改一个时间](https://dev-belly.github.io/PITBridge/try/) | 数据发生、公开、入库和决策时点，修订记录选择，SQL 与独立 Python 对照。 |
| 量化研究方法 | **AlphaForge**：[共同样本与分组反例](INTERVIEW_PLAYBOOK.zh-CN.md#共同样本与分组口径) | Rank-IC 的共同有效样本、等分组、交易日标签与切分边界。旧回测待按修正协议重拟合，暂不引用收益成绩。 |

## 三个值得追问的问题

- **FCF 增长弱，能直接说明企业变差吗？** 不能。先看经营现金流与资本投入，再查投资用途、回报周期、税务和租赁口径；当前案例没有做估值结论。
- **校准改善 Brier，为什么复核结果可能变差？** 概率误差、排序质量和固定名额下的事件捕获是不同目标，需要在同一测试样本和名额下比较。
- **SQL 与 Python 一致，是否就证明数据是真的？** 一致能支持计算核对；源数据抄录、历史可得性和共同依赖还需要另外检查。

SBA 是回溯研究；PITBridge 是合成事件案例；财报研究使用人工整理的公开申报数据。
项目代码与分析产物可核查，尚无生产部署、实盘收益或商业效果的证明。

[GitHub 主页](https://github.com/dev-belly) · [完整项目目录](CATALOG.md) · [运行方法](START_HERE.md) · [面试速讲卡](面试速讲卡.zh-CN.md)
