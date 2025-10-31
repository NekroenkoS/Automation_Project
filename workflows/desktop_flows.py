import time

import allure
import utilities.manage_pages as page

from extensions.ui_actions import UiActions
from extensions.verifications import Verifications


class DesktopFlows:

    @staticmethod
    @allure.step("Verifiying calculator answer")
    def verify_calculator_answer(expected_num):
        time.sleep(1)
        result_str = page.calculator_standard_page.get_answer_element().text
        actual_num = result_str.replace("Display is ", "").strip()
        Verifications.verify_equals(actual_num,expected_num)

    @staticmethod
    @allure.step("Clicking on number")
    def step_click_on_number(num):
        mapping = {
            0: lambda: UiActions.click(page.calculator_standard_page.get_zero_element()),
            1: lambda: UiActions.click(page.calculator_standard_page.get_one_element()),
            2: lambda: UiActions.click(page.calculator_standard_page.get_two_element()),
            3: lambda: UiActions.click(page.calculator_standard_page.get_three_element()),
            4: lambda: UiActions.click(page.calculator_standard_page.get_four_element()),
            5: lambda: UiActions.click(page.calculator_standard_page.get_five_element()),
            6: lambda: UiActions.click(page.calculator_standard_page.get_six_element()),
            7: lambda: UiActions.click(page.calculator_standard_page.get_seven_element()),
            8: lambda: UiActions.click(page.calculator_standard_page.get_eight_element()),
            9: lambda: UiActions.click(page.calculator_standard_page.get_nine_element())
        }

        if num not in mapping:
            raise ValueError(f"Invalid number: {num}. Only 0–9 are supported.")

        mapping[num]()
    @staticmethod
    @allure.step("Clicking on add")
    def step_click_add():
        UiActions.click(page.calculator_standard_page.get_add_element())

    @staticmethod
    @allure.step("Clicking on subtract")
    def step_click_subtract():
        UiActions.click(page.calculator_standard_page.get_subtract_element())

    @staticmethod
    @allure.step("Clicking on multiply")
    def step_click_multiply():
        UiActions.click(page.calculator_standard_page.get_multiply_element())

    @staticmethod
    @allure.step("Clicking on divide")
    def step_click_divide():
        UiActions.click(page.calculator_standard_page.get_divide_element())

    @staticmethod
    @allure.step("Clicking on equals")
    def step_click_equals():
        UiActions.click(page.calculator_standard_page.get_equals_element())

    @staticmethod
    @allure.step("Clicking on decimal point")
    def step_click_decimal():
        UiActions.click(page.calculator_standard_page.get_decimal_element())

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
