import allure

from extensions.api_actions import APIActions
from utilities.common_ops import get_data

BASE_URL = get_data("BASE_URL")


class ApiFlows:

    @staticmethod
    @allure.step("Getting List Of Users")
    def get_list_of_users():
        resource = "api/users"
        params = dict(per_page=100)
        response = APIActions.get(BASE_URL + resource, params)
        return APIActions.extract_value_from_response(response, ["data"])

    @staticmethod
    @allure.step("Getting Specific Users Email")
    def get_email_of_user(user_id):
        resource = f"api/users/{user_id}"
        response = APIActions.get(BASE_URL + resource)
        return APIActions.extract_value_from_response(response, ["data", "email"])

    @staticmethod
    @allure.step("Creating User")
    def create_user(name, job):
        resource = "api/users"
        payload = {"name": "name", "job": "job"}
        response = APIActions.post(BASE_URL + resource, payload)
        return response.status_code

    @staticmethod
    @allure.step("Deleting User")
    def delete_user(user_id):
        resource = f"api/users/{user_id}"
        response = APIActions.delete(BASE_URL + resource)
        return response.status_code

    @staticmethod
    @allure.step("Loging In")
    def login(email, password):
        resource = "api/login"
        payload = dict(email=email, password=password)
        response = APIActions.post(BASE_URL + resource, payload)
        return response.status_code
