import allure

from extensions.ui_actions import UiActions
import utilities.manage_pages as page


class WebFlows:

    @staticmethod
    @allure.step("Add Samsung Galaxy S6 to cart")
    def step_add_samsung_to_cart():
        UiActions.click(page.web_home_page.get_samsung_galaxy_s6_element())
        UiActions.click(page.web_product_page.get_add_to_cart_element())

    @staticmethod
    @allure.step("Click on Cart in the top navbar")
    def click_cart():
        UiActions.click()
