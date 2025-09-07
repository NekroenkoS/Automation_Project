from pathlib import Path

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET

def get_data(node_name):
    root = ET.parse(
        Path(__file__).parent.parent / 'configuration' / 'data.xml')
    return root.find(".//" + node_name).text


def get_popup_text():
    return conf.driver.switch_to.alert.text


def dismiss_alert():
    conf.driver.switch_to.alert.dismiss()

def wait(for_element, elem):
    if for_element == "element_exists":
        WebDriverWait(conf.driver, 10).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == "element_displayed":
        WebDriverWait(conf.driver, 10).until(EC.visibility_of_element_located((elem[0], elem[1])))
    elif for_element == "element_clickable":
        WebDriverWait(conf.driver, 10).until(EC.element_to_be_clickable((elem[0], elem[1])))


# enum for the for_element in wait method
class For:
    ELEMENT_EXISTS = "element_exists"
    ELEMENT_DISPLAYED = "element_displayed"
    ELEMENT_CLICKABLE = "element_clickable"
