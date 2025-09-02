import allure
import pytest

from test_cases.conftest import get_data
from workflows.web_flows import WebFlows

name = get_data("NAME")
country = get_data("COUNTRY")
city = get_data("CITY")
credit_card = get_data("CREDIT_CARD")
month_in_credit_card = get_data("MONTH_IN_CREDIT_CARD")
year_in_credit_card = get_data("YEAR_IN_CREDIT_CARD")
email = get_data("EMAIL")


@pytest.mark.usefixtures("init_driver")
class TestWeb:

    @allure.title("Verify Contact Us Form Sent Successfully")
    @allure.description("This test verifies that the contact us form is sent and there is a success message")
    def test_01_verify_contact_us(self):
        WebFlows.step_click_contact_us()
        WebFlows.step_fill_contact_us_form(name, email, "Hello World!")
        WebFlows.click_send_message()
        WebFlows.step_verify_text_in_popup_after_contact_us("Thanks for the message!!")

    @allure.title("Test 2 - Verify Checkout Flow")
    @allure.description("This test verifies that you can checkout successfully with a product")
    def test_02_verify_checkout_flow(self, go_home):
        WebFlows.check_out_flow(name, country, city, credit_card, month_in_credit_card, year_in_credit_card)
        WebFlows.verify_header_text_after_purchase("Thank you for your purchase!")
