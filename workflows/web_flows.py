import allure

from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from page_objects.web_pages.after_purchase_page import header
from utilities.common_ops import wait, For, get_popup_text, dismiss_alert


class WebFlows:

    @staticmethod
    @allure.step("Verifying All Buttons In The Upper Navbar Exist")
    def verify_top_navbar_links_exist():
        elems = [ page.web_top_nav_bar.get_home_element(),
                  page.web_top_nav_bar.get_contact_element(),
                  page.web_top_nav_bar.get_about_us_element(),
                  page.web_top_nav_bar.get_cart_element(),
                  page.web_top_nav_bar.get_login_element(),
                  page.web_top_nav_bar.get_sign_up_element()
        ]
        Verifications.soft_assert(elems)

    @staticmethod
    @allure.step("Filling Out Contact Us Form")
    def step_fill_contact_us_form(name, email, message):
        UiActions.update_text(page.web_contact_us_page.get_contact_name_element(), name)
        UiActions.update_text(page.web_contact_us_page.get_contact_email_element(), email)
        UiActions.update_text(page.web_contact_us_page.get_message_element(), message)

    @staticmethod
    @allure.step("Verifying Text In PopUp After Sending A Message In Contact Us")
    def step_verify_text_in_popup_after_contact_us(expected_text):
        actual_text = get_popup_text()
        dismiss_alert()
        Verifications.verify_equals(actual_text, expected_text)

    @staticmethod
    @allure.step("Clicking Send Message")
    def click_send_message():
        UiActions.click(page.web_contact_us_page.get_send_message_button_element())

    @staticmethod
    @allure.step("Clicking Contact Us In The Top Navbar")
    def step_click_contact_us():
        UiActions.click(page.web_top_nav_bar.get_contact_element())

    @staticmethod
    @allure.step("Clicking Add To Cart Button")
    def step_click_add_to_cart():
        UiActions.click(page.web_product_page.get_add_to_cart_element())

    @staticmethod
    @allure.step("Clicking Samsung Galaxy S6 Link")
    def step_navigate_to_galaxy_s6_product_page():
        UiActions.click(page.web_home_page.get_product_page_element())

    @staticmethod
    @allure.step("Clicking Cart In The Top Navbar")
    def step_click_cart_button():
        UiActions.click(page.web_top_nav_bar.get_cart_element())

    @staticmethod
    @allure.step("Clicking Place Order Button")
    def step_click_place_order_button():
        UiActions.click(page.web_cart_page.get_place_order_button_element())

    @staticmethod
    @allure.step("Filling Product Order Form")
    def step_fill_place_order_form(name, country, city, card, month, year):
        UiActions.update_text(page.web_place_order_page.get_name_element(), name)
        UiActions.update_text(page.web_place_order_page.get_country_element(), country)
        UiActions.update_text(page.web_place_order_page.get_city_element(), city)
        UiActions.update_text(page.web_place_order_page.get_credit_card_element(), card)
        UiActions.update_text(page.web_place_order_page.get_credit_card_month_element(), month)
        UiActions.update_text(page.web_place_order_page.get_credit_card_year_element(), year)

    @staticmethod
    @allure.step("Clicking Purchase Inside Order Form")
    def click_purchase():
        UiActions.click(page.web_place_order_page.get_purchase_button_element())

    @staticmethod
    @allure.step("Verifying Purchase Successful based on message")
    def verify_header_text_after_purchase(expected_text_in_header):
        wait(For.ELEMENT_EXISTS, header)
        actual_text_in_header = page.web_after_purchase_page.get_header_element().text
        Verifications.verify_equals(actual_text_in_header, expected_text_in_header)

    @staticmethod
    def check_out_flow(name, country, city, card, month, year):
        WebFlows.step_navigate_to_galaxy_s6_product_page()
        WebFlows.step_click_add_to_cart()
        WebFlows.step_click_cart_button()
        WebFlows.step_click_place_order_button()
        WebFlows.step_fill_place_order_form(name, country, city, card, month, year)
        WebFlows.click_purchase()
