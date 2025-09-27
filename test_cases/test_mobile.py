import allure
import pytest

from utilities.common_ops import get_data
from workflows.mobile_flows import MobileFlows

user_name = get_data("MOBILE_USER_NAME")
password = get_data("MOBILE_PASSWORD")


@pytest.mark.usefixtures("init_mobile_driver")
class TestMobile:
    @allure.title("Test 01 - Verify Text Saves Correctly In Echo Screen")
    @allure.description("This test verifies that the text inputted in the echo screen input is reflected back properly")
    def test_01_verify_text_output(self):
        message = "Hello World!"
        MobileFlows.step_tap_on_echo_screen()
        MobileFlows.step_input_message(message)
        MobileFlows.step_save_message_in_echo_screen()
        MobileFlows.verify_input_saved_correctly(message)

    @allure.title("Test 02 - Verify Login Successfully")
    @allure.description("This test verifies that we can log in successfully")
    def test_02_verify_login(self, reset_app):
        MobileFlows.step_tap_on_login_screen()
        MobileFlows.step_input_user_name(user_name)
        MobileFlows.step_input_password(password)
        MobileFlows.step_tap_login_btn()
        MobileFlows.verify_successful_login(user_name)

    @allure.title("Test 03 - Verify Stratus Cloud Was Selected Successfully")
    @allure.description(
        "This test verifies that at the bottom of the list we can access information about stratus cloud")
    def test_03_verify_stratus_cloud(self, reset_app):
        MobileFlows.step_tap_list_demo()
        MobileFlows.step_scroll_to_bottom_of_list()
        MobileFlows.step_tap_stratus()
        MobileFlows.verify_stratus_info()

    @allure.title("Test 04 - Verify The Number Of Categories In Home Page")
    @allure.description("This test verifies the number of categories at the main home page of the app")
    def test_04_verify_number_of_homepage_categories(self, reset_app):
        MobileFlows.verify_list_at_main_home_page(10)
