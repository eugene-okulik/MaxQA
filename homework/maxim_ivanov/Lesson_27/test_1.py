from playwright.sync_api import Page, expect


def test_confirm_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link", name="Click").click()
    page.get_by_text("You selected Ok").click()
    selected_text = page.locator("#result")
    result_text = "You selected Ok"
    expect(selected_text).to_have_text(result_text)
