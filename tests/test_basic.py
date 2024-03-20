import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://127.0.0.1:8000")
    expect(page).to_have_title(re.compile("Home"))

def test_link_about(page: Page):
    page.goto("http://127.0.0.1:8000")

    # Click the get started link.
    page.get_by_role("link", name="About page").click()
    # Expects page to have a heading with the name of Installation.
    expect(page).to_have_title(re.compile("About"))

def id_click_and_expect(page:Page, element_id:str, expect_site:str):
    page.locator(element_id).click()
    expect(page).to_have_title(re.compile(expect_site))

def test_nav_list(page: Page):
    page.goto("http://127.0.0.1:8000")
    id_click_and_expect(page, "#nav_about", "About")
    id_click_and_expect(page, "#nav_home", "Home")
    id_click_and_expect(page, "#nav_login", "Login")
    id_click_and_expect(page, "#nav_register", "Register")
