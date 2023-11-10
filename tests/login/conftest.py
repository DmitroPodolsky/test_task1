import pytest

from framework.login_page import LoginPage


@pytest.fixture()
def user_login_fixture(driver):
    yield LoginPage(driver)
