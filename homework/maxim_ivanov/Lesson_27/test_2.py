from playwright.sync_api import Page, expect


def test_confirm_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")

    click_button = page.locator("text=Click")
    click_button.wait_for(state='visible', timeout=60000)

    with page.expect_popup() as new_tab_info:
        page.click("text=Click")

    new_tab = new_tab_info.value

    expect(new_tab.locator("#result-text")).to_have_text("I am a new page in a new tab")
    expect(page.locator("text=Click")).to_be_enabled()
