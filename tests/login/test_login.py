from time import sleep

import pytest
from selenium.common.exceptions import NoSuchElementException

from framework.login_page import LoginPage
from utils.config import settings


def is_user_logged_in(user_login_fixture: LoginPage) -> bool:
    """Check if user is logged in by looking for the menu button"""
    try:
        user_login_fixture.find_element(
            '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
        )
        return True
    except NoSuchElementException:
        return False


@pytest.mark.parametrize(
    "email, password", [(settings.USER_EMAIL, settings.USER_PASSWORD)]
)
def test_user_login_success(user_login_fixture: LoginPage, email: str, password: str) -> None:
    user_login_fixture.find_and_click(
        '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button'
    )

    user_login_fixture.enter_email(
        email,
        '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]',
    )

    user_login_fixture.enter_password(
        password,
        '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]',
    )

    user_login_fixture.find_and_click(
        '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
    )
    sleep(5)

    assert True == is_user_logged_in(user_login_fixture)


@pytest.mark.parametrize("email, password", [(settings.USER_EMAIL, "1")])
def test_user_login_failure(user_login_fixture: LoginPage, email: str, password: str) -> None:
    user_login_fixture.find_and_click(
        '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button'
    )

    user_login_fixture.enter_email(
        email,
        '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]',
    )

    user_login_fixture.enter_password(
        password,
        '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]',
    )

    user_login_fixture.find_and_click(
        '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
    )
    sleep(5)

    assert False == is_user_logged_in(user_login_fixture)
