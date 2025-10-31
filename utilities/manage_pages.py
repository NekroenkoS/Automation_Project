import test_cases.conftest
from page_objects.desktop_objects.standard_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.after_login_page import AfterLoginPage
from page_objects.mobile_objects.echo_screen_page import EchoScreenPage
from page_objects.mobile_objects.list_demo_page import ListDemoPage
from page_objects.mobile_objects.main_page import MainPage
from page_objects.mobile_objects.mobile_login_page import MobileLoginPage
from page_objects.web_objects.after_purchase_page import AfterPurchasePage
from page_objects.web_objects.cart_page import CartPage
from page_objects.web_objects.contact_us_page import ContactUsPage
from page_objects.web_objects.home_page import HomePage
from page_objects.web_objects.web_login_page import WebLoginPage
from page_objects.web_objects.place_order_page import PlaceOrderPage
from page_objects.web_objects.product_page import ProductPage
from page_objects.web_objects.top_navbar import TopNavBar

# Web Objects
web_login_page = None
web_home_page = None
web_product_page = None
web_top_nav_bar = None
web_cart_page = None
web_contact_us_page = None
web_place_order_page = None
web_after_purchase_page = None

# Mobile Objects
mobile_after_login_page = None
mobile_echo_screen_page = None
mobile_login_page = None
mobile_main_page = None
mobile_list_demo_page = None

# Electron Objects
electron_task_page = None

# Desktop Objects
calculator_standard_page = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        global web_login_page, web_home_page, web_product_page, web_top_nav_bar, web_cart_page, web_contact_us_page, web_place_order_page, web_after_purchase_page
        web_login_page = WebLoginPage(test_cases.conftest.driver)
        web_home_page = HomePage(test_cases.conftest.driver)
        web_product_page = ProductPage(test_cases.conftest.driver)
        web_top_nav_bar = TopNavBar(test_cases.conftest.driver)
        web_cart_page = CartPage(test_cases.conftest.driver)
        web_contact_us_page = ContactUsPage(test_cases.conftest.driver)
        web_place_order_page = PlaceOrderPage(test_cases.conftest.driver)
        web_after_purchase_page = AfterPurchasePage(test_cases.conftest.driver)

    @staticmethod
    def init_mobile_pages():
        global mobile_after_login_page, mobile_echo_screen_page, mobile_login_page, mobile_main_page, mobile_list_demo_page
        mobile_after_login_page = AfterLoginPage(test_cases.conftest.driver)
        mobile_echo_screen_page = EchoScreenPage(test_cases.conftest.driver)
        mobile_login_page = MobileLoginPage(test_cases.conftest.driver)
        mobile_main_page = MainPage(test_cases.conftest.driver)
        mobile_list_demo_page = ListDemoPage(test_cases.conftest.driver)

    @staticmethod
    def init_electron_pages():
        global electron_task_page
        electron_task_page = TaskPage(test_cases.conftest.driver)

    @staticmethod
    def init_desktop_pages():
        global calculator_standard_page
        calculator_standard_page = StandardPage(test_cases.conftest.driver)
