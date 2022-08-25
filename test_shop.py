from pages.start_page import StartPage
from pages.environment import Env


class TestUserInApp:

    def test_open_shop(self, browser):
        link = Env.URL
        page = StartPage(browser, link)
        page.open_url()
        page.should_be_start_page()
        page.go_to_women_page()
        page.is_page_correct()
