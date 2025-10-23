import allure
import pytest

from workflows.electron_flows import ElectronFlows


@pytest.mark.usefixtures("init_electron_driver")
class TestWeb:

    @allure.title("Test 1 - Verify task created successfully")
    @allure.description("This test verifies that the task is created successfully")
    def test_01_verify_task_created(self):
        task_name = "Complete an hour of study"
        ElectronFlows.step_create_task(task_name)
        ElectronFlows.verify_task_created_with_name(task_name)

    @allure.title("Test 2 - Create multiple tasks and verify they were created")
    @allure.description("This test verifies that the amount of tasks we entered were created successfully")
    def test_02_verify_multiple_tasks_created(self):
        ElectronFlows.step_delete_upper_task()
        task_names = ["Read a book","Complete an hour of study","Buy milk"]
        ElectronFlows.step_create_multiple_tasks(task_names)
        ElectronFlows.verify_num_of_tasks(len(task_names))
