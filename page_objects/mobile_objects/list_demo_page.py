from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

altocumulus = (By.ID, "Altocumulus")
altostratus = (By.ID, "Altostratus")
aws = (By.ID, "AWS")
azure = (By.ID, "Azure")
cirrocumulus = (By.ID, "Cirrocumulus")
cirrostratus = (By.ID, "Cirrostratus")
cirrus = (By.ID, "Cirrus")
creative_cloud = (By.ID, "Creative Cloud")
cumulonimbus = (By.ID, "Cumulonimbus")
cumulus_congestus = (By.ID, "Cumulus Congestus")
cumulus_humilis = (By.ID, "Cumulus humilis")
dropbox = (By.ID, "Dropbox")
fog = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./*[@text='Fog']]")
google_cloud_platform = (By.ID, "Google Cloud Platform")
ibm_cloud = (By.ID, "IBM Cloud")
kamatera = (By.ID, "Kamatera")
nimbostratus = (By.ID, "Nimbostratus")
noctilucent = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./parent::*[@id='Noctilucent'] and ./*[@text]]")
oracle_cloud = (By.ID, "Oracle Cloud")
phoenix_nap = (By.ID, "PhoenixNAP")
polar_stratospheric = (By.ID, "Polar Stratospheric")
rackspace_cloud = (By.ID, "Rackspace Cloud")
red_hat = (By.XPATH, "//*[@id='RNE__LISTITEM__padView' and ./parent::*[@id='RedHat'] and ./*[@text]]")
salesforce_cloud = (By.ID, "Salesforce Cloud")
sap = (By.ID, "SAP")
science_soft = (By.ID, "ScienceSoft")
stratocumulus = (By.ID, "Stratocumulus")
stratus = (By.ID, "Stratus")
message = (By.ID, "message")


class ListDemoPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_altocumulus_element(self):
        return self.driver.find_element(altocumulus[0], altocumulus[1])

    def get_altostratus_element(self):
        return self.driver.find_element(altostratus[0], altostratus[1])

    def get_aws_element(self):
        return self.driver.find_element(aws[0], aws[1])

    def get_azure_element(self):
        return self.driver.find_element(azure[0], azure[1])

    def get_cirrocumulus_element(self):
        return self.driver.find_element(cirrocumulus[0], cirrocumulus[1])

    def get_cirrostratus_element(self):
        return self.driver.find_element(cirrostratus[0], cirrostratus[1])

    def get_cirrus_element(self):
        return self.driver.find_element(cirrus[0], cirrus[1])

    def get_creative_cloud_element(self):
        return self.driver.find_element(creative_cloud[0], creative_cloud[1])

    def get_cumulonimbus_element(self):
        return self.driver.find_element(cumulonimbus[0], cumulonimbus[1])

    def get_cumulus_congestus_element(self):
        return self.driver.find_element(cumulus_congestus[0], cumulus_congestus[1])

    def get_cumulus_humilis_element(self):
        return self.driver.find_element(cumulus_humilis[0], cumulus_humilis[1])

    def get_dropbox_element(self):
        return self.driver.find_element(dropbox[0], dropbox[1])

    def get_fog_element(self):
        return self.driver.find_element(fog[0], fog[1])

    def get_google_cloud_platform_element(self):
        return self.driver.find_element(google_cloud_platform[0], google_cloud_platform[1])

    def get_ibm_cloud_element(self):
        return self.driver.find_element(ibm_cloud[0], ibm_cloud[1])

    def get_kamatera_element(self):
        return self.driver.find_element(kamatera[0], kamatera[1])

    def get_nimbostratus_element(self):
        return self.driver.find_element(nimbostratus[0], nimbostratus[1])

    def get_noctilucent_element(self):
        return self.driver.find_element(noctilucent[0], noctilucent[1])

    def get_oracle_cloud_element(self):
        return self.driver.find_element(oracle_cloud[0], oracle_cloud[1])

    def get_phoenix_nap_element(self):
        return self.driver.find_element(phoenix_nap[0], phoenix_nap[1])

    def get_polar_stratospheric_element(self):
        return self.driver.find_element(polar_stratospheric[0], polar_stratospheric[1])

    def get_rackspace_cloud_element(self):
        return self.driver.find_element(rackspace_cloud[0], rackspace_cloud[1])

    def get_red_hat_element(self):
        return self.driver.find_element(red_hat[0], red_hat[1])

    def get_salesforce_cloud_element(self):
        return self.driver.find_element(salesforce_cloud[0], salesforce_cloud[1])

    def get_sap_element(self):
        return self.driver.find_element(sap[0], sap[1])

    def get_science_soft_element(self):
        return self.driver.find_element(science_soft[0], science_soft[1])

    def get_stratocumulus_element(self):
        return self.driver.find_element(stratocumulus[0], stratocumulus[1])

    def get_stratus_element(self):
        return self.driver.find_element(stratus[0], stratus[1])

    def get_message_element(self):
        return self.driver.find_element(message[0], message[1])
