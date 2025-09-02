from selenium.webdriver.common.by import By

galaxy_s6_product_page = (By.LINK_TEXT, "Samsung galaxy s6")


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_samsung_galaxy_s6_product_page_element(self):
        return self.driver.find_element(galaxy_s6_product_page[0], galaxy_s6_product_page[1])
