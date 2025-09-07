from selenium.webdriver.remote.webelement import WebElement


class Verifications:

    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, f"Verify equals failed, actual: {actual} and expected is: {expected}"

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "is_displayed Failed - Element is not displayed"

    @staticmethod
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].text)
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print(f"Soft display failed - Elements that failed {failed_elem}")
                raise AssertionError("Soft display failed")