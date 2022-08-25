from .base_methods import BaseWebDriver
from .locators import StartPageLocators
from .environment import Env


class StartPage(BaseWebDriver):

    def should_be_start_page(self):
        # Check if there is a login form frame on the page available
        self.is_page_open()

    def go_to_women_page(self):
        self.find_and_click_button(*StartPageLocators.TITLE_WOMEN)

    def is_page_open(self):
        # To make sure that the page is open, check that there is a button "UPGRADE" on the page available
        self.is_element_present(*StartPageLocators.TITLE_WOMEN)

    def is_page_correct(self):
        self.is_element_text_correct(*StartPageLocators.BLOCK_WOMEN, StartPageLocators.BLOCK_TEXT)