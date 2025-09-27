from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

user_name = (By.ID, "username")
password = (By.ID, "password")
login_btn = (By.XPATH, "//*[@text='Login' and ./parent::*[@id='loginBtn']]")


class MobileLoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_user_name_element(self):
        return self.driver.find_element(user_name[0], user_name[1])

    def get_password_element(self):
        return self.driver.find_element(password[0], password[1])

    def get_login_btn_element(self):
        return self.driver.find_element(login_btn[0], login_btn[1])
