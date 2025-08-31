import allure

from extensions.ui_actions import UiActions
import utilities.manage_pages as page


class WebFlows:

    @staticmethod
    @allure.step("Adding Samsung Galaxy S6 to cart")
    def step_add_samsung_to_cart():
        WebFlows.step_navigate_to_galaxy_s6_product_page()
        WebFlows.step_click_add_to_cart()

    @staticmethod
    @allure.step("Filling Out Contact Us Form")
    def step_fill_contact_us_form(name,email,message):
        WebFlows.input_contact_name(name)
        WebFlows.input_contact_email(email)
        WebFlows.input_message(message)

    @staticmethod
    @allure.step("Clicking Send Message")
    def step_click_send_message():
        UiActions.click(page.web_contact_us_page.get_send_message_button_element())

    @staticmethod
    @allure.step("Entering Message Text")
    def input_message(message):
        UiActions.update_text(page.web_contact_us_page.get_message_element(), message)

    @staticmethod
    @allure.step("Entering Contact Name")
    def input_contact_name(name):
        UiActions.update_text(page.web_contact_us_page.get_contact_name_element(), name)

    @staticmethod
    @allure.step("Entering Contact Email")
    def input_contact_email(email):
        UiActions.update_text(page.web_contact_us_page.get_contact_email_element(), email)

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
        UiActions.click(page.web_home_page.get_samsung_galaxy_s6_product_page_element())

    @staticmethod
    @allure.step("Clicking Cart In The Top Navbar")
    def step_click_cart_button():
        UiActions.click(page.web_top_nav_bar.get_cart_element())

    @staticmethod
    @allure.step("Clicking Place Order Button")
    def step_click_place_order_button():
        UiActions.click(page.web_cart_page.get_place_order_button_element())
