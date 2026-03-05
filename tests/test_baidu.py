import re

from playwright.sync_api import Page, expect


def test_baidu_title(page: Page):
    """打开 baidu.com 并断言页面标题"""
    page.goto("https://www.baidu.com")
    expect(page).to_have_title(re.compile("百度"))
