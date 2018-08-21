from base.base_driver import init_driver
from page.display_page import DisplayPage
from page.display_search_page import DisplaySearchPage
from page.setting_page import SettingPage


class TestDisplaySearch:

    def setup(self):
        self.driver = init_driver()
        self.display_page = DisplayPage(self.driver)
        self.display_search_page = DisplaySearchPage(self.driver)
        self.setting_page = SettingPage(self.driver)

    # @pytest.mark.skipif(True, reason='未完成方法')
    def test_display_search(self):
        self.setting_page.click_display_button()
        self.display_page.click_search_button()
        self.display_search_page.input_search()
        self.display_search_page.click_back_button()
