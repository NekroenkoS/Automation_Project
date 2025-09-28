import allure

from extensions.verifications import Verifications
from utilities.common_ops import get_data
from workflows.api_flows import ApiFlows

expected_email = get_data("API_EMAIL")
name = get_data("API_NAME")
job = get_data("JOB")
email_for_login = get_data("API_LOGIN_EMAIL")
password = get_data("API_LOGIN_PASSWORD")


class TestApi:

    @allure.title("Test 01 - Verify Number Of Users")
    @allure.description("This test verifies the number of users")
    def test_01_verify_total_users(self):
        user_list = ApiFlows.get_list_of_users()
        Verifications.verify_equals(len(user_list), 12)

    @allure.title("Test 02 - Verify Email")
    @allure.description("This test verifies the email of a specific user")
    def test_02_verify_email(self):
        actual_email = ApiFlows.get_email_of_user(2)
        Verifications.verify_equals(actual_email, expected_email)

    @allure.title("Test 03 - Verify User Creation")
    @allure.description("This test verifies that you can create a new user")
    def test_03_verify_user_creation(self):
        actual_status_code = ApiFlows.create_user(name, job)
        Verifications.verify_equals(actual_status_code, 201)

    @allure.title("Test 04 - Verify User Deleted")
    @allure.description("This test verifies that a user is deleted successfully")
    def test_04_verify_user_deleted(self):
        actual_status_code = ApiFlows.delete_user(2)
        Verifications.verify_equals(actual_status_code, 204)

    @allure.title("Test 05 - Verify Login And Session Creation")
    @allure.description("This test verifies that you can create a session by loging in")
    def test_05_verify_login(self):
        actual_status_code = ApiFlows.login(email_for_login, password)
        Verifications.verify_equals(actual_status_code, 200)
