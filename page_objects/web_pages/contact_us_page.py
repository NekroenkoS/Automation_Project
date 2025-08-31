from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

contact_email = (By.ID, "recipient-email")
contact_name = (By.ID, "recipient-name")
message = (By.ID, "message-text")
send_message_button = (By.CSS_SELECTOR, "button[onclick='send()']")

class ContactUsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_contact_email_element(self):
        return self.driver.find_element(contact_email[0], contact_email[1])

    def get_contact_name_element(self):
        return self.driver.find_element(contact_name[0], contact_name[1])

    def get_message_element(self):
        return self.driver.find_element(message[0], message[1])

    def get_send_message_button_element(self):
        return self.driver.find_element(send_message_button[0], send_message_button[1])
