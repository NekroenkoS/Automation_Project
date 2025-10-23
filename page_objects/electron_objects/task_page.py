from appium.webdriver.webdriver import WebDriver
from pygments.styles.dracula import yellow
from selenium.webdriver.common.by import By

create_a_task = (By.CSS_SELECTOR, "input[placeholder='Create a task']")
tasks = (By.CLASS_NAME, "view_2Ow90")
delete_button = (By.CLASS_NAME, "destroy_19w1q")
color_list_button = (By.CLASS_NAME, "topWrapper_2caNE")
task_names = (By.CLASS_NAME, "label_5i8SP")
empty_list = (By.CLASS_NAME, "emptyState_3FwtK")
red_color = (By.CSS_SELECTOR,
             "div[class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']>span[style='background: rgb(255, 103, 93);']")
orange_color = (By.CSS_SELECTOR,
                "div[class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']>span[style='background: rgb(249, 167, 77);']")
yellow_color = (By.CSS_SELECTOR,
                "div[class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']>span[style='background: rgb(245, 206, 83);']")
green_color = (By.CSS_SELECTOR,
               "div[class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']>span[style='background: rgb(114, 204, 87);']")
blue_color = (By.CSS_SELECTOR,
              "div[class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']>span[style='background: rgb(87, 185, 244);']")
purple_color = (By.CSS_SELECTOR,
                "div[class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']>span[style='background: rgb(210, 137, 226);']")
gray_color = (By.CSS_SELECTOR,
              "div[class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']>span[style='background: rgb(165, 165, 167);']")


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

    def get_task_names_elements(self):
        return self.driver.find_elements(task_names[0], task_names[1])

    def get_empty_list_element(self):
        return self.driver.find_element(empty_list[0], empty_list[1])

    def get_red_color_element(self):
        return self.driver.find_element(red_color[0], red_color[1])

    def get_orange_color_element(self):
        return self.driver.find_element(orange_color[0], orange_color[1])

    def get_yellow_color_element(self):
        return self.driver.find_element(yellow_color[0], yellow_color[1])

    def get_green_color_element(self):
        return self.driver.find_element(green_color[0], green_color[1])

    def get_blue_color_element(self):
        return self.driver.find_element(blue_color[0], blue_color[1])

    def get_purple_color_element(self):
        return self.driver.find_element(purple_color[0], purple_color[1])

    def get_gray_color_element(self):
        return self.driver.find_element(gray_color[0], gray_color[1])
