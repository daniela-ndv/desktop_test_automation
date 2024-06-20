import pytest


@pytest.mark.usefixtures("cef_driver_init")
class BaseTest:
    """
    This is the Parent class of all the test classes.
    """
    pass
