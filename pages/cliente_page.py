from playwright.sync_api import Page, expect


class ClientePage:

    def __init__(self, page: Page):
        self.page = page

    def acessar_cadastro(self):

        campo_pesquisa = self.page.locator(
            "[data-test='search-screen-input']"
        )

        campo_pesquisa.press_sequentially(
            "cadastro de cliente",
            delay=100
        )

        opcao_cliente = self.page.get_by_role("option")

        expect(opcao_cliente).to_be_visible(timeout=10000)

        opcao_cliente.click()

        self.page.wait_for_timeout(5000)

    def criar_cadastro(self, nome, codigo_cidade):

        self.page.locator(
            "[data-test='txtNome']"
        ).fill(nome)

        campo_cidade = self.page.locator(
            "[data-test='txtCidade']"
        )

        campo_cidade.click()

        campo_cidade.press_sequentially(
            codigo_cidade,
            delay=100
        )

        # Confirma o código digitado
        campo_cidade.press("Enter")

        # Confirma que a cidade foi selecionada
        cidade_selecionada = self.page.get_by_text(
            "ARARAQUARA - Brasil",
            exact=True
        )

        expect(cidade_selecionada).to_be_visible()

    def gravar_cliente(self):
        self.page.get_by_role(
            "button",
            name="Gravar",
            exact=True
        ).click()

        expect(
            self.page.get_by_text(
            "gravado com sucesso"
        )
    ).to_be_visible(
        timeout=20000
    )

    def excluir_cliente(self):
        self.page.get_by_role(
            "button",
            name="Excluir",
            exact=True
        ).click()

        botao_sim = self.page.get_by_role(
            "button",
            name="Sim",
            exact=True
        )

        expect(botao_sim).to_be_visible(timeout=5000)

        botao_sim.click()

        expect(
            self.page.get_by_text(
                "Registro excluído com sucesso"
            )
        ).to_be_visible(
            timeout=5000
        )