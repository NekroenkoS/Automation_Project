from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

header = (By.XPATH, "//div[@class='sweet-alert  showSweetAlert visible']/h2")


class AfterPurchasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_header_element(self):
        return self.driver.find_element(header[0], header[1])
