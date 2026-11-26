import os

import pytest
from actions.actions import Actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def url():
    return os.getenv("APP_BASE_URL", "http://localhost:5173/")


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture
def actions(driver):
    return Actions(driver)