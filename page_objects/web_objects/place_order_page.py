from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

name = (By.ID, "name")
country = (By.ID, "country")
city = (By.ID, "city")
card = (By.ID, "card")
month = (By.ID, "month")
year = (By.ID, "year")
purchase_button = (By.CSS_SELECTOR, "[onclick='purchaseOrder()']")


class PlaceOrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_name_element(self):
        return self.driver.find_element(name[0], name[1])

    def get_country_element(self):
        return self.driver.find_element(country[0], country[1])

    def get_city_element(self):
        return self.driver.find_element(city[0], city[1])

    def get_credit_card_element(self):
        return self.driver.find_element(card[0], card[1])

    def get_credit_card_month_element(self):
        return self.driver.find_element(month[0], month[1])

    def get_credit_card_year_element(self):
        return self.driver.find_element(year[0], year[1])

    def get_purchase_button_element(self):
        return self.driver.find_element(purchase_button[0], purchase_button[1])
