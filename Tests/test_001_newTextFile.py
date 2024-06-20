import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Tests.base_test import BaseTest


class TestNewTextFile(BaseTest):
    @pytest.fixture(scope="function")
    def setup(self):
        pass

    def test_newtextfile(self, setup):
        """
        - Test scenario:
            1. Launch VS Code.
            2. Click on File menu.
            3. Select New Text File.
            4. Validate a new page with title 'Untitled-1' is created.
        :param setup:
        :return:
        """
        try:
            self.cef_driver.find_element(By.XPATH, "//div[@aria-label='File']").click()
            time.sleep(1)
            self.cef_driver.find_element(By.XPATH, "//div[@aria-label='Edit']").click()
            time.sleep(1)
            self.cef_driver.find_element(By.XPATH, "//div[@aria-label='Selection']").click()
            time.sleep(1)
            self.cef_driver.find_element(By.XPATH, "//div[@aria-label='View']").click()
            time.sleep(1)

        except NoSuchElementException as NSE:
            pytest.fail(f"Element not found: {NSE}")
        except Exception as e:
            pytest.fail(f"Unknown exception occurred: {e}")
