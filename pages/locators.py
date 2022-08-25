from selenium.webdriver.common.by import  By


class StartPageLocators:
    TITLE_WOMEN = (By.CSS_SELECTOR, ".sf-menu.clearfix.menu-content.sf-js-enabled.sf-arrows > li:nth-child(1)")
    BLOCK_WOMEN = (By.CSS_SELECTOR, ".navigation_page")
    BLOCK_TEXT = "Women"
