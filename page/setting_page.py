from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    more_button = By.XPATH, "//*[@text='更多']"
    display_button = By.XPATH, "//*[@text='显示']"

    def click_more_button(self):
        self.click(self.more_button)

    def click_display_button(self):
        self.click(self.display_button)
