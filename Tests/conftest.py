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
    - Selenium WebDriver is initialized here for handling elements inside CEF browser.
    ---
    :param request:
    :return:
    """

    """find an available port to start WebDriver with remote-debugging."""
    port_number = GenericUtilities.find_available_port(AutoConfig.PORT_START, AutoConfig.PORT_RANGE)
    if port_number is None:
        pytest.fail(f"no available ports in given range "
                    f"from {AutoConfig.PORT_START} to {AutoConfig.PORT_START + AutoConfig.PORT_RANGE}. "
                    f"WebDriver can't be initialized.")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = AppConfig.APP_PATH
    chrome_options.add_argument(f"--remote-debugging-port" + "=" + str(port_number))
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chrome_driver_path = ChromeDriverManager(driver_version=AppConfig.CHROME_DRIVER_VERSION).install()
    service = Service(executable_path=chrome_driver_path,
                      log_output=AutoConfig.LOG_PATH)

    request.cls.cef_driver = webdriver.Chrome(service=service, options=chrome_options)

    """ Implicit wait time: to wait for max 10 seconds before throwing exception. """
    request.cls.cef_driver.implicitly_wait(10)

    """ Maximize application """
    request.cls.cef_driver.execute_script("window.moveTo(0, 0);window.resizeTo(screen.width, screen.height);")
    yield
    request.cls.cef_driver.quit()
