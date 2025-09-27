from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

user_name_locator = (By.ID, "loginusername")
password_locator = (By.ID, "loginpassword")
log_in_button_locator = (By.CSS_SELECTOR, "button[onclick='logIn()']")


class WebLoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_user_name_element(self):
        return self.driver.find_element(user_name_locator[0], user_name_locator[1])

    def get_password_element(self):
        return self.driver.find_element(password_locator[0], password_locator[1])

    def get_log_in_button_element(self):
        return self.driver.find_element(log_in_button_locator[0], log_in_button_locator[1])
