from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

home = (By.LINK_TEXT, "Home ")
contact = (By.LINK_TEXT, "Contact")
about_us = (By.LINK_TEXT, "About us")
cart = (By.LINK_TEXT, "Cart")
log_in = (By.LINK_TEXT, "Log in")
sign_up = (By.LINK_TEXT, "Sign up")

class TopNavBar:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_home_element(self):
        return self.driver.find_element(home[0], home[1])

    def get_contact_element(self):
        return self.driver.find_element(contact[0], contact[1])

    def get_about_us_element(self):
        return self.driver.find_element(about_us[0], about_us[1])

    def get_cart_element(self):
        return self.driver.find_element(cart[0], cart[1])

    def get_login_element(self):
        return self.driver.find_element(log_in[0], log_in[1])

    def get_sign_up_element(self):
        return self.driver.find_element(sign_up[0], sign_up[1])