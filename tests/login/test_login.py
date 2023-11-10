from time import sleep

from selenium.common.exceptions import NoSuchElementException

from framework.login_page import LoginPage
from utils.config import settings


def is_user_logged_in(user_login_fixture: LoginPage) -> bool:
    try:
        user_login_fixture.find_element(
            '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
        )
        return True
    except NoSuchElementException:
        return False


def test_user_login(user_login_fixture: LoginPage):
    user_login_fixture.find_and_click(
        '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button'
    )

    email_element = user_login_fixture.find_and_click(
        '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'
    )
    user_login_fixture.send_keys_to_element(email_element, settings.USER_EMAIL)

    password_element = user_login_fixture.find_and_click(
        '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'
    )
    user_login_fixture.send_keys_to_element(password_element, settings.USER_PASSWORD)

    user_login_fixture.find_and_click(
        '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button'
    )
    sleep(5)

    assert True == is_user_logged_in(user_login_fixture)
