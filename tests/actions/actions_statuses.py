from actions.actions import Actions
from locators import Locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class ActionStatuses(Actions):
    def find_name_field(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.NAME))

    def find_slug_field(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.SLUG))

    def enter_name(self, text):
        self.fill_field(Locators.NAME, text)

    def enter_slug(self, text):
        self.fill_field(Locators.SLUG, text)

    def get_status_row(self, name, slug):
        locator = Locators.status_row(name, slug)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_status_exists(self, name, slug):
        locator = Locators.status_row(name, slug)
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_status_disappear(self, name, slug):
        locator = Locators.status_row(name, slug)
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def names(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.NAMES))

    def slugs(self):
        return self.wait.until(EC.presence_of_all_elements_located(Locators.SLUGS))

    def select_status_row(self, name, slug):
        self.get_status_row(name, slug).click()