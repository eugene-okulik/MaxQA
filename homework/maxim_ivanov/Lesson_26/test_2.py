from playwright.sync_api import Page
import re


def test_get_started_link(page: Page):
    page.goto("https://demoqa.com/automation-practice-form", wait_until='domcontentloaded')
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("Max")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("Ivanov")
    page.get_by_placeholder("name@example.com").click()
    page.get_by_placeholder("name@example.com").fill("test@mail.com")
    page.get_by_text("Male", exact=True).click()
    page.get_by_placeholder("Mobile Number").click()
    page.get_by_placeholder("Mobile Number").fill("1234567890")
    page.locator("#dateOfBirthInput").click()
    page.get_by_role("combobox").nth(1).select_option("1944")
    page.get_by_label("Choose Wednesday, June 7th,").click()
    page.locator(".subjects-auto-complete__value-container").click()
    page.locator("#subjectsInput").fill("P")
    page.get_by_text("Physics", exact=True).click()
    page.get_by_text("Sports").click()
    page.get_by_placeholder("Current Address").click()
    page.get_by_placeholder("Current Address").fill("New Daily")
    page.locator("div").filter(has_text=re.compile(r"^Select State$")).nth(3).click()
    page.get_by_text("Uttar Pradesh", exact=True).click()
    page.get_by_text("Select City").click()
    page.get_by_text("Agra", exact=True).click()
    page.get_by_role("button", name="Submit").click()
