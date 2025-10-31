import time

import allure
import pytest

from workflows.electron_flows import ElectronFlows


@pytest.mark.usefixtures("init_electron_driver")
class TestElectron:

    @allure.title("Test 1 - Verify task created successfully")
    @allure.description("This test verifies that the task is created successfully")
    def test_01_verify_task_created(self):
        task_name = "Complete an hour of study"
        ElectronFlows.step_create_task(task_name)
        ElectronFlows.verify_task_created_with_name(task_name)

    @allure.title("Test 2 - Verify multiple tasks created successfully")
    @allure.description("This test verifies that the amount of tasks we entered were created successfully")
    def test_02_verify_multiple_tasks_created(self):
        task_names = ["Read a book", "Complete an hour of study", "Buy milk"]
        ElectronFlows.step_delete_all_tasks()
        ElectronFlows.step_create_multiple_tasks(task_names)
        ElectronFlows.verify_num_of_tasks(len(task_names))

    @allure.title("Test 3 - Verify multiple colored tasks created successfully")
    @allure.description(
        "This test verifies that the amount of tasks we entered were created successfully with the selected color")
    def test_03_verify_multiple_colored_tasks_created(self):
        colored_task_name = "This is a red task"
        task_names = ["Read a book", "Complete an hour of study", "Buy milk"]
        ElectronFlows.step_delete_all_tasks()
        ElectronFlows.step_create_multiple_tasks(task_names)
        ElectronFlows.step_create_colored_task(colored_task_name, "red")
        ElectronFlows.verify_num_of_colored_tasks(1, "red")

    @allure.title("Test 4 - Verify filter all displays tasks from all dates")
    @allure.description("This test verifies that the 'ALL' filter displays all tasks from all dates")
    def test_04_verify_all_filter(self):
        task_names = ["Read a book", "Complete an hour of study", "Buy milk"]
        ElectronFlows.step_delete_all_tasks()
        ElectronFlows.step_create_multiple_tasks(task_names)
        ElectronFlows.step_create_multiple_tasks_at_day(task_names,27)
        ElectronFlows.step_create_multiple_tasks_at_day(task_names,30)
        ElectronFlows.step_click_on_filter_tab()
        ElectronFlows.step_click_on_all_filter()
        ElectronFlows.verify_num_of_tasks(9)