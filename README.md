# VSCodeSelenium

Automação de testes para validar interações em interfaces de **aplicações desktop** que utilizam webview, utilizando **Python**, **Selenium** e **pytest**. 

Como exemplo, foi utilizado o **Visual Studio Code**, desenvolvido com Electron ((Fonte↗️)[https://code.visualstudio.com/docs/editor/whyvscode]).

**Este repositório foi baseado em [Abdulhasiib/VSCodeSelenium](https://github.com/Abdulhasiib/VSCodeSelenium.git)**

---

## 💻 Pré-requisitos

- Python 3.8+
- VS Code instalado  
- [ChromeDriver](https://chromedriver.chromium.org/) (gerenciado automaticamente pelo `webdriver-manager`)

---

## Configuração do Ambiente

1. Criar e ativar um ambiente virtual:

```
python -m venv venv
```

```
.\venv\Scripts\activate
```

2. Instalar dependências:

```
pip install -r requirements.txt
```

## Executando os Testes

Com o ambiente virtual ativo:

    pytest 

Ou para rodar um teste específico:

    pytest Tests/test_001_newTextFile.py -v

---

#### Configuração Importante

APP_PATH:
- No arquivo Configuration/AppConfig.py, defina o caminho para o executável do VS Code.

#### Dependências Principais

* **pytest**: framework de testes
* **selenium**: automação de navegador
* **webdriver-manager**: gerencia o ChromeDriver
* **psutil**: utilitários do sistema

#### Dicas
* Caso altere a versão do VS Code, verifique se o ChromeDriver é compatível com o Chromium embutido.