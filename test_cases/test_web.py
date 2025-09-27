import allure
import pytest

import page_objects.web_objects.home_page

from test_cases.conftest import get_data
from workflows.web_flows import WebFlows

name = get_data("NAME")
country = get_data("COUNTRY")
city = get_data("CITY")
credit_card = get_data("CREDIT_CARD")
month_in_credit_card = get_data("MONTH_IN_CREDIT_CARD")
year_in_credit_card = get_data("YEAR_IN_CREDIT_CARD")
email = get_data("EMAIL")
user_name = get_data("WEB_USER_NAME")
password = get_data("WEB_PASSWORD")


@pytest.mark.usefixtures("init_web_driver")
class TestWeb:

    @allure.title("Test 1 - Verify Contact Us Form Sent Successfully")
    @allure.description("This test verifies that the contact us form is sent and there is a success message")
    def test_01_verify_contact_us(self):
        WebFlows.step_click_contact_us()
        WebFlows.step_fill_contact_us_form(name, email, "Hello World!")
        WebFlows.click_send_message()
        WebFlows.verify_text_in_popup_after_contact_us("Thanks for the message!!")

    @allure.title("Test 2 - Verify Checkout Flow")
    @allure.description("This test verifies that you can checkout successfully with a product")
    def test_02_verify_checkout_flow(self, go_home):
        WebFlows.check_out_flow(name, country, city, credit_card, month_in_credit_card, year_in_credit_card)
        WebFlows.verify_header_text_after_purchase("Thank you for your purchase!")

    @allure.title("Test 3 - Verify All The Top Navbar Buttons Are Displayed")
    @allure.description("This test verifies that all the buttons in the top navbar exist")
    def test_03_verify_top_navbar_buttons_exist(self, go_home):
        WebFlows.verify_top_navbar_links_exist()

    @pytest.mark.parametrize(
        "locator, expected_name", [
            (page_objects.web_objects.home_page.galaxy_s6_product_page, "Samsung galaxy s6"),
            (page_objects.web_objects.home_page.nokia_lumia_1520_product_page, "Nokia lumia 1520"),
            (page_objects.web_objects.home_page.nexus_6_product_page, "Nexus 6"),
            (page_objects.web_objects.home_page.galaxy_s7_product_page, "Samsung galaxy s7"),
            (page_objects.web_objects.home_page.iphone_6_32gb_product_page, "Iphone 6 32gb"),
            (page_objects.web_objects.home_page.htc_one_m9_product_page, "HTC One M9"),
            (page_objects.web_objects.home_page.sony_vaio_i5_product_page, "Sony vaio i5"),
            (page_objects.web_objects.home_page.sony_vaio_i7_product_page, "Sony vaio i7")
        ]
    )
    @allure.title("Test 4 - Verify All The Product Links Are Valid In Home Page")
    @allure.description(
        "This test verifies that all the product links in the homepage are leading to the correct pages")
    def test_04_verify_product_links_valid(self, go_home, locator, expected_name):
        WebFlows.step_navigate_to_item_product_page(locator)
        WebFlows.verify_name_of_product(expected_name)

    @allure.title("Test 5 - Verify Sum Of Products In Cart")
    @allure.description("This test verifies that the sum of products in cart is correct")
    def test_05_verify_login_successful(self):
        WebFlows.step_click_login_button()
        WebFlows.step_fill_login_information(user_name, password)
        WebFlows.step_click_login_button_inside_login_form()
        WebFlows.verify_login_successful(user_name)
