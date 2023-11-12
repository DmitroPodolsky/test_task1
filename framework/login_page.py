from .page import Page


class LoginPage(Page):
    """Class for login page"""

    def enter_email(self, email: str, xpath: str) -> None:
        email_element = self.find_and_click(xpath)
        self.send_keys_to_element(email_element, email)

    def enter_password(self, password: str, xpath: str) -> None:
        password_element = self.find_and_click(xpath)
        self.send_keys_to_element(password_element, password)
