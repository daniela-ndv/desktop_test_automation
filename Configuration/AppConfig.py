import os

class AppConfig:
    """
    Configurações da aplicação
    """
    # Versão do ChromeDriver correspondente à versão do CEF usado no VS Code.
    # Para verificar a versão do Chrome no VS Code, navegue até Help>Toggle Developer Tools e rode o seguinte comando no console:
    # console.log(navigator.appVersion)
    CHROME_DRIVER_VERSION = "138.0.7204.235"

    USER_HOME = os.path.expanduser("~")
    APP_PATH = os.path.join(
        USER_HOME,
        r"AppData\Local\Programs\Microsoft VS Code\Code.exe"
    )
    APP_TITLE = "Visual Studio Code"
