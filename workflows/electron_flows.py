import time

import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import utilities.manage_pages as page
import test_cases.conftest as conf
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications


class ElectronFlows:

    @staticmethod
    @allure.step("Verifying number of colored tasks in list")
    def verify_num_of_colored_tasks(expected_number, color):
        color = color.lower()
        match color:
            case "red":
                actual_num_of_tasks = len(page.electron_task_page.get_red_background_tasks_elements())
            case "orange":
                actual_num_of_tasks = len(page.electron_task_page.get_orange_background_tasks_elements())
            case "yellow":
                actual_num_of_tasks = len(page.electron_task_page.get_yellow_background_tasks_elements())
            case "green":
                actual_num_of_tasks = len(page.electron_task_page.get_green_background_tasks_elements())
            case "blue":
                actual_num_of_tasks = len(page.electron_task_page.get_blue_background_tasks_elements())
            case "purple":
                actual_num_of_tasks = len(page.electron_task_page.get_purple_background_tasks_elements())
            case "gray":
                actual_num_of_tasks = len(page.electron_task_page.get_gray_background_tasks_elements())
            case _:
                pytest.fail("No such color exists")

        Verifications.verify_equals(actual_num_of_tasks, expected_number)

    @staticmethod
    @allure.step("Verifying that the task list is empty")
    def verify_task_list_empty():
        Verifications.is_displayed(page.electron_task_page.get_empty_list_element())

    @staticmethod
    @allure.step("Verifying the number of tasks currently in the list")
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
        time.sleep(0.5)
        ActionChains(conf.driver).move_to_element(
            page.electron_task_page.get_delete_button_elements()[0]).click().perform()

    @staticmethod
    @allure.step("Deleting all tasks")
    def step_delete_all_tasks():
        num_of_tasks = len(page.electron_task_page.get_tasks_elements())
        for i in range(num_of_tasks):
            time.sleep(0.5)
            ActionChains(conf.driver).move_to_element(
                page.electron_task_page.get_delete_button_elements()[0]).click().perform()

    @staticmethod
    @allure.step("Creating a task")
    def step_create_task(task_name):
        UiActions.update_text(page.electron_task_page.get_create_task_element(), task_name)
        UiActions.update_text(page.electron_task_page.get_create_task_element(), Keys.RETURN)

    @staticmethod
    @allure.step("Creating a task with color")
    def step_create_colored_task(task_name, color):
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
            case _:
                pytest.fail("No such color exists")
        UiActions.click(page.electron_task_page.get_color_list_button_element())
        ElectronFlows.step_create_task(task_name)

    @staticmethod
    @allure.step("Creating multiple tasks")
    def step_create_multiple_tasks(task_names: list[str]):
        for task_name in task_names:
            ElectronFlows.step_create_task(task_name)

    @staticmethod
    @allure.step("Creating multiple tasks in specific day of month")
    def step_create_multiple_tasks_at_day(task_names: list[str], day):
        ElectronFlows.click_calendar_banner()
        ElectronFlows.step_click_on_day_in_calendar(day)
        ElectronFlows.click_calendar_banner()
        for task_name in task_names:
            ElectronFlows.step_create_task(task_name)

    @staticmethod
    @allure.step("Clicking on another day in calendar")
    def step_click_on_day_in_calendar(day):
        UiActions.click(page.electron_task_page.get_day_in_calendar_element(day))

    @staticmethod
    @allure.step("Clicking on filter box")
    def step_click_on_filter_tab():
        UiActions.click(page.electron_task_page.get_filter_button_element())

    @staticmethod
    @allure.step("Clicking on all filter")
    def step_click_on_all_filter():
        time.sleep(0.5)
        UiActions.click(page.electron_task_page.get_date_all_filter_button_element())

    @staticmethod
    def click_calendar_banner():
        UiActions.click(page.electron_task_page.get_date_box_element())
