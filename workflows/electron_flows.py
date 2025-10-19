import allure
from selenium.webdriver import ActionChains
import utilities.manage_pages as page
import test_cases.conftest as conf
from extensions.ui_actions import UiActions


class ElectronFlows:
    @staticmethod
    @allure.step("Deleting a task")
    def step_delete_task():
        ActionChains(conf.driver).move_to_element(
            page.electron_task_page.get_delete_button_elements()).click().perform()

    @staticmethod
    @allure.step("Add a task")
    def step_add_task(task_name):
       UiActions.update_text(page.electron_task_page.get_create_task_element(),task_name)