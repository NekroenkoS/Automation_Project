from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

place_order_button = (By.CSS_SELECTOR, "button[data-target='#orderModal']")


class CartPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_place_order_button_element(self):
        return self.driver.find_element(place_order_button[0], place_order_button[1])
