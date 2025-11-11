from selenium.webdriver.remote.webelement import WebElement

# Common UI interaction helpers for readability and consistency
class UiActions:

    @staticmethod
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    def update_text(elem: WebElement, value):
        elem.send_keys(value)