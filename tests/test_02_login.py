from locators import Locators
from pages.start_page import StartPage


def test_login(driver, actions, url):
    page = StartPage(driver)
    page.open(url)
    page.login("user", "pass")

    assert actions.wait_page_title_text("Welcome to the administration")
    assert page.text_of(Locators.USER) == "Jane Doe"