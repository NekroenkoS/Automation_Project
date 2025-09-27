from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

title = (By.XPATH, "//*[@text='Secret Area']")
login_message = (By.XPATH, "//*[@text='You are logged in as alice']")
logout_btn = (By.XPATH, "//*[@contentDescription='Logout']")


class AfterLoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_title_element(self):
        return self.driver.find_element(title[0], title[1])

    def get_login_message_element(self):
        return self.driver.find_element(login_message[0], login_message[1])

    def get_logout_btn_element(self):
        return self.driver.find_element(logout_btn[0], logout_btn[1])
