import xml.etree.ElementTree as ET
from pathlib import Path

import appium.webdriver
import pytest
import selenium
from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import get_data
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages

driver = None
action = None
mobile_size = None
web_driver = get_data("BROWSER")


@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_web_driver()
    global driver
    driver = EventFiringWebDriver(edriver, EventListener())
    driver.maximize_window()
    driver.implicitly_wait(int(get_data("WAIT_TIME")))
    driver.get(get_data("WEB_URL"))
    request.cls.driver = driver
    ManagePages.init_web_pages()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_mobile_driver(request):
    edriver = get_mobile_driver()
    global driver, action, mobile_size
    driver = EventFiringWebDriver(edriver, EventListener())
    driver.implicitly_wait(int(get_data("WAIT_TIME")))
    request.cls.driver = driver
    ManagePages.init_mobile_pages()
    action = TouchAction(driver)
    request.cls.action = action
    mobile_size = driver.get_window_size()
    request.cls.mobile_size = mobile_size

    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_electron_driver(request):
    edriver = get_electron_driver()
    global driver, action
    driver = EventFiringWebDriver(edriver, EventListener())
    driver.implicitly_wait(int(get_data("WAIT_TIME")))
    request.cls.driver = driver
    action = ActionChains(driver)
    request.cls.action = action
    ManagePages.init_electron_pages()
    yield
    driver.quit()

@pytest.fixture(scope='class')
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    global driver, action
    driver = EventFiringWebDriver(edriver, EventListener())
    driver.implicitly_wait(int(get_data("WAIT_TIME")))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()


def get_web_driver():
    if web_driver.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif web_driver.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif web_driver.lower() == "edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    else:
        driver = None
        raise Exception('Wrong input - unrecognized browser')
    return driver


def get_mobile_driver():
    if get_data("MOBILE_DEVICE").lower() == "android":
        driver = get_android(get_data("UDID"))
    elif get_data("MOBILE_DEVICE").lower() == "ios":
        driver = get_ios(get_data("UDID"))
    else:
        driver = None
        raise Exception("Wrong Input, Driver Is None")
    return driver

def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data("ELECTRON_APP")
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data("ELECTRON_DRIVER"))
    return driver

def get_desktop_driver():
    dc = {}
    dc['app'] = get_data("APPLICATION_NAME")
    dc['platformName'] = "Windows"
    dc['deviceName'] = "WindowsPC"
    driver = appium.webdriver.Remote(get_data("WINAPP_DRIVER_SERVICE"),dc)
    return driver

def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data("APP_PACKAGE")
    dc['appActivity'] = get_data("APP_ACTIVITY")
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data("APPIUM_SERVER"), dc)
    return android_driver


def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data("BUNDLE_ID")
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data("APPIUM_SERVER"), dc)
    return ios_driver

# Returns back to home web site
@pytest.fixture(scope="function")
def go_home(init_web_driver):
    driver.get(get_data("WEB_URL"))

# Resets mobile APP
@pytest.fixture(scope="function")
def reset_app(init_mobile_driver):
    driver.reset()
