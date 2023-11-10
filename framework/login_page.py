from .page import Page


class LoginPage(Page):
    def find_and_click(self, xpath: str):
        element = self.find_element(xpath)
        self.click_element(element)
        return element
