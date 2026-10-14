# 把项目讲成业务判断：面试练习手册

想先亲自跑出结果，可用 [空目录首次运行](START_HERE.md#try-a-project)；只读审阅可用 [业务问题与代码入口](START_HERE.md#review-the-work)。

先用 [面试速讲卡](面试速讲卡.zh-CN.md)练一个开场和五个追问，再回来查实现与细节。

先练熟一条数据链：**业务要做什么决定 → 当时能看见什么数据 → 怎样验证 → 输出交给谁 → 还有什么不能证明。** 面试时按这条线讲，再根据追问打开代码。

以下第一人称是**理解并亲自练习后可使用的表达模板**，不是对你的开发经历、实习或独立贡献的认定。把“我实现了”改成实际情况：我定义了什么、亲自修改了什么、复核了什么、哪些实现由 AI 协助。不能解释的部分先说明参与范围，再补练。

依据：[项目证据](PROJECT_BRIEFS.md)、[验证记录](PROJECT_REVIEW.md)及下方链接的源码、方法与公开结果。核对日期：2026-10-13。公开演示均标明合成数据；这里不把代码演示说成实际银行上线、客户项目或已实现收益。

## 1. 按岗位选择开场

| 岗位 | 主讲问题 | 展示入口 | 展开方向 |
| --- | --- | --- | --- |
| 金融数据分析 / 银行数据 | 哪些放款批次和客群值得复核，人工名额覆盖了多少风险事件？ | [CreditVintage SQL 分析](https://dev-belly.github.io/CreditVintage/analysis/) | SQL、分母、跨月份口径、复核容量 |
| 信贷风控 / 模型验证 | 评分是否用了未来信息，评估结果能否被独立复算？ | [CreditVintage 风险报告](https://dev-belly.github.io/CreditVintage/demo/) | 标签成熟、跨期切分、校准负结果 |
| 金融数据工程 | 给定一个历史决策，重建当时实际可得的输入 | [PITBridge × CreditVintage](https://dev-belly.github.io/CreditVintage/lineage/) | 修订、发布与入库时间、单位、血缘 |
| IT 审计 / 内控 / 风险咨询 | 一条控制线索怎样成为可复核底稿？ | [ControlTrace 完整案例](https://github.com/dev-belly/ControlTrace/blob/main/docs/CASE_STUDY.md) | 控制目标、证据断链、人工结论 |
| 财务审计数据分析 | 在有限复核预算内，兼顾高风险线索与剩余总体 | [AuditLens 复核工作底稿](https://github.com/dev-belly/AuditLens/blob/main/outputs/reports/review_plan.csv) | 规则解释、抽样框、异常与舞弊的区别 |

选一条主线和一条补充线即可。所有项目都背一遍，会削弱你对一个具体问题的掌握。

## 2. CreditVintage × PITBridge：让评分回到申请时点

### 60 秒开场

> 我围绕信贷数据分析做了一条可复核的链路。业务问题是：比较不同放款批次时，能否确保输入当时可得、标签已经成熟，而且复核名单没有偷看未来逾期？
>
> PITBridge 先按事件、发布时间和入库时间选择历史修订；CreditVintage 再检查特征单位和七天新鲜度，用分开的训练、校准、测试批次评估固定基线。原始成熟测试报告还通过 SQL 拆到客群和放款月，把有限复核容量的精确率和事件捕获率分开。
>
> 我的展示重点是一笔申请：可以从预测追到源记录，再从保存的输入重放。数据是合成的，所以结果证明的是流程和验证方法。接下来我可以展开时间口径、SQL 分母，或者为什么校准结果反而变差。

### 3 分钟版本：五段，各约 30–40 秒

**① 业务决定。**

> 风控分析不能只给一个 AUC。业务还要知道哪些批次值得复核、名额怎样分配，以及看到的差异是否只是表现期不一致。我把输入可得性、标签成熟和结果分母作为分析前提。

**② 输入与时间。**

> 源数据里，一个事件可以被更正。事件发生得早，不代表更正当时已经进入系统。PITBridge 要同时满足事件时间和可得时间不晚于决策；可得时间取发布与入库的较晚者，再在合格修订中选版本。连接到模型时还明确身份、比例与计数单位、七天新鲜度，以及 UTC 日终约定。缺失、过期或删除的输入会拒绝进入适配器。

**③ 标签与评估。**

> 研究标签是申请后 180 天内出现 90 天以上逾期。统一等待表现期和两天报告滞后；没有事件还要有六份计划报告完整，缺报告不当成未违约。模型在训练期拟合，校准器在另一批成熟数据拟合，最后用更晚的批次测试。固定 Logistic 基线让数据口径和验证更容易审查。

**④ 业务输出。**

> 原始分析的成熟测试样本有 480 笔。固定全体 10% 复核容量产生 48 笔名单，包含全部 107 个事件中的 25 个：25/48 回答名单里命中多少，25/107 回答所有事件覆盖多少。SQL 从全体、客群、月份和月份乘客群四种视角拆分；名单不带未来标签，避免把回顾评价混进选人规则。

**⑤ 验证与判断。**

> 我保留了逐笔预测和源记录，也用独立 Python 路径核对 SQL 分母。联合案例还能从原始事件重建输入、重新拟合模型并比对测试预测。校准后 Brier 从约 0.155 变为 0.158，结果变差也保留，因为不能预设校准一定有效。当前链路没有真实放贷部署；要接业务，还需确认源系统完整性、标签定义、隐私权限和策略成本。

最后停下来：“您更想看一次迟到修订，还是固定容量复核的 SQL？”这能让下一轮围绕你已经准备的证据展开。

### 记牢：两份案例是不同样本

| 案例 | 样本口径 | 可以引用的结果 |
| --- | --- | --- |
| 原始评估及 SQL 业务分析 | 480 笔成熟测试申请 | 48 笔复核；107 个事件中选到 25 个；原始 Logistic AUC 约 0.747 |
| PITBridge 联合案例 | 480 笔总申请，其中 120 笔测试预测 | 1,440 个输入特征值；192 条源记录在决策后才可得 |

不能给联合案例套用原始评估的 AUC、事件数或复核效果。192 是特定合成样例中的记录数量，不是实际数据泄漏率。

### 面试前按顺序读这六处

| 代码 / 文件 | 必须能解释的问题 |
| --- | --- |
| [PITBridge `src/pitbridge/core.py`](https://github.com/dev-belly/PITBridge/blob/main/src/pitbridge/core.py) | `Observation.available_at`、SQL 中先过滤再 `ROW_NUMBER`、`reference_snapshot` 为什么不调用 SQL |
| [CreditVintage `src/creditvintage/lineage.py`](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/lineage.py) | `cutoff`、`adapt_bundle`、`verify_lineage`：日期怎么变成具体决策时刻，输入怎样连到源记录 |
| [CreditVintage `src/creditvintage/core.py`](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/core.py) | `snapshot`：时点特征、成熟等待、负标签完整报告条件 |
| [CreditVintage `src/creditvintage/model.py`](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/model.py) | `_fit_stages`：StandardScaler 和 Logistic 在哪里拟合，校准器在哪里拟合，复核同分怎么排序 |
| [CreditVintage `src/creditvintage/business_groups.sql`](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/business_groups.sql) | 条件聚合、`NULLIF`、`LAG`，同一申请为何进入不同分析视角 |
| [CreditVintage `src/creditvintage/business.py`](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/business.py)及[回归](https://github.com/dev-belly/CreditVintage/blob/main/tests/test_business.py) | 不执行 SQL 的重算、输入冻结、零分母、重哈希后篡改为什么失败 |

联合案例固定依赖 PITBridge 提交 `ed19dc698534f45a2b646fb4976ff6b01966b0cc`；解释其重放时以[该版本](https://github.com/dev-belly/PITBridge/blob/ed19dc698534f45a2b646fb4976ff6b01966b0cc/src/pitbridge/core.py)为准。[集成合同](https://github.com/dev-belly/CreditVintage/blob/main/docs/LINEAGE.md)给出身份、单位和数值比较边界。

### 高频追问：回答要带理由

**“为什么发布时间和入库时间都要考虑？”**

> 发布说明外部已提供，入库说明本系统已获得。中午发布、次日零点入库的更正，在当天 UTC 日终决策时仍不可得。只看事件日期会把未来更正倒灌回历史；只看发布时间又忽略实际采集延迟。

**“为什么先筛选可得记录，再找最新版本？”**

> 先全局取最新修订可能选到未来版本，再把它过滤掉，连当时仍有效的旧版也丢了。应先确定当时可知的集合，再选修订。同一逻辑事件的删除记录若当时可得，就不能重新启用它此前的修订；其他事件是否可用按各自历史判断。

**“日期级决策会不会丢信息？”**

> 会，所以适配器只接受明确的 UTC 日终约定，并保留源时间戳。它不支持当天上午审批的情形。要做盘中决策，应该把模型侧时间合同扩展为精确时间戳并补边界测试，不能先截成日期再说时点正确。

**“为什么不用复杂模型，为什么选择 SQLite？”**

> 先用固定基线隔离数据与评估问题；模型复杂度不能补救未来信息和标签偏差。SQLite 方便本地运行、检查 SQL 和保存轻量案例。当前没有分布式容量证据；如果要扩到真实大规模数据，应先测查询计划、索引、分区和重放成本，再决定迁移。

**“缺失为什么不填 0？”**

> 0 是一个确定业务值，缺失是没有足够证据。把未知历史变成零，会误导模型。当前适配器明确拒绝缺失，成熟负标签也要求完整报告。实际系统可另设计缺失指示和插补策略，但要在时间隔离的验证中检验，并展示拒绝比例。

**“校准不是一定改善吗？”**

> 不是。独立校准样本有限，跨期分布也可能改变；这里 isotonic 的 Brier 在测试上变差。保留它是为了如实展示比较。没有额外诊断时，不能把原因说成已经证实；也不能反复用测试集调校准器再把它叫未触碰测试。

**“PSI 上升说明坏账变多了吗？”**

> 只说明分数分布与参考期不同。标签尚未成熟时，不能据此说实际事件率或校准漂移已经上升。先查输入质量、客群构成和模型版本，成熟后再核对真实表现。PSI 阈值也不是通用风险结论。

**“为什么 10% 不按每个客群各选 10%？”**

> 目前合同是全体固定容量，再按公布精度的概率和申请 ID 排序，所以各客群入选比例会不同。SQL 把这种分配展示出来。要改成客群配额，需要明确业务目标、约束和成本，再单独评估，不能把当前结果直接称为公平或最优。

**“完整重放比哈希多证明了什么？”**

> 哈希检查文件与清单相符；如果修改文件后同步更新清单，内部一致也可能成立。重放从输入重建特征、指标和预测，能发现违背计算合同的结果。二者仍不能证明外部数据真实、抽取完整或模型适用于真实借款人。

### 复核清单之后：谁来处理，以及怎样避免覆盖

CreditVintage 新增 [人工复核闭环](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_WORKFLOW.md)。理解并运行后，可以把原来的 60 秒开场最后一段扩展为：

> 在选出复核清单之后，我还关注真正的处理过程：认领、释放、带原因和材料引用的结案，以及重开。SQLite 在同一个事务里检查版本并追加事件；两个审核人同时认领，只能一人成功。同一个请求重复提交，返回原事件。状态从历史重放，处理完成率和模型事件捕获率分别计算。

必须能解释 [reviews.py](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/reviews.py) 中的三个区别：事务保证整次操作原子完成；version 防止旧状态提交；request_id 防止相同请求重试产生第二次效果。不要把 CLI 的 actor 声明说成登录认证，也不要把材料引用说成已经验过真实附件。

现场练习：按文档处理一条案例，重复结案命令，事件数应仍为 2；用旧版本再提交新请求，应拒绝。再重开案例，旧历史保留，当前完成率下降。代码证据见 [工作流回归](https://github.com/dev-belly/CreditVintage/blob/main/tests/test_reviews.py)。

复核后也要能交付：[CreditVintage 底稿交付](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_DELIVERY.md)从一个读取事务捕获无标签清单和全部操作事件，接收人可脱离数据库重算状态。内部哈希检查字节，状态重放检查合法转换；合法备注整包重写仍可能内部一致，需要独立保存的摘要才能发现。不能把这种核验说成材料真实性认证。

仓库还提供 [同预算模型比较](https://github.com/dev-belly/CreditVintage/blob/main/docs/BENCHMARK.md)：在相同的 5%、10%、20% 容量下，对照业务规则、Logistic、WOE 评分卡与树模型。特征处理、分箱和参数在训练路径冻结；测试结果用于报告，不能反过来调参选一个部署赢家。每例 5 美元的复核成本和 45% LGD 都是假设；捕获历史事件本金的损失代理不等于减少了损失。面试里先说明“相同人力下复杂模型增加了什么”，再讲 AUC 和解释性。

## 3. ControlTrace / AuditLens：让线索形成可复核流程

新的具体切入点是 [证据绑定与旧表单保护](https://github.com/dev-belly/ControlTrace/blob/main/docs/REVIEW_INTEGRITY.md)：CH002 审批时间被更正后，D002 的发现 ID 和违规类型可能都不变，但旧关闭结论不应自动继承。现在复核绑定完整证据指纹；证据变化后恢复 pending，旧记录保留。两人同时提交同一显示版本时，事务中的实际行更新会让第二次提交冲突；仅更新成原值可能被 DuckDB 优化，不能据此宣称保护并发。

现场追问“迁移历史记录怎么办”：旧记录没有保存当时指纹，保留历史并要求重新复核，不能从今天的源数据补造历史证据。指纹相同仍不证明来源真实。[业务回归](https://github.com/dev-belly/ControlTrace/blob/main/tests/test_review_evidence.py)包含源修正、同版本并发、失败回滚与旧底稿兼容。

两个项目分别处理系统访问与变更控制、财务凭证分析。它们没有已经集成成一个企业平台；可用共同的“线索—证据—复核—底稿”思想解释。

### ControlTrace 60 秒开场

> 我关注的是 IT 控制测试怎样留下可检查的依据。HR、账号、授权、工单和部署记录通过稳定 ID 关联，按审计截止时点执行五类规则。每条线索保留控制目标、原因、源记录和时间线，再由人工记录复核结论，导出可重放底稿。
>
> 例如 D002 部署关联 CH002 工单：部署在 6 月 20 日，审批在 6 月 21 日，形成审批晚于部署的线索。如果只是缺审批时间，则应标为待补证，不能直接认定违例。这个案例是合成的；它展示我的证据和边界意识，不能代替真实审计判断。

### ControlTrace 3 分钟版本

**① 控制目标与总体。**

> 先定义常规生产部署需要事前审批和测试完成，再确定截止日前的适用总体。应急部署有单独补批口径；未知部署类型要核实，不能直接套标准流程。政策阈值是案例假设，实际项目要和受审单位制度核对。

**② 一笔证据链。**

> D002 的部署、C002 的提交、CH002 的工单通过 ID 关联。工单 6 月 17 日提交，代码 6 月 20 日 08:00 提交，10:00 部署；审批到 6 月 21 日 12:00 才完成，晚了 26 小时。测试完成也在部署后，所以产生另一条线索。两条规则命中仍是同一部署，统计部署数量时要去重。

**③ 自动判断与人工结论。**

> 有明确时间且审批晚于部署，可以形成时间违例线索；没有审批记录或时间则是证据缺口。复核人员还要看原件、时间同步、授权和例外背景。系统把自动结果与人工结论分开，追加保存复核历史，重跑规则不会擦掉此前意见。

**④ 导出与验证。**

> 底稿包含原值 JSON、便于查看的 CSV、规则元数据、复核历史和文件清单。验证不仅核对哈希，还从包内源值重跑规则，核对发现和底稿。复核状态也有合同：关闭必须有最终结论和说明；非法 JSON 或重复键在重放前拒绝。

**⑤ 一个实际边界修复。**

> 生命周期控制曾把审计截止日后才创建的账号放进此前总体，形成误报。修复把已知未来账号排除，同时保留截止时刻相等的记录和缺证据的人工复核。这体现先定义总体再测控制。源表若完全漏抽一批账号，当前规则仍无法自己证明完整性。

### AuditLens 60 秒补充

> AuditLens 处理财务凭证。在九项规则、统计检验和异常评分之后，输出有选择理由的人工复核底稿。复核预算既保留规则覆盖和高风险样本，也留一部分名额从非定向总体随机抽取。
>
> 这样会牺牲一部分合成命中数：300 笔预算下，混合方案包含 107 个注入异常，纯风险排序包含 140 个。随机控制样本用来了解剩余总体，而不是刷更高命中率。规则或模型的异常线索还要查看凭证；异常评分不能直接认定舞弊。

### 审计方向代码入口

| 文件 | 要讲清的判断 |
| --- | --- |
| [ControlTrace `src/controltrace/rules.py`](https://github.com/dev-belly/ControlTrace/blob/main/src/controltrace/rules.py) | `evaluate`：截止日总体、缺证据与违例分类、CT-04 时间条件 |
| [ControlTrace `src/controltrace/store.py`](https://github.com/dev-belly/ControlTrace/blob/main/src/controltrace/store.py)及[`reviews.py`](https://github.com/dev-belly/ControlTrace/blob/main/src/controltrace/reviews.py) | 追加复核记录、UTC 排序、状态与结论校验 |
| [ControlTrace `src/controltrace/verify.py`](https://github.com/dev-belly/ControlTrace/blob/main/src/controltrace/verify.py) | `verify_bundle`：结构、哈希、JSON/CSV 和规则重放 |
| [AuditLens `src/review_plan.py`](https://github.com/dev-belly/AuditLens/blob/main/src/review_plan.py) | `build_review_plan`：覆盖、定向排序、剩余总体随机抽取，选择不读标签 |
| [AuditLens `src/review_outcomes.py`](https://github.com/dev-belly/AuditLens/blob/main/src/review_outcomes.py) | `summarize_completed_review`：只允许改复核字段，用同一字节快照解析并计算摘要 |
| [AuditLens 方法说明](https://github.com/dev-belly/AuditLens/blob/main/docs/methodology.md) | 缺失特征不能被规则当作零；Benford 与 Isolation Forest 的适用边界 |

**“少了审批记录，为什么不直接判违规？”**

> 可能是真的没审批，也可能是抽取遗漏或存在于其他系统。自动程序能证明的是当前证据不充分。明确晚审批和缺记录必须分别报告，否则会把数据质量问题包装成审计结论。

**“抽查 300 笔，能估计全账异常率吗？”**

> 不能把整份混合名单当简单随机样本。默认有 240 笔定向选择，60 笔从剩余 29,888 笔中随机抽取；60/29,888 的纳入概率只适用于剩余抽样框。先完成复核、明确异常口径，再讨论该框内估计和抽样误差，不能用模型标签冒充人工结果。

**“为什么不用有监督的舞弊模型？”**

> 真实任务未必有可信舞弊标签；用注入标签训练容易学习生成器。这里无监督评分用于排序，规则提供可读证据。合成标签只在选样完成后评价，不能证明真实识别效果。

**“你处理过什么容易忽略的工程问题？”**

> 我会用复核文件快照说明：先读文件算统计，之后再读一次算哈希，若中间有人保存，报告可能统计旧版却引用新版。AuditLens 改为读一次字节，同时用这份字节解析和计算摘要。这个修复维护的是证据版本一致性，不是人为提高命中率。

### 新的反例：主数据先要有一致的含义

[AuditLens 主数据案例](https://github.com/dev-belly/AuditLens/blob/main/docs/MASTER_DATA_CASE.zh-CN.md)解释同一供应商 ID 出现不同银行账户时的处理。没有权威修订号、生效区间或审批依据，就不能让“第一条/最后一条”决定答案；完全一致的重复记录可合并，冲突记录明确拒绝。比较发生在日期有损解析之前，避免两个不同坏日期都变成 NaT 后被误当作一致。

四个清洗产物先全部暂存，发布失败回滚已替换的文件；回滚也失败则保留旧版本备份并报告恢复路径。这是单进程 CLI 的失败处理，不能宣称多文件替换对并发读者是一个原子快照。现场练习可以先交换两条冲突主数据的顺序：两次都应该拒绝，而不是出现不同审计结论。

## 4. 现场展示：先操作，再解释

**信贷：在 CreditVintage 仓库根目录，Python 3.12+。** 每次练习选择尚不存在的输出目录；别覆盖之前的练习证据。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\creditvintage.exe analyze docs/demo --out outputs/interview-analysis
.\.venv\Scripts\creditvintage.exe verify-analysis outputs/interview-analysis
```

打开 `outputs/interview-analysis/index.html`：先讲一个分子和分母，再切换一次月份 × 客群视角，最后指出复核 CSV 不含标签。完整源到预测演示需按 [README 的固定依赖步骤](https://github.com/dev-belly/CreditVintage#source-to-prediction-lineage)安装 PITBridge，再运行 `lineage-demo` 和 `verify-lineage`。

**内控：在 ControlTrace 仓库根目录，按 README 安装 uv。**

```powershell
uv run controltrace demo
```

在界面选 D002 的晚审批线索，打开三条源记录，保存你自己的示范复核；关闭界面后导出并验证：

```powershell
uv run controltrace export
uv run controltrace verify --bundle exports/workpapers.zip
```

**凭证：在 AuditLens 仓库根目录的独立环境中。**

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt -r requirements-dev.txt
.\.venv\Scripts\python.exe src/run_pipeline.py
```

打开 `outputs/reports/review_plan.csv`，指出三种选择路径以及随机概率仅对哪一类行有意义。

## 5. 五个练习：做出来后再背台词

| 练习 | 要交出的证据 | 解题方向 / 自查 |
| --- | --- | --- |
| 手算迟到更正 | 两条修订与一个决策时刻，写出最终版本 | 决策为 UTC 日终，更正中午发布但次日零点入库：旧版仍可用；入库提前到截止时刻时更正可用 |
| 手写客群 SQL | 数量、事件率、平均 PD 三列 | `COUNT(*)`、`SUM(label)`、`1.0 * SUM(label)/COUNT(*)`、`AVG(calibrated_pd)`；合计用总分子/总分母，不能平均两个事件率 |
| 解释三个分母 | 写出 107/480、25/48、25/107 各回答什么 | 总体事件率、名单精确率、事件捕获率；再解释为什么最后一项不等于减少坏账的比例 |
| 改一条源记录再验证 | 在证据副本里制造错误，记录拒绝原因 | 可先改数值看哈希失败，再按测试已有方式同步更新哈希看语义重放失败；不要改发布样例 |
| 做一个资料缺口案例 | 把 CH002 审批时间改为缺失后的分类和解释 | 从明确晚审批转为人工核实；列出要补的材料，解释为何不能自动说合规或违规 |

加练 SQL：没有复核申请的组，精确率输出空值；没有事件的组，捕获率输出空值。0% 表示分母存在但分子为零，空值表示比率未定义。

加练测试：找一个“截止时刻相等”的回归，先口述输入和预期，再看代码；能说清如果比较符号改为 `<`，哪一种合法输入会被误拒绝。

每天用 15 分钟：3 分钟讲业务链路，5 分钟读一处代码，5 分钟做一个反例，2 分钟复述局限。至少录一次音，删掉没有证据支撑的“显著提升”“企业级”“全自动”等词。

## 6. 如果投 AI 应用 / 后端岗位：企业查询的业务判断

[企微平台业务案例](https://github.com/dev-belly/wecom-agent-platform/blob/main/docs/business-workflow.md)提供一条适合补充的主线：

> 检索能找相关内容，但合同条件筛选和客户持仓总额不能靠检索前几条代表全体。我把结构化查询放在所有已索引表格行上执行：业务编号保留前导零并精确匹配，日期按闭区间过滤，金额用 Decimal 和明确的币种、单位计算。缺估值时给出不完整原因，不能默认补零。每行都有文件、页码和表格位置，且不接大模型也能走鉴权 API 和离线示例验证结果。

追问“总额和展示条数为什么不同”：总额基于全部匹配行，界面结果可以截断但应明示；检索 top-k 是发现候选的机制，不是完整统计口径。追问“是不是生产客户资产”：当前是虚构解析样例和已索引数据，没有验证源系统的全量完整性，也没有实现客户级细粒度授权或跨币种兑换。

企业查询还要保证同一份数据：[索引快照案例](https://github.com/dev-belly/wecom-agent-platform/blob/main/docs/index-snapshots.md)先准备完整的新一代检索与结构化行，成功后一起发布，失败保留旧代。读者固定捕获一次快照，合同与持仓结果带该次 `index_revision`；正在读旧代时不会被新代发布改写，向量集合要等旧读者结束再清理。该保证是一个服务进程内的索引版本一致性，不证明源系统完整性或跨进程一致性。

### 量化工程项目也有接口边界

[TradeForge #13](https://github.com/dev-belly/TradeForge/pull/13)修复了一个能当场复现的报告读取问题：请求者曾能用 `directory` 指定任意外部目录，服务端只检查文件是否在这个请求者指定的目录里。这相当于把信任边界交给了调用者。现在根目录由服务启动配置固定，请求只能选择根下相对子目录，并拒绝跨平台绝对路径、父目录和符号链接越界。

讲这个例子时要能说明“路径包含检查为什么还不够”：检查所依赖的根必须由服务控制，不能同样来自不可信请求。合法生成报告仍可读；相同外部 HTML 在旧代码返回 200，新代码拒绝。它是报告服务边界修复，不是交易策略表现或完整服务认证的证据。

## 7. 被问“是不是 AI 写的”时

按真实情况填完这段，再练到无需照读：

> 我使用 AI 协助了【具体代码、文档或测试范围】。我亲自负责或复核了【有证据的内容】。例如这条【时间边界 / 分母 / 状态转换】约束，我能解释业务理由，现场修改输入并预测结果，也能指出哪项测试会失败。其余【尚未掌握的模块】由工具协助较多，我会明确参与范围。项目是否可信，我愿意让您沿输入、规则和重放结果检查。

用一处亲手完成的变更回答，比声称“全是我独立写的”更经得起追问。练习完成后再把相关点写进简历；测试通过也不自动等于你掌握了全部实现。

遇到没做的生产问题，可以直接说：

> 当前公开实现做到【已验证的范围】，这部分没有生产证据。如果继续做，我会先明确【业务合同】，设计【反例 / 对照】，再测【结果指标】。我现在能展示的是【对应文件或操作】。

能够清楚说出业务决定、成立条件、反例和下一步验证，就是这些项目最适合展示的能力。
