from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

create_a_task = (By.CSS_SELECTOR, "input[placeholder='Create a task']")
tasks = (By.CLASS_NAME, "view_2Ow90")
delete_button = (By.CLASS_NAME, "destroy_19w1q")
color_list_button = (By.CLASS_NAME, "tagSelector_1mhz5")


class TaskPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_create_task_element(self):
        return self.driver.find_element(create_a_task[0], create_a_task[1])

    def get_tasks_elements(self):
        return self.driver.find_elements(tasks[0], tasks[1])

    def get_delete_button_elements(self):
        return self.driver.find_elements(delete_button[0], delete_button[1])

    def get_color_list_button_element(self):
        return self.driver.find_element(color_list_button[0], color_list_button[1])
