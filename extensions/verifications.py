from selenium.webdriver.remote.webelement import WebElement


class Verifications:

    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, f"Verify equals failed, actual: {actual} and expected is: {expected}"

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "is_displayed Failed - Element is not displayed"
