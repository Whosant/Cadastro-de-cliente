from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.cliente_page import ClientePage


def test_acessar_cadastro_cliente(page: Page):

    login = LoginPage(page)
    cliente = ClientePage(page)

    login.acessar()

    login.logar(
        "admin",
        "123456"
    )

    cliente.acessar_cadastro()

    cliente.criar_cadastro(
        "Wesley",
        "8133"
    )

    cliente.gravar_cliente()

    cliente.excluir_cliente()