from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

header_message = (By.XPATH, "//*[@text=concat('Here', \"'\", 's what you said before:')]")
saved_message = (By.ID, "savedMessage")
input_message = (By.ID, "messageInput")
save_btn = (By.ID, "messageSaveBtn")


class EchoScreenPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_header_message_element(self):
        return self.driver.find_element(header_message[0], header_message[1])

    def get_saved_message_element(self):
        return self.driver.find_element(saved_message[0], saved_message[1])

    def get_input_message_element(self):
        return self.driver.find_element(input_message[0], input_message[1])

    def get_save_btn_element(self):
        return self.driver.find_element(save_btn[0], save_btn[1])
