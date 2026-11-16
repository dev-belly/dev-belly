# dev-belly · 开发项目速览

中央财经大学数据科学与大数据技术本科在读，当前方向为**全栈开发**，目标是 2027 年暑期开发实习。
目前系统学习 HTML、CSS 与 JavaScript；作品集按可运行的页面、接口、数据和验证组织。

## 先看 Personal AI Chat：页面到可取消的流式接口

[仓库与运行说明](https://github.com/dev-belly/personal-ai-chat) ·
[架构与设计取舍](https://github.com/dev-belly/personal-ai-chat/blob/main/docs/ARCHITECTURE.zh-CN.md) ·
[标准消息流 / 兼容接口](https://github.com/dev-belly/personal-ai-chat/blob/main/docs/API.zh-CN.md)

用 **Next.js 16.4 / React 19.3 / TypeScript 7 / AI SDK 7** 实现模块化 BFF：页面、状态、传输、HTTP 编排和模型适配器各有边界。
默认本地模拟让读者先体验；真实服务逐段显示模型回复，浏览器使用独立访问口令。
半途断流或取消会保留“未完成回复”，只有明确完成的轮次进入后续上下文。

| 可以检查的能力 | 对应源码 | 具体行为 |
| --- | --- | --- |
| 页面状态与交互 | [use-chat.ts](https://github.com/dev-belly/personal-ai-chat/blob/main/app/hooks/use-chat.ts) · [chat-state.ts](https://github.com/dev-belly/personal-ai-chat/blob/main/lib/chat-state.ts) | 流入、完成、未完成、取消重试与新会话；旧请求动作不能写入新会话。 |
| 流式传输 | [chat-ui-transport.ts](https://github.com/dev-belly/personal-ai-chat/blob/main/lib/chat-ui-transport.ts) | 使用 AI SDK 官方传输与 UIMessage 读取器；校验元数据、帧预算和明确完成事件。 |
| 共享数据契约 | [chat-contract.ts](https://github.com/dev-belly/personal-ai-chat/blob/main/lib/chat-contract.ts) | Zod 4 校验实际输入并推导类型；标准 UI 信封按真实序列化开销裁剪。 |
| 对话上下文 | [lib/chat-client.ts](https://github.com/dev-belly/personal-ai-chat/blob/main/lib/chat-client.ts) | 只携带完成的对话轮次；按消息数、字符数和 UTF-8 字节预算裁剪。 |
| 服务端接口 | [chat-handler.ts](https://github.com/dev-belly/personal-ai-chat/blob/main/lib/server/chat-handler.ts) | 配置、独立口令、JSON / SSE 协商、50 秒截止时间、取消传播与请求编号。 |
| 模型适配器 | [model-provider.ts](https://github.com/dev-belly/personal-ai-chat/blob/main/lib/server/model-provider.ts) | Anthropic 与 OpenAI 兼容服务共享 AI SDK 接口；验证终止原因，不自动重试。 |
| 输入契约 | [lib/chat-validation.ts](https://github.com/dev-belly/personal-ai-chat/blob/main/lib/chat-validation.ts) | 流式读取并限制请求体；校验角色交替、消息长度和完整会话。 |
| HTTP 集成验证 | [scripts/check-http.mjs](https://github.com/dev-belly/personal-ai-chat/blob/main/scripts/check-http.mjs) | 33 项检查经过生产 Next.js 和 AI SDK，验证先到达的文本、断流、公开错误与上游连接关闭，无真实模型费用。 |
| 浏览器验收 | [check-browser.mjs](https://github.com/dev-belly/personal-ai-chat/blob/main/scripts/check-browser.mjs) | Chromium 验证流式显示、取消重试、错误、清空会话与手机布局；CI 保存合成会话截图。 |
| 构建与部署配置 | [CI](https://github.com/dev-belly/personal-ai-chat/blob/main/.github/workflows/ci.yml) · [README](https://github.com/dev-belly/personal-ai-chat/blob/main/README.md) | strict TypeScript、Node 测试、依赖审计、HTTP 与浏览器验证、Next.js 及 OpenNext / Cloudflare Workers 双构建。 |

首次试用可按 [运行指南](START_HERE.md#run-the-full-stack-chat-application--运行全栈聊天应用)执行。
默认模拟回复是固定示例；真实模型与生产部署需单独配置。

## 再看 StatementTrace：类型接口与数据一致性

[API 运行说明](https://github.com/dev-belly/StatementTrace/blob/main/docs/API.zh-CN.md) ·
[接口实现](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/api.py) ·
[接口测试](https://github.com/dev-belly/StatementTrace/blob/main/tests/test_api.py)

**FastAPI / Pydantic / Uvicorn** 提供六个只读接口，支持公司与财年筛选、来源事实分页。
启动前捕获并核验数据包，请求读取同一份快照；金额通过 JSON 时保留为精确整数字符串，
缺失值保持 `null`。未知和重复参数返回 422。

数据层使用 **Polars → Parquet → DuckDB → dbt**，将同一组 24 条财报事实生成六个公司年度。
每条 SQL 路径与 Python 核对 138 个字段。可阅读
[管道实现](https://github.com/dev-belly/StatementTrace/blob/main/src/statementtrace/warehouse.py)、
[SQL 与 dbt 模型](https://github.com/dev-belly/StatementTrace/tree/main/warehouse_dbt/models)及
[管道说明](https://github.com/dev-belly/StatementTrace/blob/main/docs/WAREHOUSE.zh-CN.md)。

这是三家公司 FY2023–FY2024 的手工整理案例。API 本地运行，公开静态报告与服务端接口分别验收。

## 浏览器交互与独立重放

[PITBridge 立即试用](https://dev-belly.github.io/PITBridge/try/)：修改发票到达时间和决策时间，
查看选中的版本，分享 URL 状态，下载 JSON 后用 Python / SQLite 重放。
用一个小规模合成案例查看界面状态如何与可验证输入对应。
[下载后重放](START_HERE.md#download-and-replay-your-browser-scenario)。

## 可以继续展开的工程问题

- 为什么已经显示部分回复，仍必须等到明确的完成事件才纳入下一轮上下文？
- 取消请求与创建新会话时，如何避免较晚返回的响应写入错误会话？
- 为什么消息字符数合规，中文与 JSON 转义仍可能使请求超过字节上限？
- 为什么工具函数单测通过后，还需要启动真实 HTTP 服务验证？
- 前端如何区分缺失金额、合法的零和超过 Number 精度范围的整数？
- 分页请求跨越数据更新时，快照身份如何帮助保持一致？

金融数据与研究案例保留在 [三个代表作](README.md#三个代表作)和 [完整目录](CATALOG.md)。
下一阶段的学习与工程任务见 [当前优先级](OPEN_SOURCE_ROADMAP.zh-CN.md)。

[GitHub 主页](https://github.com/dev-belly) · [本地运行](START_HERE.md)
