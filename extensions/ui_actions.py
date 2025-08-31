from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class UiActions:

    @staticmethod
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    def update_text(elem: WebElement, value):
        elem.send_keys(value)

    @staticmethod
    def mouse_hover(elem: WebElement):
        elem.click()

    @staticmethod
    def get_popup_text(driver:WebDriver):
        popup = driver.switch_to.alert.text
        print(f"The text is {popup}")

