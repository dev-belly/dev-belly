# 安全反馈 / Security reporting

本仓库包含个人主页、项目导航和展示材料。项目代码的问题应报告到对应项目仓库。
This policy describes reporting routes; it does not claim that any repository has
private vulnerability reporting enabled or a guaranteed response time.

## 保护敏感信息 / Protect sensitive information

不要在公开 Issue、PR、截图或日志中放入令牌、密钥、账户信息、个人数据或可直接利用的漏洞细节。
发现自己的凭据泄露时，先在凭据提供方撤销或轮换它；删除页面内容不能使旧凭据失效。

## 报告路径 / Reporting route

1. 打开受影响项目的 **Security → Advisories**。如果页面提供 **Report a vulnerability**，使用该私密入口。
2. 如果没有私密入口，可提交仅请求安全联系渠道的公开 Issue；不要包含漏洞细节、敏感样例或凭据。
3. 普通失效链接、错字和不涉及敏感信息的文档问题，可使用[问题模板](https://github.com/dev-belly/dev-belly/issues/new/choose)。

For a private report, include the affected repository and commit or version,
expected and observed behavior, impact, and a minimal reproduction with synthetic
or redacted inputs. Share detailed reproduction material only through an agreed
private channel. There is no published support window or remediation deadline.
