import os


class AutoConfig:
    """
    Configuration for UI Automation Framework
    """
    ROOT_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    TESTDATA_PATH = os.path.join(ROOT_DIR, "Test Data", "config.csv")
    LOG_PATH = os.path.join(ROOT_DIR, "WebDriver.log")
    LOGGER_PATH = os.path.join(ROOT_DIR, "Logger.log")

    PORT_START = 7900
    PORT_RANGE = 10
