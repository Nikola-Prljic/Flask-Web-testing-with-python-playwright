import re
from playwright.sync_api import Page, expect
from create_database.create_database_tabels import reset_database
from test_posts_login import just_register, login

def login_wrong(page: Page, username, password, msg, flash_nr):
    login(page, username, password)
    expect(page.locator("#flask-flash-" + flash_nr)).to_have_text(msg)

def test_wrong_login_data(page: Page):
    reset_database()
    page.goto("http://127.0.0.1:8001")
    just_register(page, "eule", "96")
    login_wrong(page, "eule", "", "Password is empty", "0")
    login_wrong(page, "", "123", "Username is empty", "0")
    login_wrong(page, "", "", "Username is empty", "0")
    expect(page.locator("#flask-flash-1")).to_have_text("Password is empty")