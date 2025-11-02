from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import WebDriver


zero = (By.NAME, "Zero")
one = (By.NAME, "One")
two = (By.NAME, "Two")
three = (By.NAME, "Three")
four = (By.NAME, "Four")
five = (By.NAME, "Five")
six = (By.NAME, "Six")
seven = (By.NAME, "Seven")
eight = (By.NAME, "Eight")
nine = (By.NAME, "Nine")
add = (By.NAME, "Plus")
subtract = (By.NAME, "Minus")
multiply = (By.NAME, "Multiply by")
divide = (By.NAME, "Divide by")
equals = (By.NAME, "Equals")
decimal = (By.NAME, "Decimal separator")
clear = (By.NAME, "Clear")
clear_entry = (By.NAME, "Clear entry")
backspace = (By.NAME, "Backspace")
negate = (By.XPATH, "//*[@AutomationId='negateButton']")
percentage = (By.NAME, "Percent")
answer = (By.XPATH, "//*[@AutomationId='CalculatorResults']")


class StandardPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_zero_element(self):
        return self.driver.find_element(zero[0], zero[1])

    def get_one_element(self):
        return self.driver.find_element(one[0], one[1])

    def get_two_element(self):
        return self.driver.find_element(two[0], two[1])

    def get_three_element(self):
        return self.driver.find_element(three[0], three[1])

    def get_four_element(self):
        return self.driver.find_element(four[0], four[1])

    def get_five_element(self):
        return self.driver.find_element(five[0], five[1])

    def get_six_element(self):
        return self.driver.find_element(six[0], six[1])

    def get_seven_element(self):
        return self.driver.find_element(seven[0], seven[1])

    def get_eight_element(self):
        return self.driver.find_element(eight[0], eight[1])

    def get_nine_element(self):
        return self.driver.find_element(nine[0], nine[1])

    def get_add_element(self):
        return self.driver.find_element(add[0], add[1])

    def get_subtract_element(self):
        return self.driver.find_element(subtract[0], subtract[1])

    def get_multiply_element(self):
        return self.driver.find_element(multiply[0], multiply[1])

    def get_divide_element(self):
        return self.driver.find_element(divide[0], divide[1])

    def get_equals_element(self):
        return self.driver.find_element(equals[0], equals[1])

    def get_decimal_element(self):
        return self.driver.find_element(decimal[0], decimal[1])

    def get_clear_element(self):
        return self.driver.find_element(clear[0], clear[1])

    def get_clear_entry_element(self):
        return self.driver.find_element(clear_entry[0], clear_entry[1])

    def get_backspace_element(self):
        return self.driver.find_element(backspace[0], backspace[1])

    def get_negate_element(self):
        return self.driver.find_element(negate[0], negate[1])

    def get_percentage_element(self):
        return self.driver.find_element(percentage[0], percentage[1])

    def get_answer_element(self):
        return self.driver.find_element(answer[0], answer[1])
