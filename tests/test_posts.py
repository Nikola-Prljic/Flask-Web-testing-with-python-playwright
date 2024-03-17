import re
from time import sleep
from playwright.sync_api import Page, expect

#expect a empty database!
def createPostAndCheck(page: Page, author, msg, expectedID):
    page.goto("http://127.0.0.1:8000")
    page.locator("#nav_create").click()
    expect(page).to_have_title(re.compile("Create"))
    page.locator("#author").fill(author)
    page.locator("#message").fill(msg)
    page.locator("#submit_button").click()
    expect(page).to_have_title(re.compile("Posts"))

    expect(page.locator("#a1")).to_have_text("hi")
    expect(page.locator("body > section > header > h2")).to_have_text(re.compile("Posts"))
    """ sleep(2)
    locator = page.locator("#1")
    expect(locator).to_have_text(re.compile("hi")) """

def test_one_post(page: Page):
    createPostAndCheck(page, "eule", "hi", "#1")

""" def test_tow_post(page: Page):
    createPostAndCheck(page, "niki", "bro", "#2")
    createPostAndCheck(page, "eule", "yo", "#3") """