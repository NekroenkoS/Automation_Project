
import allure
import pytest
from selenium.webdriver.common.by import By

from test_cases.conftest import get_data
from workflows.web_flows import WebFlows

name = get_data("NAME")
country = get_data("COUNTRY")
city = get_data("CITY")
credit_card = get_data("CREDIT_CARD")
month_in_credit_card = get_data("MONTH_IN_CREDIT_CARD")
year_in_credit_card = get_data("YEAR_IN_CREDIT_CARD")

@pytest.mark.usefixtures("init_driver")
class TestWeb:

    @allure.title("Verify Galaxy S6 Price In Cart")
    @allure.description("")
    def test_01_verify_samsung_galaxy_s6_price_in_cart(self):
        WebFlows.step_add_samsung_to_cart()
        WebFlows.click_cart()
        # Verification
        actual_cart_samsung_price = self.driver.find_elements(By.TAG_NAME, "td")[2].text
        expected_samsung_price = "360"
        assert expected_samsung_price == actual_cart_samsung_price

    @allure.title("Test 2 - Verify Checkout Flow")
    @allure.description("Verify checkout flow from beginning until the end")
    def test_02_verify_checkout_flow(self):
        WebFlows.step_add_samsung_to_cart()
        WebFlows.click_cart()
        self.step_click_on_order()
        self.step_fill_out_form(name, country, city, credit_card, month_in_credit_card, year_in_credit_card)
        self.click_on_purchase()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                   "div[class*='sweet-alert']>h2").text == "Thank you for your purchase!"

    @allure.step("Click On Order Inside Cart")
    def step_click_on_order(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-target='#orderModal']").click()

    @allure.step("Fill Out Order Form")
    def step_fill_out_form(self, my_name, my_country, my_city, my_credit_card, my_month_in_credit_card,
                           my_year_in_credit_card):
        self.driver.find_element(By.ID, "name").send_keys(my_name)
        self.driver.find_element(By.ID, "country").send_keys(my_country)
        self.driver.find_element(By.ID, "city").send_keys(my_city)
        self.driver.find_element(By.ID, "card").send_keys(my_credit_card)
        self.driver.find_element(By.ID, "month").send_keys(my_month_in_credit_card)
        self.driver.find_element(By.ID, "year").send_keys(my_year_in_credit_card)

    @allure.step("Click On Purchase Button Inside Order Form")
    def click_on_purchase(self):
        self.driver.find_element(By.CSS_SELECTOR, "[onclick='purchaseOrder()']").click()
