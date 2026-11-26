from actions.actions import Actions
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class ActionsStartPage(Actions):
    def find_username_field(self):
        return self.driver.find_element(*Locators.USERNAME)

    def find_password_field(self):
        return self.driver.find_element(*Locators.PASSWORD)
    
    def find_sign_in_button(self):
        return self.driver.find_element(*Locators.SIGN_IN_BUTTON)

    def enter_username(self, text):
        self.fill_field(Locators.USERNAME, text)

    def enter_password(self, text):
        self.fill_field(Locators.PASSWORD, text)

    def click_sign_in(self):
        self.driver.find_element(*Locators.SIGN_IN_BUTTON).click()

    def click_user_button(self):
        button = self.wait.until(EC.element_to_be_clickable(Locators.USER))
        button.click()

    def click_logout_button(self):
        button = self.wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)

    def click_save_button(self):
        button = self.wait.until(EC.element_to_be_clickable(Locators.SAVE_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)