from actions.actions_start_page import ActionsStartPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class StartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionsStartPage(driver)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def text_of(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text
    
    def login(self, username, password):
        self.actions.enter_username(username)
        self.actions.enter_password(password)
        self.actions.click_sign_in()

    def logout(self):
        self.actions.click_user_button()
        self.actions.click_logout_button()

    def go_to_users(self):
        self.actions.to_users().click()
    
    def go_to_statuses(self):
        self.actions.to_statuses().click()
    
    def go_to_labels(self):
        self.actions.to_labels().click()
    
    def go_to_tasks(self):
        self.actions.to_tasks().click()