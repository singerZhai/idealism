from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MobileNetworkPage(BaseAction):
    first_network_type = By.XPATH, "//*[@text='首选网络类型']"
    network_3g = By.XPATH, "//*[@text='3G']"
    network_2g = By.XPATH, "//*[@text='2G']"

    def click_first_network_type(self):
        self.click(self.first_network_type)

    def click_3g_button(self):
        self.click(self.network_3g)

    def click_2g_button(self):
        self.click(self.network_2g)