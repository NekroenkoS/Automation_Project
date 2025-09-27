from selenium.webdriver.common.by import By

galaxy_s6_product_page = (By.LINK_TEXT, "Samsung galaxy s6")
nokia_lumia_1520_product_page = (By.LINK_TEXT, "Nokia lumia 1520")
nexus_6_product_page = (By.LINK_TEXT, "Nexus 6")
galaxy_s7_product_page = (By.LINK_TEXT, "Samsung galaxy s7")
iphone_6_32gb_product_page = (By.LINK_TEXT, "Iphone 6 32gb")
sony_xperia_z5_product_page = (By.LINK_TEXT, "Sony xperia z5")
htc_one_m9_product_page = (By.LINK_TEXT, "HTC One M9")
sony_vaio_i5_product_page = (By.LINK_TEXT, "Sony vaio i5")
sony_vaio_i7_product_page = (By.LINK_TEXT, "Sony vaio i7")


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_page_element(self,item):
        return self.driver.find_element(item[0], item[1])

    def get_samsung_galaxy_s6_product_page_element(self):
        return self.driver.find_element(galaxy_s6_product_page[0], galaxy_s6_product_page[1])

    def get_nokia_lumia_1520_product_page_element(self):
        return self.driver.find_element(nokia_lumia_1520_product_page[0], nokia_lumia_1520_product_page[1])

    def get_nexus_6_product_page_element(self):
        return self.driver.find_element(nexus_6_product_page[0], nexus_6_product_page[1])

    def get_galaxy_s7_product_page_element(self):
        return self.driver.find_element(galaxy_s7_product_page[0], galaxy_s7_product_page[1])

    def get_iphone_6_32gb_product_page_element(self):
        return self.driver.find_element(iphone_6_32gb_product_page[0], iphone_6_32gb_product_page[1])

    def get_sony_xperia_z5_product_page_element(self):
        return self.driver.find_element(sony_xperia_z5_product_page[0], sony_xperia_z5_product_page[1])

    def get_htc_one_m9_product_page_element(self):
        return self.driver.find_element(htc_one_m9_product_page[0], htc_one_m9_product_page[1])

    def get_sony_vaio_i5_product_page_element(self):
        return self.driver.find_element(sony_vaio_i5_product_page[0], sony_vaio_i5_product_page[1])

    def get_sony_vaio_i7_product_page_element(self):
        return self.driver.find_element(sony_vaio_i7_product_page[0], sony_vaio_i7_product_page[1])
