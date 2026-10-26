# 参与改进 / Contributing

欢迎修复失效链接、补充可复现步骤、纠正项目说明，或指出结论与证据不一致的地方。
This repository hosts the GitHub profile and portfolio documentation. For a
project's code or runtime issue, use that project's own repository and contribution guide.

## 先选入口 / Choose the right place

- 试运行项目：从 [Start here](START_HERE.md) 选择路线，记录卡住的具体步骤。
- 主页、导航或文档错误：在[此仓库提交问题](https://github.com/dev-belly/dev-belly/issues/new/choose)。
- 项目实现问题：到对应项目提 Issue，附仓库、版本或 commit、运行环境和最小样例。
- 涉及凭据、个人数据或可利用漏洞：先读 [Security](SECURITY.md)，不要公开敏感内容。

## 修改与本地检查 / Edit and check

使用 Python 3.12+，在仓库根目录运行：

```bash
python scripts/build_profile_assets.py
python scripts/build_project_catalog.py
python scripts/build_project_catalog.py --check
python scripts/check_profile.py
```

图片由 `scripts/build_profile_assets.py` 生成；需要修改时编辑生成器并一并提交生成结果。
项目目录从 `portfolio.json` 生成；修改条目后提交 `CATALOG.md`，由 CI 检查二者一致。
保留准确的链接和图片说明文字，检查中文、英文、折叠区与移动端阅读顺序。
The profile checks cover generated assets and local navigation; they do not prove
that a remote service is available or that a research claim is correct.

## 提交内容 / What to include

1. 说明访问者遇到的问题、修改后的行为，以及涉及的文档或项目。
2. 新增数值、版本、性能或能力说明时，链接到对应数据、方法、代码或保存的验证记录。
3. 区分真实数据、合成样例、回溯研究和生产运行；同时保留适用边界与负面结果。
4. 写明实际执行的检查和结果；没有运行的步骤明确标注，避免把预期结果写成已验证结果。

Keep each pull request focused and reviewable. Do not include credentials,
private customer records, or third-party material you are not allowed to share.
No response or release schedule is guaranteed.
