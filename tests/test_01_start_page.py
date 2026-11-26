from actions.actions_start_page import ActionsStartPage
from helpers import open_page


def test_start_page(driver, url):
    open_page(driver, url)

    assert driver.title == "Task manager"

    actions = ActionsStartPage(driver)
    assert actions.find_username_field().is_displayed()
    assert actions.find_password_field().is_displayed()
    assert actions.find_sign_in_button().is_displayed()
