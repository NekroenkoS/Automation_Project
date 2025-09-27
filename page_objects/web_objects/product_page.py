from selenium.webdriver.common.by import By

add_to_cart_button = (By.LINK_TEXT, "Add to cart")
name_of_product = (By.CSS_SELECTOR, "div[class='row']>div>h2")

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def get_add_to_cart_element(self):
        return self.driver.find_element(add_to_cart_button[0], add_to_cart_button[1])

    def get_name_of_product_element(self):
        return self.driver.find_element(name_of_product[0], name_of_product[1])