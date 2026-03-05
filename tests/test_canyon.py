import re

from playwright.sync_api import Page, expect


def test_canyon_title_contains_vite(page: Page):
    """打开 canyon-demo 并断言标题包含 Vite"""
    page.goto("http://canyon-demo.fat3.qa.nt.ctripcorp.com/")
    expect(page).to_have_title(re.compile("Vite", re.IGNORECASE))
