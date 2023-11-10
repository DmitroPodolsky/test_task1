from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement


class Page:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, element: WebElement):
        element.click()

    def find_element(self, xpath: str):
        element = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        return element

    def send_keys_to_element(self, element: WebElement, text: str):
        element.send_keys(text)
