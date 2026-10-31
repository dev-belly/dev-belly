"""Build the public project directory from portfolio.json, using only stdlib."""

import argparse
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    "flagship": "先试这三个 / Start here",
    "financial": "财务、审计与清偿 / Financial systems",
    "research": "量化与研究实验 / Research experiments",
    "applications": "应用与早期作品 / Applications",
}
REQUIRED = {"repo", "group", "summary", "stack", "boundary"}
OPTIONAL = {"demo", "evidence"}


def validate(data):
    if set(data) != {"schema_version", "owner", "projects"}:
        raise ValueError("Unexpected portfolio fields")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError("Unsupported portfolio schema")
    if data["owner"] != "dev-belly":
        raise ValueError("The portfolio owner must be dev-belly")
    projects = data["projects"]
    if not isinstance(projects, list) or not projects:
        raise ValueError("Projects must be a nonempty list")
    seen = set()
    for project in projects:
        if not isinstance(project, dict) or not REQUIRED <= set(project):
            raise ValueError("A project is missing required fields")
        if set(project) - REQUIRED - OPTIONAL:
            raise ValueError("Unknown project fields")
        for value in project.values():
            if not isinstance(value, str) or not value.strip() or any(
                char in value for char in "\n\r|"
            ):
                raise ValueError("Project fields must be nonempty single-line table text")
        repo = project["repo"]
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", repo):
            raise ValueError(f"Invalid repository name: {repo}")
        if repo.casefold() in seen:
            raise ValueError(f"Duplicate repository: {repo}")
        seen.add(repo.casefold())
        if project["group"] not in GROUPS:
            raise ValueError(f"Unknown project group: {repo}")
        if "evidence" in project:
            evidence = project["evidence"]
            path = PurePosixPath(evidence)
            if path.is_absolute() or ".." in path.parts or "\\" in evidence:
                raise ValueError(f"Evidence must stay inside its repository: {repo}")
        if "demo" in project:
            parts = urlsplit(project["demo"])
            if (
                parts.scheme != "https"
                or parts.hostname not in {"dev-belly.github.io", "colab.research.google.com"}
                or parts.username is not None
                or parts.password is not None
                or parts.port is not None
            ):
                raise ValueError(f"Unexpected public demo URL: {repo}")
    return projects


def render(data):
    projects = validate(data)
    lines = [
        "# 项目目录 / Project directory",
        "",
        "<!-- Generated from portfolio.json; run python scripts/build_project_catalog.py. -->",
        "",
        f"这里收录 **{len(projects)} 个公开项目**，按使用目的组织。先打开 README 确认环境，再按对应证据复现。",
        "目录不把公开源码、静态演示或 CI 通过等同于生产部署、实盘表现或第三方认证。",
        "",
        "| 你想做什么 | 推荐路线 |",
        "| :--- | :--- |",
        "| 不安装环境，先改一个输入 | [PITBridge 浏览器发票案例](https://dev-belly.github.io/PITBridge/try/) |",
        "| 把浏览器情景带回本地核验 | [下载当前输入并独立重放](START_HERE.md#download-and-replay-your-browser-scenario) |",
        "| 看信贷分析或数据岗位作品 | CreditVintage → PITBridge → StatementTrace |",
        "| 看量化研究与工程 | AlphaForge → TradeForge → StressAtlas；再看保留负结果的图模型与区间实验 |",
        "| 看审计、会计与内控 | AuditLens → ControlTrace → LedgerX |",
        "| 看应用开发 | WeCom Agent → Personal AI Chat → 两个微信小程序 |",
        "",
        "[空目录安装与逐步试用](START_HERE.md) · [成果与代码](PROJECT_BRIEFS.md) · [验证记录](PROJECT_REVIEW.md)",
        "",
    ]
    for key, title in GROUPS.items():
        lines += [f"## {title}", "", "| 项目与入口 | 解决的问题 / 技术 | 数据与使用边界 |", "| :--- | :--- | :--- |"]
        for project in projects:
            if project["group"] != key:
                continue
            base = f"https://github.com/{data['owner']}/{project['repo']}"
            links = [f"[**{project['repo']}**]({base})", f"[README]({base}/blob/main/README.md)"]
            if "demo" in project:
                links.append(f"[试用 / 报告]({project['demo']})")
            if "evidence" in project:
                route = "tree" if project["evidence"].endswith("/") else "blob"
                links.append(f"[证据 / 方法]({base}/{route}/main/{quote(project['evidence'], safe='/')})")
            lines.append(f"| {' · '.join(links)} | {project['summary']}<br />{project['stack']} | {project['boundary']} |")
        lines.append("")
    lines += [
        "## 反馈与参与 / Feedback and contribution",
        "",
        "主页导航、文字与目录问题请到 [主页 Issues](https://github.com/dev-belly/dev-belly/issues/new/choose)；",
        "项目运行错误请到对应仓库的 Issues，附 commit 或版本、系统环境、完整命令和最小合成输入。",
        "仓库内的 SUPPORT、CONTRIBUTING 与 SECURITY 文件分别说明试用、贡献和安全报告路径。",
        "许可证与数据使用条件以各仓库的实际声明为准。",
        "",
        "维护目录时编辑 [portfolio.json](portfolio.json)，然后运行 `python scripts/build_project_catalog.py`。",
        "`--check` 和主页 CI 离线核对结构与生成结果；不会把远端站点的实时可用性作为已通过的结论。",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the catalog needs rebuilding")
    args = parser.parse_args()
    try:
        data = json.loads((ROOT / "portfolio.json").read_text(encoding="utf-8"))
        expected = render(data)
        target = ROOT / "CATALOG.md"
        if args.check:
            if not target.is_file() or target.read_text(encoding="utf-8") != expected:
                raise ValueError("CATALOG.md is stale; run scripts/build_project_catalog.py")
            print(f"Catalog checks passed: {len(data['projects'])} public projects across {len(GROUPS)} groups.")
        else:
            target.write_text(expected, encoding="utf-8", newline="\n")
            print(f"Built CATALOG.md for {len(data['projects'])} public projects.")
    except (ValueError, OSError, TypeError) as error:
        raise SystemExit(f"Catalog check failed: {error}")


if __name__ == "__main__":
    main()
