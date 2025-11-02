import allure
import pytest

from workflows.desktop_flows import DesktopFlows


@pytest.mark.usefixtures("init_desktop_driver")
class TestDesktop:

    @allure.title("Test 1 - Verify adding numbers")
    @allure.description("This test verifies the add feature works correctly")
    def test_01_verify_adding(self, clear_calc):
        first_num = 2
        sec_num = 5
        DesktopFlows.step_calculate_flow(f"{first_num}+{sec_num}")
        expected_answer = first_num + sec_num
        DesktopFlows.step_click_equals()
        DesktopFlows.verify_calculator_answer(str(expected_answer))

    @allure.title("Test 2 - Verifying chained ops with immediate execution")
    @allure.description(
        "This test verifies that the standard mode uses immediate execution: (12 + 34) = 46, then * 56 = 2576.")
    def test_02_chained_immediate_execution(self):
        DesktopFlows.step_calculate_flow("12+34")
        DesktopFlows.step_click_equals()
        DesktopFlows.step_calculate_flow("*56")
        DesktopFlows.step_click_equals()
        DesktopFlows.verify_calculator_answer("2,576")

    @allure.title("Test 3 - Editing with Backspace in a longer entry")
    @allure.description("Validates input editing and result correctness.")
    def test_03_verify_backspace_edit_then_compute(self, clear_calc):
        DesktopFlows.step_calculate_flow("123")
        DesktopFlows.step_click_backspace()
        DesktopFlows.step_calculate_flow("*3")
        DesktopFlows.step_click_equals()
        DesktopFlows.verify_calculator_answer("36")

    @allure.title("Test 4 - Repeated equals repeats last operation")
    @allure.description("This test verifies that pressing the equals button calculates the last operand and num")
    def test_04_verify_repeated_equals_behavior(self, clear_calc):
        DesktopFlows.step_calculate_flow("5+10")
        for i in range(3):
            DesktopFlows.step_click_equals()
        DesktopFlows.verify_calculator_answer("35")

    @allure.title("Test 5 - Verifying negate functionality")
    @allure.description(
        "This test verifies that negating a number correctly toggles its sign "
        "and works properly in combination with arithmetic operations."
    )
    def test_05_verify_negate_behavior(self, clear_calc):
        DesktopFlows.step_calculate_flow('8')
        DesktopFlows.step_click_negate()
        DesktopFlows.step_calculate_flow('+3=')
        DesktopFlows.step_click_negate()
        DesktopFlows.verify_calculator_answer("5")
