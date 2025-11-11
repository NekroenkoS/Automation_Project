from pathlib import Path

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


# Returns the text value of the given XML node from data.xml
def get_data(node_name):
    root = ET.parse(
        Path(__file__).parent.parent / 'configuration' / 'data.xml')
    return root.find(".//" + node_name).text


# Returns the text from the currently displayed alert popup
def get_popup_text():
    return conf.driver.switch_to.alert.text


# Dismisses the currently displayed browser alert popup
def dismiss_alert():
    conf.driver.switch_to.alert.dismiss()


# Waits for a specific element condition (exists, displayed, clickable, or contains text)
def wait(for_element, elem, text=None):
    if for_element == "element_exists":
        WebDriverWait(conf.driver, 10).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == "element_displayed":
        WebDriverWait(conf.driver, 10).until(EC.visibility_of_element_located((elem[0], elem[1])))
    elif for_element == "element_clickable":
        WebDriverWait(conf.driver, 10).until(EC.element_to_be_clickable((elem[0], elem[1])))
    elif for_element == "text_to_be_present":
        WebDriverWait(conf.driver, 10).until(EC.text_to_be_present_in_element((elem[0], elem[1]), text))


# Used to specify which condition the wait() function should apply
class For:
    ELEMENT_EXISTS = "element_exists"
    ELEMENT_DISPLAYED = "element_displayed"
    ELEMENT_CLICKABLE = "element_clickable"
    TEXT_TO_BE_PRESENT = "text_to_be_present"