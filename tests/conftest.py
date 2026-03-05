"""
启用 canyonjs-playwright，类似 baseTest.ts 的用法。

pytest_plugins 需放在最前面，确保在 pytest-playwright 之后加载，从而 override page fixture。
"""
import sys
from pathlib import Path

# 本地开发：将 src 加入 path，无需 pip install -e .
_root = Path(__file__).resolve().parent.parent
if str(_root / "src") not in sys.path:
    sys.path.insert(0, str(_root / "src"))

pytest_plugins = ["canyonjs_playwright.pytest_plugin"]
