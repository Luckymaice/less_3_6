import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_for_two_language(browser, browser_language):
    link = f"https://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/"
    browser.get(link)

    add_buttons = browser.find_elements(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')

    assert len(add_buttons) > 0, 'Кнопки добавления в корзину не существует!'
