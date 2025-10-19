from selenium.webdriver.remote.webelement import WebElement


class UiActions:

    @staticmethod
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    def update_text(elem: WebElement, value):
        elem.send_keys(value)