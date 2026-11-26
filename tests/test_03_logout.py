from pages.start_page import StartPage
from selenium.webdriver.common.by import By


def test_logout(driver, url):
    page = StartPage(driver)
    page.open(url)
    page.login("user", "pass")
    page.logout()

    assert driver.find_element(By.CLASS_NAME, "css-1bz6oir").is_displayed()