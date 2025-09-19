import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Tests.base_test import BaseTest


class TestVsCode(BaseTest):
    @pytest.fixture(scope="function")
    def setup(self):
        pass

    def testOpenMenu(self, setup):
        """
        - Cenário de teste:
            1. Clicar no menu File.
            2. Clicar no menu Edit.
            3. Clicar no menu Selection.
            4. Clicar no menu View.
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
            pytest.fail(f"Elemento não encontrado: {NSE}")
        except Exception as e:
            pytest.fail(f"Ocorreu uma exceção inesperada: {e}")


    def testOpenSidebar(self):
        """
        - Cenário de teste:
            1. Clicar na seção Explorer na sidebar.
            2. Verificar se o título do menu lateral está sendo exibido.
        """
        
        try:
            self.cef_driver.find_element(By.XPATH, "//*[@id='workbench.parts.activitybar']/div/div[1]/div/ul/li[1]/a").click()
            time.sleep(1)

            element = self.cef_driver.find_element(By.XPATH, "//*[@id='workbench.parts.sidebar']/div[1]/div[1]/h2")
            
            assert "EXPLORER" in element.text, "O texto 'EXPLORER' não está presente no título h2"
            
            # if element.is_displayed():
            #     print("O elemento está visível")
            # else:
            #     print("O elemento existe, mas não está visível")

        except NoSuchElementException as NSE:
            pytest.fail(f"Elemento não encontrado: {NSE}")
        except Exception as e:
            pytest.fail(f"Ocorreu uma execeção inesperada: {e}")

