from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseWebDriver:

    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_url(self):
        self.browser.get(self.url)

    def find_and_click_button(self, locator_name, locator_value, timeout=10):
        button = WebDriverWait(self.browser, timeout, 2, TimeoutException). \
            until(EC.element_to_be_clickable((locator_name, locator_value)))
        button.click()

    # def find_and_send_key(self, locator_name, locator_value, text, timeout=10):
    #     field = WebDriverWait(self.browser, timeout, 2, TimeoutException). \
    #         until(EC.presence_of_element_located((locator_name, locator_value)))
    #     field.clear()
    #     field.send_keys(text)

    def is_element_present(self, locator_name, locator_value, timeout=10):
        WebDriverWait(self.browser, timeout, 2, TimeoutException). \
            until(EC.presence_of_element_located((locator_name, locator_value)))

    def is_element_text_correct(self, locator_name, locator_value, text, timeout=10):
        # element_info = self.browser.find_element(locator_name, locator_value)
        # element_text = element_info.text
        # assert element_text == valid_element_text, "Element text is invalid or incorrect"
        WebDriverWait(self.browser, timeout, 2, TimeoutException). \
            until(EC.text_to_be_present_in_element((locator_name, locator_value), text))