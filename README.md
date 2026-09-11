# Automação de Cadastro de Cliente

Projeto de automação de testes desenvolvido em **Python**, utilizando **Playwright** e **Pytest**.

## 🚀 Tecnologias utilizadas

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* Git e GitHub

## 📋 Cenários automatizados

Atualmente, o projeto possui automações para:

* Acesso ao sistema
* Login
* Acesso ao cadastro de clientes
* Preenchimento do nome do cliente
* Seleção da cidade pelo código
* Gravação do cliente
* Exclusão do cliente

## 📁 Estrutura do projeto

```text
cliente/
│
├── pages/
│   ├── cliente_page.py
│   └── login_page.py
│
├── tests/
│   ├── test_cliente.py
│   └── test_login.py
│
├── conftest.py
├── pytest.ini
├── .gitignore
└── README.md
```

## ▶️ Executando os testes

### 1. Instalar as dependências

```bash
pip install playwright pytest pytest-playwright
```

### 2. Instalar os navegadores do Playwright

```bash
playwright install
```

### 3. Executar todos os testes

```bash
pytest
```

### 4. Executar os testes com o navegador visível

```bash
pytest --headed --browser=chromium
```

## 🎯 Objetivo

Este projeto foi desenvolvido com o objetivo de praticar **automação de testes utilizando Python, Playwright e Pytest**, aplicando conceitos de:

* Page Object Model (POM)
* Locators
* Assertions
* Fixtures
* Organização de testes automatizados

## 📌 Próximos passos

* [ ] Adicionar novos cenários de cadastro
* [ ] Validar campos obrigatórios
* [ ] Validar mensagens de erro
* [ ] Melhorar as validações de exclusão
* [ ] Criar mais cenários negativos
* [ ] Evoluir a estrutura do projeto
* [ ] Adicionar geração de relatórios de testes
* [ ] Melhorar a cobertura dos testes

---

**Projeto desenvolvido para fins de estudo e prática em automação de testes.**
