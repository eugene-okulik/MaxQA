from playwright.sync_api import expect, Page


def test_click_red_button(page: Page):
    page.goto("https://demoqa.com/dynamic-properties", wait_until="domcontentloaded", timeout=60000)
    button = page.locator("#colorChange")
    expect(button).to_have_css("color", "rgb(220, 53, 69)", timeout=60000)
    button.click()
