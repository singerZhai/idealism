from base.base_driver import init_driver
from page.mobile_network_page import MobileNetworkPage
from page.more_page import MorePage
from page.setting_page import SettingPage


class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.more_page = MorePage(self.driver)
        self.mobile_page = MobileNetworkPage(self.driver)
        self.setting_page = SettingPage(self.driver)

    def test_setting_3g_network(self):
        self.setting_page.click_more_button()
        self.more_page.click_mobile_network_button()
        self.mobile_page.click_first_network_type()
        self.mobile_page.click_3g_button()

    def test_setting_2g_network(self):
        self.setting_page.click_more_button()
        self.more_page.click_mobile_network_button()
        self.mobile_page.click_first_network_type()
        self.mobile_page.click_2g_button()

    def display_input(self):
        pass