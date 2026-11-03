# 实习项目速览 / For recruiters

中央财经大学 · 数据科学与大数据技术本科在读。希望寻找**数据分析、风险分析、金融数据工程**相关实习。
主要使用 Python、SQL；项目覆盖时间数据、模型验证和可追溯分析。

先看一个与你的岗位相关的项目，再沿链接核查结果与实现。

| 岗位方向 | 先看这个结果 | 可以继续检查的能力 |
| --- | --- | --- |
| 风控分析 / 模型验证 | [CreditVintage：两分钟看复核名额与事件捕获](https://dev-belly.github.io/CreditVintage/sba-brief/) · [完整 SBA 研究](https://dev-belly.github.io/CreditVintage/sba-credit/) · [从源码做 SQLite 复算](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_REVIEW_SQL.md) · [合成 CSV 接入检查](START_HERE.md#creditvintage-editable-csvs-and-input-diagnostics) | 按真实放款期划分、24 月表现成熟、训练独占预处理、独立校准、逐笔预测重拟合；SQL 排名和分母核对。见[建模实现](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/sba_credit.py)。 |
| 金融数据工程 | [PITBridge：修改入库时间](https://dev-belly.github.io/PITBridge/try/) · [下载情景并独立复现](START_HERE.md#download-and-replay-your-browser-scenario) · [安装包生成可编辑三表](START_HERE.md#pitbridge-create-editable-csv-inputs) | 发布/入库/决策时点、修订选择、微秒边界、离线 CSV 接入、SQL 与独立 Python 核验。见[时间连接代码](https://github.com/dev-belly/PITBridge/blob/main/src/pitbridge/core.py)。 |
| 财务 / 业务数据分析 | [StatementTrace：FY2024 申报前](https://dev-belly.github.io/StatementTrace/#as_of=2024-10-31&period=2024) → [申报后](https://dev-belly.github.io/StatementTrace/#as_of=2024-11-01&period=2024) · [一分钟试用](START_HERE.md#inspect-a-filing-cutoff) | 同一财年如何从缺失到可用；53 周财年、单位与指标公式、SEC 来源追溯。链接保留截止日与财年。见[公开来源台账](https://github.com/dev-belly/StatementTrace/blob/main/docs/SOURCES.md)。 |

## 三个可以当场展开的问题

- **校准为什么会让结果变差？** SBA 固定测试中，Logistic AUC 为 0.6723；独立保序校准改善 Brier，却降低排序和相同复核容量下的事件捕获。保留原结果，分别解释概率误差与排名。
- **两个实现一致，为什么仍可能有错？** SQL 与 Python 可能共用一个有损时间解析器。把晚到 0.9 微秒的输入截断后，两者会一起错；应先校验源精度，再做算法对照。
- **26/1,000 和 26/89 有什么区别？** 前者是 SBA 固定名单的精确率，后者是测试事件捕获率；63 个事件未进入名单。可从保存的预测用 SQLite 复算，标签不参与排名。合成工作流另有人工处理完成率，不能把任何一个说成避免坏账。

## 结果的适用范围

SBA 是真实放款日期下的回溯研究，最终快照缺少历史首次公开和修订记录。
PITBridge 与人工复核演示使用合成输入；StatementTrace 使用精选公开财报摘录。
这些项目展示实现、分析与核验方法，尚无真实银行部署或独立业务收益证据。

希望进一步了解时，可以直接选一段输入、一个失败场景和对应测试来讨论。
更详细的[项目结果与代码](PROJECT_BRIEFS.md)、[面试速讲卡](面试速讲卡.zh-CN.md)、
[运行入口](START_HERE.md)和[GitHub 主页](https://github.com/dev-belly)均可继续查阅。

[English interactive credit case](https://dev-belly.github.io/CreditVintage/sba-brief/en/)
uses the same verified data and keeps the selected review capacity when switching languages.
