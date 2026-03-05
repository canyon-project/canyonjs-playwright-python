"""
覆盖率收集 fixture 实现。
"""
import json
import time
from pathlib import Path

import pytest
from playwright.sync_api import BrowserContext


def create_coverage_context_fixture(
    output_dir: str = ".canyon_output",
):
    """
    创建覆盖率 context fixture，类似 @canyonjs/playwright 的 createCoverageContextFixture。

    用法（在 conftest.py 中）:
        from canyonjs_playwright import create_coverage_context_fixture
        coverage_context = create_coverage_context_fixture(output_dir=".canyon_output")

    或使用 pytest 插件（自动注册，无需 conftest）:
        pip install canyonjs-playwright
        # 插件会自动提供 coverage_context，并 override page 以自动启用
    """
    output_path = Path(output_dir)

    @pytest.fixture
    def coverage_context(context: BrowserContext) -> BrowserContext:
        """在 context 中注入 Istanbul 覆盖率收集逻辑。"""
        context.add_init_script(
            """
            window.addEventListener('beforeunload', () => {
                if (window.collectIstanbulCoverage && window.__coverage__) {
                    window.collectIstanbulCoverage(window.__coverage__);
                }
            });
            """
        )

        output_path.mkdir(parents=True, exist_ok=True)

        def collect_istanbul_coverage(coverage):
            if coverage is not None:
                file_path = output_path / f"coverage-{time.time_ns()}.json"
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(coverage, f, ensure_ascii=False, indent=2)

        context.expose_function("collectIstanbulCoverage", collect_istanbul_coverage)

        yield context

        for page in context.pages:
            try:
                page.evaluate(
                    """
                    () => {
                        if (window.collectIstanbulCoverage && window.__coverage__) {
                            window.collectIstanbulCoverage(window.__coverage__);
                        }
                    }
                    """
                )
            except Exception:
                pass

    return coverage_context
