from playwright.sync_api import Page, expect


def test_get_started_link(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_label("Username").fill('MyLogin')
    page.get_by_label("Password").fill('MyPassword')
    page.get_by_role("button", name=" Login").click()
