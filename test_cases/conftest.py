import xml.etree.ElementTree as ET

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.manage_pages import ManagePages

driver = None
web_driver = "Chrome"

@pytest.fixture(scope='class')
def init_driver(request):
    global driver
    driver = get_web_driver()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(get_data("URL"))
    request.cls.driver = driver
    ManagePages.init_web_pages()
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

def get_data(node_name):
    root = ET.parse(
        r"C:\Users\USER\PycharmProjects\Automation Project\configuration\configuration_for_blaze_testing.xml").getroot()
    return root.find(".//" + node_name).text
