import test_cases.conftest
from page_objects.web_pages.home_page import HomePage
from page_objects.web_pages.login_page import LoginPage
from page_objects.web_pages.product_page import ProductPage
from page_objects.web_pages.top_navbar import TopNavBar

# Web Objects
web_login = None
web_home_page = None
web_product_page = None
web_top_nav_bar = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        global web_login, web_home_page, web_product_page, web_top_nav_bar
        web_login = LoginPage(test_cases.conftest.driver)
        web_home_page = HomePage(test_cases.conftest.driver)
        web_product_page = ProductPage(test_cases.conftest.driver)
        web_top_nav_bar = TopNavBar(test_cases.conftest.driver)
