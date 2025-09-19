import pytest

@pytest.mark.usefixtures("cef_driver_init")
class BaseTest:
    """
    Esta é a classe pai de todas as classes de teste.
    """
    pass
