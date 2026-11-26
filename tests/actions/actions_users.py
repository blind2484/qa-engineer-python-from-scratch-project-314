from actions.actions import Actions
from locators import Locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class ActionUsers(Actions):
    def find_email_field(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.EMAIL))

    def find_first_name_field(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.FIRST_NAME))

    def find_last_name_field(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.LAST_NAME))

    def enter_email(self, text):
        self.fill_field(Locators.EMAIL, text)

    def enter_first_name(self, text):
        self.fill_field(Locators.FIRST_NAME, text)

    def enter_last_name(self, text):
        self.fill_field(Locators.LAST_NAME, text)

    def get_user_row(self, email, first_name, last_name):
        locator = Locators.user_row(email, first_name, last_name)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_user_exists(self, email, first_name, last_name):
        locator = Locators.user_row(email, first_name, last_name)
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_user_disappear(self, email, first_name, last_name):
        locator = Locators.user_row(email, first_name, last_name)
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def emails(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.EMAILS))

    def first_names(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.FIRST_NAMES))

    def last_names(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.LAST_NAMES))

    def select_user_row(self, email, first_name, last_name):
        self.get_user_row(email, first_name, last_name).click()