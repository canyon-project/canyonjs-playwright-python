# canyonjs-playwright-python

`@canyonjs/playwright` 的 Python 实现，为 Playwright Python 提供 Istanbul 覆盖率收集能力。

## 安装

```bash
pip install canyonjs-playwright
```

或从源码安装（开发模式）:

```bash
pip install -e .
```

## 用法

### 方式一：pytest_plugins（推荐，类似 baseTest.ts）

在 `conftest.py` 中添加一行即可自动启用，所有使用 `page` 的测试都会自动收集覆盖率：

```python
# conftest.py
pytest_plugins = ["canyonjs_playwright.pytest_plugin"]
```

测试用例无需修改，直接使用 `page`：

```python
def test_example(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
```

### 方式二：自定义输出目录

```python
# conftest.py
import os
os.environ["CANYON_OUTPUT_DIR"] = ".canyon_output"
pytest_plugins = ["canyonjs_playwright.pytest_plugin"]
```

### 方式三：手动使用 fixture

```python
# conftest.py
from canyonjs_playwright import create_coverage_context_fixture

coverage_context = create_coverage_context_fixture(output_dir=".canyon_output")
```

```python
# test_example.py
def test_example(page, coverage_context):
    page.goto("https://example.com")
```

## 运行步骤

### 1. 创建虚拟环境（推荐）

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# Windows: venv\Scripts\activate
```

### 2. 安装依赖

```bash
python -m pip install -r requirements.txt
```

### 3. 安装 Chromium 浏览器

```bash
python -m playwright install chromium
```

### 4. 运行测试

```bash
python -m pytest
```

### 可选参数

| 参数 | 说明 |
|------|------|
| `--headed` | 有界面模式运行（显示浏览器窗口） |
| `-v` | 详细输出 |
| `--tracing=retain-on-failure` | 失败时保留 trace 便于调试 |

## 项目结构

```
canyonjs-playwright-python/
├── src/
│   └── canyonjs_playwright/    # 包源码
│       ├── __init__.py
│       ├── fixtures.py
│       └── pytest_plugin.py
├── tests/
│   ├── conftest.py
│   ├── test_baidu.py
│   └── test_canyon.py
├── pyproject.toml
├── requirements.txt
├── pytest.ini
└── .github/workflows/
    └── playwright.yml
```

## 输出

覆盖率数据写入 `coverage-{timestamp}.json`，默认目录为 `.canyon_output`。

> 注意：仅当被测页面有 Istanbul 注入的 `window.__coverage__` 时才会生成覆盖率文件。

## 依赖

- Python >= 3.8
- playwright >= 1.40.0
- pytest-playwright >= 0.4.0

## CI

推送到 GitHub 后，GitHub Actions 会自动运行测试。失败时可在 Actions 页面下载 trace 文件，在 [trace.playwright.dev](https://trace.playwright.dev/) 查看。
