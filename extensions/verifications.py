from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:

    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, f"Verify equals failed, actual: {actual} and expected is: {expected}"

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "is_displayed Failed - Element is not displayed"

    # Verify top navbar buttons using smart-assert
    @staticmethod
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()