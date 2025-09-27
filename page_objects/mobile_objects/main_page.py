from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

echo_box = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Echo Box']]")
login_screen = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Login Screen']]")
clipboard_demo = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Clipboard Demo']]")
webview_demo = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Webview Demo']]")
dual_webview_demo = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Dual Webview Demo']]")
list_demo = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='List Demo']]")
photo_demo = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Photo Demo']]")
geolocation_demo = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Geolocation Demo']]")
picker_demo = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Picker Demo']]")
verify_phone_number = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Verify Phone Number']]")
shared_id = (By.ID, "RNE__LISTITEM__padView")


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_echo_box_element(self):
        return self.driver.find_element(echo_box[0], echo_box[1])

    def get_login_screen_element(self):
        return self.driver.find_element(login_screen[0], login_screen[1])

    def get_clipboard_demo_element(self):
        return self.driver.find_element(clipboard_demo[0], clipboard_demo[1])

    def get_webview_demo_element(self):
        return self.driver.find_element(webview_demo[0], webview_demo[1])

    def get_dual_webview_demo_element(self):
        return self.driver.find_element(dual_webview_demo[0], dual_webview_demo[1])

    def get_list_demo_element(self):
        return self.driver.find_element(list_demo[0], list_demo[1])

    def get_photo_demo_element(self):
        return self.driver.find_element(photo_demo[0], photo_demo[1])

    def get_geolocation_demo_element(self):
        return self.driver.find_element(geolocation_demo[0], geolocation_demo[1])

    def get_picker_demo_element(self):
        return self.driver.find_element(picker_demo[0], picker_demo[1])

    def get_verify_phone_number_element(self):
        return self.driver.find_element(verify_phone_number[0], verify_phone_number[1])

    def get_list_of_all_elements(self):
        return self.driver.find_elements(shared_id[0], shared_id[1])
