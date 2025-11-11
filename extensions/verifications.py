from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations

# Centralized verification helpers for readability + consistent failure messages
class Verifications:

    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, f"Verify equals failed, actual: {actual} and expected is: {expected}"

    @staticmethod
    def verify_exists_in(actual, expected):
        assert expected in actual

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "is_displayed Failed - Element is not displayed"

    @staticmethod
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    def verify_true(statement: bool):
        assert statement, f"The Test Failed. {statement} is false"

    @staticmethod
    def verify_false(statement: bool):
        assert not statement, f"The Test Failed. {statement} is true"
