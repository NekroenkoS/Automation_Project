import allure

import utilities.manage_pages as page
from extensions.mobile_actions import MobileActions
from extensions.verifications import Verifications
import test_cases.conftest as conf


class MobileFlows:

    @staticmethod
    @allure.step("Verifying The Number Of Categories")
    def verify_list_at_main_home_page(expected_number_of_elements):
        actual_number_of_elements = page.mobile_main_page.get_list_of_all_elements()
        assert len(actual_number_of_elements) == expected_number_of_elements

    @staticmethod
    @allure.step("Verifying That Stratus Was Successfully Tapped")
    def verify_stratus_info():
        expected_text_in_message = "Stratus"
        actual_message = page.mobile_list_demo_page.get_message_element().text
        Verifications.verify_exists_in(actual_message, expected_text_in_message)

    @staticmethod
    @allure.step("Verifying Successfully logged in")
    def verify_successful_login(expected_text_after_login):
        actual_text_after_login = page.mobile_after_login_page.get_login_message_element().text
        Verifications.verify_exists_in(actual_text_after_login, expected_text_after_login)

    @staticmethod
    @allure.step("Verifying Message Was Saved Correctly")
    def verify_input_saved_correctly(expected_saved_text):
        actual_saved_text = page.mobile_echo_screen_page.get_saved_message_element().text
        Verifications.verify_equals(actual_saved_text, expected_saved_text)

    @staticmethod
    @allure.step("Tapping On Echo Screen From Main Page")
    def step_tap_on_echo_screen():
        MobileActions.tap(page.mobile_main_page.get_echo_box_element(), 1)

    @staticmethod
    @allure.step("Inputting Message")
    def step_input_message(message):
        MobileActions.update_text(page.mobile_echo_screen_page.get_input_message_element(), message)

    @staticmethod
    @allure.step("Tapping On Save In Echo Screen")
    def step_save_message_in_echo_screen():
        MobileActions.tap(page.mobile_echo_screen_page.get_save_btn_element(), 1)

    @staticmethod
    @allure.step("Tapping On Login Screen From Main Page")
    def step_tap_on_login_screen():
        MobileActions.tap(page.mobile_main_page.get_login_screen_element(), 1)

    @staticmethod
    @allure.step("Inputting User Name")
    def step_input_user_name(user_name):
        MobileActions.update_text(page.mobile_login_page.get_user_name_element(), user_name)

    @staticmethod
    @allure.step("Inputting Password")
    def step_input_password(password):
        MobileActions.update_text(page.mobile_login_page.get_password_element(), password)

    @staticmethod
    @allure.step("Tapping Login Button")
    def step_tap_login_btn():
        MobileActions.tap(page.mobile_login_page.get_login_btn_element(), 1)

    @staticmethod
    @allure.step("Tapping On List Demo From Main Page")
    def step_tap_list_demo():
        MobileActions.tap(page.mobile_main_page.get_list_demo_element(), 1)

    @staticmethod
    @allure.step("Scrolling Down To Bottom Of List")
    def step_scroll_to_bottom_of_list():
        width = conf.mobile_size["width"]
        height = conf.mobile_size["height"]
        MobileActions.swipe(width * 0.5, height * 0.95, width * 0.5, height * 0.05, 3000)
        MobileActions.swipe(width * 0.5, height * 0.95, width * 0.5, height * 0.05, 3000)

    @staticmethod
    @allure.step("Tapping On Stratus")
    def step_tap_stratus():
        MobileActions.tap(page.mobile_list_demo_page.get_stratus_element(), 1)
