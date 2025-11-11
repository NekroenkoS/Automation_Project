import time

import allure
import utilities.manage_pages as page

from extensions.ui_actions import UiActions
from extensions.verifications import Verifications


class DesktopFlows:

    @staticmethod
    @allure.step("Calculating Equation")
    def step_calculate_flow(equation):
        for i in equation:
            DesktopFlows.click_on_calculator(i)

    @staticmethod
    @allure.step("Verifying calculator answer")
    def verify_calculator_answer(expected_num):
        time.sleep(1)
        result_str = page.calculator_standard_page.get_answer_element().text
        actual_num = result_str.replace("Display is ", "").strip()
        Verifications.verify_equals(actual_num, expected_num)

    @staticmethod
    # Click a single calculator key by char (digits/operators)
    def click_on_calculator(char):
        mapping = {
            '0': lambda: UiActions.click(page.calculator_standard_page.get_zero_element()),
            '1': lambda: UiActions.click(page.calculator_standard_page.get_one_element()),
            '2': lambda: UiActions.click(page.calculator_standard_page.get_two_element()),
            '3': lambda: UiActions.click(page.calculator_standard_page.get_three_element()),
            '4': lambda: UiActions.click(page.calculator_standard_page.get_four_element()),
            '5': lambda: UiActions.click(page.calculator_standard_page.get_five_element()),
            '6': lambda: UiActions.click(page.calculator_standard_page.get_six_element()),
            '7': lambda: UiActions.click(page.calculator_standard_page.get_seven_element()),
            '8': lambda: UiActions.click(page.calculator_standard_page.get_eight_element()),
            '9': lambda: UiActions.click(page.calculator_standard_page.get_nine_element()),
            "+": lambda: UiActions.click(page.calculator_standard_page.get_add_element()),
            "-": lambda: UiActions.click(page.calculator_standard_page.get_subtract_element()),
            "*": lambda: UiActions.click(page.calculator_standard_page.get_multiply_element()),
            "/": lambda: UiActions.click(page.calculator_standard_page.get_divide_element()),
            "=": lambda: UiActions.click(page.calculator_standard_page.get_equals_element()),
            ".": lambda: UiActions.click(page.calculator_standard_page.get_decimal_element()),

        }

        if char not in mapping:
            raise ValueError(f"Invalid char: {char}. Supported: digits 0–9 and operators +, -, *, /, =,.")

        mapping[char]()

    @staticmethod
    @allure.step("Clicking on clear")
    def step_click_clear():
        UiActions.click(page.calculator_standard_page.get_clear_element())

    @staticmethod
    @allure.step("Clicking on clear entry")
    def step_click_clear_entry():
        UiActions.click(page.calculator_standard_page.get_clear_entry_element())

    @staticmethod
    @allure.step("Clicking on backspace")
    def step_click_backspace():
        UiActions.click(page.calculator_standard_page.get_backspace_element())

    @staticmethod
    @allure.step("Clicking on negate")
    def step_click_negate():
        UiActions.click(page.calculator_standard_page.get_negate_element())

    @staticmethod
    @allure.step("Clicking on percentage")
    def step_click_percentage():
        UiActions.click(page.calculator_standard_page.get_percentage_element())

    @staticmethod
    @allure.step("Clicking on equals")
    def step_click_equals():
        UiActions.click(page.calculator_standard_page.get_equals_element())
