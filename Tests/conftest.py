from Configuration.AutoConfig import AutoConfig
from Configuration.AppConfig import AppConfig
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Utilities.GenericUtilities import GenericUtilities
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="class")
def cef_driver_init(request):
    """
    O Selenium WebDriver é inicializado aqui para manipular elementos dentro do navegador CEF.
    """

    """ Encontra uma porta disponível para iniciar o WebDriver com depuração remota. """
    port_number = GenericUtilities.find_available_port(AutoConfig.PORT_START, AutoConfig.PORT_RANGE)
    if port_number is None:
        pytest.fail(f"Nenhuma porta disponível no intervalo fornecido "
                    f"de {AutoConfig.PORT_START} até {AutoConfig.PORT_START + AutoConfig.PORT_RANGE}. "
                    f"O WebDriver não pode ser inicializado.")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = AppConfig.APP_PATH
    chrome_options.add_argument(f"--remote-debugging-port" + "=" + str(port_number))
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chrome_driver_path = ChromeDriverManager(driver_version=AppConfig.CHROME_DRIVER_VERSION).install()
    service = Service(executable_path=chrome_driver_path,
                      log_output=AutoConfig.LOG_PATH)

    request.cls.cef_driver = webdriver.Chrome(service=service, options=chrome_options)

    """ Tempo de espera implícito: esperar no máximo 10 segundos antes de lançar uma exceção. """
    request.cls.cef_driver.implicitly_wait(10)

    """ Maximizar a aplicação """
    request.cls.cef_driver.execute_script("window.moveTo(0, 0);window.resizeTo(screen.width, screen.height);")
    yield
    request.cls.cef_driver.quit()
