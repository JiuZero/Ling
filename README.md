![z0scan](https://socialify.git.ci/JiuZero/Ling/image?description=1&font=Raleway&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FJiuZero%2FLing%2Frefs%2Fheads%2Fmain%2Fdoc%2Flogo.png&owner=1&pattern=Solid&theme=Auto)

<h4 align="center" dir="auto">
  <a href="https://github.com/JiuZero/Ling/releases">发行版</a> •
  <a href="https://github.com/JiuZero/Ling/blob/master/doc/CHANGELOG.MD">更新日志</a>
</h4>

<p align="center">
  <a href="https://github.com/JiuZero/Ling/stargazers"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/JiuZero/Ling?style=for-the-badge"></a>
  <a href="https://github.com/JiuZero/Ling/issues"><img alt="Issues" src="https://img.shields.io/github/issues/JiuZero/Ling?style=for-the-badge"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge">
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-8A2BE2?style=for-the-badge">
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/JiuZero/Ling?style=for-the-badge">
</p>

---

## ✨ 项目简介

Ling 是由 z0scan 而衍生的基于 PyQt5 与 QFluentWidgets 构建的图形化界面（GUI）

它提供直观易用的界面来驱动 z0scan 执行主动/被动扫描、插件启停、结果筛选与报告导出，适合希望以可视化方式快速开展 Web 安全测试的用户。

- 运行核心：调用 z0scan（z0 或 z0.exe、或 z0.py）
- UI 组件：PyQt5 + QFluentWidgets（支持 Fluent 风格）
- 主题支持：Light/Dark,深色主题附带 dark.qss
- 报告支持：解析 z0 输出中的 JSON Report Path 并载入结果，支持导出 HTML/JSON

> [!WARNING]
> Ling 不包含 z0scan 核心, 需本地存在可用的 z0 可执行文件或脚本。

---

## ✨ 核心特性

- 可视化操作
  - 主动扫描：输入单个 URL、或批量 URL 文件
  - 被动扫描：对接代理流量（默认 127.0.0.1:5920）
  - 扫描参数：线程、级别、风险、超时、代理、仅加载/禁用插件等
- 插件管理
  - 自动读取 scanners 目录下 PerPage/PerDir/PerDomain/PerHost 四类插件
  - 支持按风险过滤、关键字搜索、一键启用/禁用
- 结果与报告
  - 风险、类型筛选与详情查看（验证步骤/细节树）
  - 保存 JSON 结果、导出 HTML 报告
- 主题与配置
  - Light/Dark 切换（Dark 下自动加载 dark.qss）
  - 设置页可指定 z0 可执行路径、在线编辑 z0 的 config/config.py

---

## 📦 安装

请先准备 Python 3.8+ 环境

```bash
git clone https://github.com/JiuZero/Ling
cd Ling
pip install -r requirements.txt
python3 ling.py
```

---

## 🚀 快速开始

1) 准备 z0 可执行文件或脚本
- 推荐将 z0.exe（Windows）或 z0（Unix），或 z0.py 放在运行 Ling 的同一目录
- 或在 Ling 设置页手动指定 z0 路径（支持 .exe/.py）

2) 启动 GUI
```bash
python ling.py
```

3) 基本用法
- 主动扫描：选择“主动扫描”，在“目标URL/文件”中填入：
  - 单 URL 示例: https://example.com/?id=1
  - 文件示例: urls.txt（每行一个 URL）
- 被动扫描：选择“被动扫描”，设置代理监听地址，默认 127.0.0.1:5920
- 扫描参数：
  - 级别: 0/1/2/3
  - 风险: 支持多选（0,1,2,3）
  - 线程: 默认 10
  - 代理 -p、超时 --timeout、控制台端口 -c、插件线程 -pt、仅加载 --enable、禁用 --disable 等
- 报告解析：
  - Ling 会监听 z0 输出中形如“JSON Report Path: xxx.json”的行，并自动加载该 JSON 报告
- 导出：
  - “扫描结果”页可保存 JSON 或导出 HTML 报告

---

## 🧩 插件视图

Ling 会扫描项目 scanners 目录下的四类插件（若存在）：
- PerPage
- PerDir
- PerDomain
- PerHost

支持能力：
- 列表勾选启用/禁用
- 按风险（0/1/2/3）与关键字过滤
- 点击项查看插件元信息：name/desc/version/risk/path

说明：
- 插件信息通过正则从脚本中提取 name/desc/version/risk
- 风险颜色：3 红、2 橙、1 黄、0 绿

提示：本仓库未附带 scanners 目录与插件，请将其与 z0scan 保持对应结构以展示。

---

## 🖼️ 截图

请将你的截图放置于 doc/ 目录，并在此更新引用路径：
- 可视化主界面

![gui](doc/example1.png)

- 插件管理

![plugins](doc/example2.png)

- 扫描结果

![results](doc/example3.png)

---

## ❓常见问题

- 无法找到 z0？
  - 将 z0.exe/z0/z0.py 放到 Ling 同目录，或在“设置”页指定 z0 路径
- 未显示插件列表？
  - 确认 scanners/PerPage|PerDir|PerDomain|PerHost 目录存在且含 .py 插件
- 扫描完成未载入结果？
  - 确保 z0 输出包含 “JSON Report Path: xxx.json”，并且该文件能被读取
  - 确保 z0 的扫描已结束（被动扫描需手动结束）

---

## 🔗 联系

<table>
  <tr>
    <td width="25%" valign="top">
      <h3>公众号</h3>
      <ul>
        <li><b>90Safe</b> - 安全资讯</li>
      </ul>
    </td>
    <td width="25%" valign="top">
      <h3>微信</h3>
      <ul>
        <li><b>JiuZer1</b> - 不怎么看…</li>
      </ul>
    </td>
    <td width="25%" valign="top">
      <h3>QQ</h3>
      <ul>
        <li><b>1703417187</b> - 偶尔在线</li>
      </ul>
    </td>
    <td width="25%" valign="top">
      <h3>QQ交流群</h3>
      <ul>
        <li><b>1058256508</b> - 问题咨询</li>
      </ul>
    </td>
  </tr>
</table>

---

## 💖 Star 趋势

<p align="center">
  <a href="https://star-history.com/#JiuZero/Ling&Date">
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=JiuZero/Ling&type=Date" width="85%">
  </a>
</p>