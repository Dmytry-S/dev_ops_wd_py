import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function", autouse=True)
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    yield browser
    browser.quit()