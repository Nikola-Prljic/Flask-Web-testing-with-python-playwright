import re
import sys
from playwright.sync_api import Page, expect
from create_database.create_database_tabels import reset_database

#expect a empty database!

def register(page: Page, username, password):
    page.locator("#nav_register").click()
    expect(page).to_have_title(re.compile("Register"))
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("#register_button").click()
    login(page, "niki", "96")
    expect(page).to_have_title(re.compile("Home"))

def login(page: Page, username, password):
    page.locator("#nav_login").click()
    expect(page).to_have_title(re.compile("Login"))
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login_button").click()

def make_post(page: Page, username, text):
    page.locator("#nav_create").click()
    expect(page).to_have_title(re.compile("Create"))
    page.locator("#message").fill(text)
    page.locator("#submit_button").click()
    expect(page).to_have_title(re.compile("Posts"))
    expect(page.get_by_text(text)).to_contain_text(text)

def test_Unauthorized(page: Page):
    reset_database()
    page.goto("http://127.0.0.1:8000/posts")
    expect(page).to_have_title(re.compile("401 Unauthorized"))
    page.goto("http://127.0.0.1:8000/create")
    expect(page).to_have_title(re.compile("401 Unauthorized"))
    page.goto("http://127.0.0.1:8000")
    register(page, "niki", "96")
    page.goto("http://127.0.0.1:8000/login")
    expect(page).to_have_title(re.compile("Home"))
    page.goto("http://127.0.0.1:8000/register")
    expect(page).to_have_title(re.compile("Home"))

def test_login_and_post(page: Page):
    reset_database()
    page.goto("http://127.0.0.1:8000")
    register(page, "niki", "96")
    make_post(page, "niki", "hi")
    make_post(page, "niki", "yo")
    page.locator("#nav_logout").click()
    register(page, "eule", "96")
    make_post(page, "eule", "yup")
    page.locator("#nav_logout").click()
    for i in range(10):
        login(page, "eule", "96")
        make_post(page, "eule", "yup" + str(i))
        page.locator("#nav_logout").click()

def just_register(page:Page, username, password):
    page.locator("#nav_register").click()
    expect(page).to_have_title(re.compile("Register"))
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("#register_button").click()

def test_Name_is_already_taken(page: Page):
    reset_database()
    page.goto("http://127.0.0.1:8000")
    register(page, "niki", "96")
    page.locator("#nav_logout").click()
    just_register(page, "niki", "96")
    expect(page.locator("#flask-flash")).to_have_text("Name is already taken!")

def test_wrong_password(page: Page):
    reset_database()
    page.goto("http://127.0.0.1:8000")
    just_register(page, "eule", "96")
    login(page, "eule", "2012")
    expect(page.locator("#flask-flash")).to_have_text("Wrong Password!")
