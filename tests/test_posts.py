import re
from time import sleep
from playwright.sync_api import Page, expect

#expect a empty database!
def login(page: Page, username, password):
    page.goto("http://127.0.0.1:8000")
    page.locator("#nav_login").click()
    expect(page).to_have_title(re.compile("Login"))
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login_button").click()
    expect(page).to_have_title(re.compile("Home"))
    return page

def make_post(page: Page, username, text):
    page.locator("#nav_create").click()
    expect(page).to_have_title(re.compile("Create"))
    page.locator("#author").fill(username)
    page.locator("#message").fill(text)
    page.locator("#submit_button").click()
    expect(page).to_have_title(re.compile("Posts"))
    expect(page.locator("body > section > main > article > p")).to_have_text == "hi"

def test_login_and_post(page: Page):
    page = login(page, "a", "a")
    make_post(page, "a", "hi")

""" def test_tow_post(page: Page):
    createPostAndCheck(page, "niki", "bro", "#2")
    createPostAndCheck(page, "eule", "yo", "#3") """
