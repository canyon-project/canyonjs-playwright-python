"""
pytest 插件：自动注册 coverage_context，并 override page 以自动启用覆盖率收集。
"""
import os

import pytest
from playwright.sync_api import BrowserContext, Page

from canyonjs_playwright.fixtures import create_coverage_context_fixture

# 默认输出目录，可通过环境变量 CANYON_OUTPUT_DIR 覆盖
_output_dir = os.environ.get("CANYON_OUTPUT_DIR", ".canyon_output")
coverage_context = create_coverage_context_fixture(output_dir=_output_dir)


@pytest.fixture
def page(context: BrowserContext, coverage_context: BrowserContext) -> Page:
    """Override pytest-playwright 的 page，确保 coverage_context 先于 page 执行。"""
    return context.new_page()
