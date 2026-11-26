from actions.actions import Actions
from locators import Locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class ActionLabels(Actions):
    def find_name_field(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.NAME))

    def enter_name(self, text):
        self.fill_field(Locators.NAME, text)

    def get_label_row(self, name):
        locator = Locators.label_row(name)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_label_exists(self, name):
        locator = Locators.label_row(name)
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_label_disappear(self, name):
        locator = Locators.label_row(name)
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def names(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.NAMES))

    def select_label_row(self, name):
        self.get_label_row(name).click()