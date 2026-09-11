from playwright.sync_api import Page, expect
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
    def acessar(self):
        self.page.goto("http://localhost/Login")

    def logar(self, usuario, senha):
        self.page.locator(
            "[data-test='username']"
        ).fill(usuario)

        self.page.get_by_placeholder(
            "Digite aqui a sua senha"
        ).fill(senha)

        with self.page.expect_response(
                lambda response:
                "/api/Principal/VerificaServicos" in response.url
                and response.ok
        ):
            self.page.locator(
                "[data-test='login-btn']"
            ).click()