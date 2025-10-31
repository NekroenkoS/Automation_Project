import allure
import pytest

from workflows.desktop_flows import DesktopFlows


@pytest.mark.usefixtures("init_desktop_driver")
class TestDesktop:

    @allure.title("Test 1 - Verify adding numbers")
    @allure.description("This test verifies the add feature works correctly")
    def test_01_verify_adding(self):
        first_num = 2
        sec_num = 5
        DesktopFlows.step_click_on_number(first_num)
        DesktopFlows.step_click_add()
        DesktopFlows.step_click_on_number(sec_num)
        DesktopFlows.step_click_equals()
        expected_answer = first_num + sec_num
        DesktopFlows.verify_calculator_answer(str(expected_answer))