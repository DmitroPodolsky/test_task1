from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement


class Page:
    """Base class for all pages in the app"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_element(self, element: WebElement):
        element.click()

    def find_element(self, xpath: str):
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        return element

    def send_keys_to_element(self, element: WebElement, text: str):
        element.send_keys(text)

    def find_and_click(self, xpath: str):
        element = self.find_element(xpath)
        self.click_element(element)
        return element
