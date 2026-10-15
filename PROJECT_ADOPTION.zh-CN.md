# 让现有项目值得被试用和收藏

第一次试用可从 [空目录安装、生成并核验报告](START_HERE.md#try-a-project) 开始；下文说明适合邀请哪些读者、收集什么反馈。

目标读者是做金融数据、信贷分析与审计工具的人。当前最有辨识度的入口是 CreditVintage × PITBridge：**一笔申请如何追到决策时点的数据，再进入有限容量的人工复核。** 用同一条业务链解释几个组件，比同时推十几个仓库更容易让人记住。

GitHub 的 [README 指南](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)强调项目用途、使用方法和帮助入口；[Topics 指南](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)说明相关主题可以帮助别人发现项目。这些入口降低试用门槛，不保证 Star 增长。

## 当前已有的试用路径

| 读者 | 一次能做完的任务 | 可带走的结果 |
| --- | --- | --- |
| 金融数据分析学习者 | 在 CreditVintage 原报告上运行 `analyze` | 客群/批次 SQL、组指标、无未来标签复核 CSV |
| 数据工程师 | 在 PITBridge 三决策案例中修改一条入库时间 | 当时可得值和源记录成员的变化 |
| 风控工具开发者 | 在 CreditVintage 工作区认领、结案、重试同一请求 | 持久化复核事件、当前状态、完成率 |
| IT 审计学习者 | 复核 ControlTrace 的一条发现，再更正其源证据 | 原结论历史与当前证据是否匹配 |

CreditVintage 增加了 [贡献指南](https://github.com/dev-belly/CreditVintage/blob/main/CONTRIBUTING.md)和[试用反馈入口](https://github.com/dev-belly/CreditVintage/issues/new?template=trial_feedback.yml)：反馈应带运行命令、预期/实际差异和脱敏样例。PITBridge 已有 [三决策案例](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md)与[试用模板](https://github.com/dev-belly/PITBridge/issues/new?template=trial_feedback.md)。

## 适合分享的内容

下面三种内容都能回到实际代码和输出。发布前亲自运行，截图保留“合成示例”标识，不把测试通过当作真实业务收益。

1. **“25/48 和 25/107 为什么不能混用？”** 用同一份复核清单解释精确率与事件捕获率，再展示 SQL 的分母。入口：[SQL 业务案例](https://github.com/dev-belly/CreditVintage/blob/main/docs/BUSINESS_CASE.md)。
2. **“更正早就发生了，为什么当时仍不能用？”** 更改发布与入库时间，展示当时可得集合和修订选择。入口：[三决策案例](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md)。
3. **“两个人同时认领同一条风险案例怎么办？”** 展示事务、版本冲突和同一请求 ID 的重试；给出能重复执行的命令。入口：[复核闭环](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_WORKFLOW.md)。

每次分享只围绕一个具体问题：用到的输入、输出、可运行入口、限制和希望获得的反馈。邀请读者试一种自己的脱敏输入；如果工具有用，可以收藏仓库。不要把交流变成只求 Star 的信息。

## 继续分享：把一次失败讲清楚

新的试用内容可以围绕三个反例：

| 一个能引发讨论的问题 | 读者可以做的对照 | 入口 |
| --- | --- | --- |
| 批次最后一条失败，前面几条还能算成功吗？ | 导入合法前缀加透支事件，确认旧日志不变；然后重试成功批次，确认日志头不变 | [LedgerX 批次接入](https://github.com/dev-belly/LedgerX/blob/main/docs/BATCH_INGESTION.md) |
| 输入行顺序应该决定供应商银行账户吗？ | 同 ID 放两条冲突记录，倒序后仍应拒绝；不把“保留第一条”当作主数据规则 | [AuditLens 主数据案例](https://github.com/dev-belly/AuditLens/blob/main/docs/MASTER_DATA_CASE.zh-CN.md) |
| 包内文件摘要全对，就能证明原结论没改吗？ | 修改合法备注并更新包内清单，解释为何内部一致仍需外部检查点 | [CreditVintage 底稿交付](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_DELIVERY.md) |

分享时附最小虚构输入、实际命令、修复前后输出和一个开放问题。例如邀请读者讨论“事件重试应该按 ID 还是按 ID 加内容判断”，比单独展示技术栈更容易获得有用反馈。传播效果以真实试用、复用和反馈判断。

## 判断是否在变好

把第一次试用能否跑通、反馈是否能复现、是否有人带来新输入、是否有人复用代码作为早期指标。Star 和 Fork 是结果信号，不能替代这些事实。GitHub 流量可在有权限的仓库 Insights 中查看；记录一个稳定周期再比较，不把自己的测试访问当作自然用户增长。

维护时，每个反馈先变成一个可复现案例，再修代码、补验证和更新使用入口。项目的持续可信度来自这种可见的处理过程。当前文件提供试用和分享路径，没有声称已经有外部用户、客户部署或新增 Star。
