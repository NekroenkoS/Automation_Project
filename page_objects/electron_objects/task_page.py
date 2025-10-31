from appium.webdriver.webdriver import WebDriver
from pygments.styles.dracula import yellow
from selenium.webdriver.common.by import By

create_a_task = (By.CSS_SELECTOR, "input[placeholder='Create a task']")
tasks = (By.XPATH, "//div[@class='taskList_1-1Yq'][2]//div[@class='draggableList_DX-a1']/div")
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
red_background_tasks = (By.CSS_SELECTOR, "[class='tag_3u4he'][style='background: rgb(255, 103, 93);']")
orange_background_tasks = (By.CSS_SELECTOR, "[class='tag_3u4he'][style='background: rgb(249, 167, 77);']")
yellow_background_tasks = (By.CSS_SELECTOR, "[class='tag_3u4he'][style='background: rgb(245, 206, 83);']")
green_background_tasks = (By.CSS_SELECTOR, "[class='tag_3u4he'][style='background: rgb(114, 204, 87);']")
blue_background_tasks = (By.CSS_SELECTOR, "[class='tag_3u4he'][style='background: rgb(87, 185, 244);']")
purple_background_tasks = (By.CSS_SELECTOR, "[class='tag_3u4he'][style='background: rgb(210, 137, 226);']")
gray_background_tasks = (By.CSS_SELECTOR, "[class='tag_3u4he'][style='background: rgb(165, 165, 167);']")
date_box = (By.CLASS_NAME, "dateFormatted_3GjaR")
filter_button = (By.CLASS_NAME, "toggleVisibilityPanel_hNPyc")
date_all_filter_button = (By.XPATH, "//div[@class='filterWrapper_1TK4M']/button[@class='filterButton_1-ZkH'][1]")


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

    def get_red_background_tasks_elements(self):
        return self.driver.find_elements(red_background_tasks[0], red_background_tasks[1])

    def get_orange_background_tasks_elements(self):
        return self.driver.find_elements(orange_background_tasks[0], orange_background_tasks[1])

    def get_yellow_background_tasks_elements(self):
        return self.driver.find_elements(yellow_background_tasks[0], yellow_background_tasks[1])

    def get_green_background_tasks_elements(self):
        return self.driver.find_elements(green_background_tasks[0], green_background_tasks[1])

    def get_blue_background_tasks_elements(self):
        return self.driver.find_elements(blue_background_tasks[0], blue_background_tasks[1])

    def get_purple_background_tasks_elements(self):
        return self.driver.find_elements(purple_background_tasks[0], purple_background_tasks[1])

    def get_gray_background_tasks_elements(self):
        return self.driver.find_elements(gray_background_tasks[0], gray_background_tasks[1])

    def get_date_box_element(self):
        return self.driver.find_element(date_box[0], date_box[1])

    def get_day_in_calendar_element(self, day):
        xpath = (
            f"//div[@class='daysWrapper_3SMBJ'][2]//div[@class='day_25Aqk']/span[@class='text_1GSPD' and text()='{day}']"
        )
        return self.driver.find_element(By.XPATH, xpath)

    def get_filter_button_element(self):
        return self.driver.find_element(filter_button[0], filter_button[1])
    def get_date_all_filter_button_element(self):
        return self.driver.find_element(date_all_filter_button[0], date_all_filter_button[1])
