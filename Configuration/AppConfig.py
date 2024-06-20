class AppConfig:
    """
    - Configurations related to Application
    """
    # Version of ChromeDriver corresponding to CEF version used in VS Code.
    # To check the Chrome version, In VS Code, navigate to Help>Toggle Developer Tools and run this command in Console:
    # console.log(navigator.appVersion)
    CHROME_DRIVER_VERSION = "122.0.6261.156"

    APP_PATH = r"C:\Program Files\Microsoft VS Code\Code.exe"
    APP_TITLE = "Visual Studio Code"
