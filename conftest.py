import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default = 'ru', help = 'choose language: ru, en, etc...')

@pytest.fixture()
def browser_language(request):
    browser_language = request.config.getoption('language')
    yield browser_language

@pytest.fixture(scope="function")
def browser():

    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print("\nquit browser..")
    browser.quit()