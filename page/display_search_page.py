from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DisplaySearchPage(BaseAction):

    search_box = By.ID, "android:id/search_src_text"
    text = 'hello'
    back_button = By.XPATH, "//*[@content-desc='收起']"

    def input_search(self):

        self.input(self.search_box, self.text)

    def click_back_button(self):

        self.click(self.back_button)
