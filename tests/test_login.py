
from playwright.sync_api import Page

from pages.login_page import LoginPage


def test_login(page: Page):

    login = LoginPage(page)

    login.acessar()

    login.logar(
        "admin",
        "123456"
    )
