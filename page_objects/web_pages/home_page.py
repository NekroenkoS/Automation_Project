import allure
from selenium.webdriver.common.by import By

galaxy_s6 = (By.LINK_TEXT, "Samsung galaxy s6")


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_samsung_galaxy_s6_element(self):
        return self.driver.find_element(galaxy_s6[0], galaxy_s6[1])
