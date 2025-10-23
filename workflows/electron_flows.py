import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import utilities.manage_pages as page
import test_cases.conftest as conf
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from page_objects.electron_objects.task_page import delete_button
from utilities.common_ops import wait, For


class ElectronFlows:

    @staticmethod
    @allure.step("Verifying that the task list is empty")
    def verify_task_list_empty():
        Verifications.is_displayed(page.electron_task_page.get_empty_list_element())

    @staticmethod
    @allure.step("Verifying the number of tasks currently in the list1")
    def verify_num_of_tasks(expected_number):
        actual_num_of_tasks = len(page.electron_task_page.get_tasks_elements())
        Verifications.verify_equals(actual_num_of_tasks, expected_number)

    @staticmethod
    @allure.step("Verifying a task created successfully")
    def verify_task_created_with_name(expected_task_name):
        actual_task_name = page.electron_task_page.get_task_names_elements()[0].text
        Verifications.verify_equals(actual_task_name, expected_task_name)

    @staticmethod
    @allure.step("Deleting a task")
    def step_delete_upper_task():
        ActionChains(conf.driver).move_to_element(
            page.electron_task_page.get_delete_button_elements()[0]).click().perform()  

    @staticmethod
    @allure.step("Deleting all tasks")
    def step_delete_all_tasks():
        num_of_tasks = len(page.electron_task_page.get_tasks_elements())
        for i in range(num_of_tasks):
            wait(For.ELEMENT_EXISTS, delete_button)
            ActionChains(conf.driver).move_to_element(
                page.electron_task_page.get_delete_button_elements()[i]).click().perform()

    @staticmethod
    @allure.step("Creating a task")
    def step_create_task(task_name):
        UiActions.update_text(page.electron_task_page.get_create_task_element(), task_name)
        UiActions.update_text(page.electron_task_page.get_create_task_element(), Keys.RETURN)

    @staticmethod
    @allure.step("Creating a task with color")
    def step_create_colored_task(task_name, color=None):
        if color is not None:
            color = color.lower()
            UiActions.click(page.electron_task_page.get_color_list_button_element())
            match color:
                case "red":
                    UiActions.click(page.electron_task_page.get_red_color_element())
                case "orange":
                    UiActions.click(page.electron_task_page.get_orange_color_element())
                case "yellow":
                    UiActions.click(page.electron_task_page.get_yellow_color_element())
                case "green":
                    UiActions.click(page.electron_task_page.get_green_color_element())
                case "blue":
                    UiActions.click(page.electron_task_page.get_blue_color_element())
                case "purple":
                    UiActions.click(page.electron_task_page.get_purple_color_element())
                case "gray":
                    UiActions.click(page.electron_task_page.get_purple_color_element())
            UiActions.click(page.electron_task_page.get_color_list_button_element())
        UiActions.update_text(page.electron_task_page.get_create_task_element(), task_name)
        UiActions.update_text(page.electron_task_page.get_create_task_element(), Keys.RETURN)

    @staticmethod
    @allure.step("Creating multiple tasks")
    def step_create_multiple_tasks(task_names: list[str]):
        for task_name in task_names:
            UiActions.update_text(page.electron_task_page.get_create_task_element(), task_name)
            UiActions.update_text(page.electron_task_page.get_create_task_element(), Keys.RETURN)
