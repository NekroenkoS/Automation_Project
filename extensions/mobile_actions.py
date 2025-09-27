from extensions.ui_actions import UiActions
import test_cases.conftest as conf


class MobileActions(UiActions):

    @staticmethod
    def tap(elem, times):
        conf.action.tap(elem, times).perform()

    @staticmethod
    def swipe(start_x, start_y, end_x, end_y, duration):
        conf.driver.swipe(start_x, start_y, end_x, end_y, duration)
