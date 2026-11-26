from locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Actions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_checkbox(self, parent=None):
        target = parent if parent else self.driver
        return target.find_element(*Locators.CHECKBOX)

    def page_title(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.PAGE_TITLE))

    def wait_page_title_text(self, expected_text):
        return self.wait.until(EC.text_to_be_present_in_element(Locators.PAGE_TITLE, expected_text))

    def alert(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.ALERT))

    def selection_count(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.SELECTION_COUNT))

    def clear_field(self, locator):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.click()
        current_value = field.get_attribute("value") or ""
        if current_value:
            field.send_keys(Keys.BACKSPACE * len(current_value))
        return field

    def fill_field(self, locator, text):
        field = self.clear_field(locator)
        field.send_keys(text)

    def select_from_list(self, locator):
        select = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", select)

    def to_users(self):
        return self.wait.until(EC.element_to_be_clickable(Locators.USERS_PAGE))
        
    def to_statuses(self):
        return self.wait.until(EC.element_to_be_clickable(Locators.STATUSES_PAGE))

    def to_labels(self):
        return self.wait.until(EC.element_to_be_clickable(Locators.LABELS_PAGE))

    def to_tasks(self):
        return self.wait.until(EC.element_to_be_clickable(Locators.TASKS_PAGE))

    def find_create_button(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.CREATE_BUTTON))

    def find_save_button(self):
        button = self.wait.until(EC.visibility_of_element_located(Locators.SAVE_BUTTON))
        return button

    def find_delete_button(self):
        button = self.wait.until(EC.visibility_of_element_located(Locators.DELETE_BUTTON))
        return button

    def find_select_all(self):
        element = self.wait.until(EC.presence_of_element_located(Locators.SELECT_ALL))
        return element
    
    def click_save_button(self):
        button = self.find_save_button()
        self.driver.execute_script("arguments[0].click();", button)

    def click_delete_button(self):
        button = self.find_delete_button()
        self.driver.execute_script("arguments[0].click();", button)

    def click_select_all(self):
        button = self.find_select_all()
        self.driver.execute_script("arguments[0].click();", button)

    def find_table(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.TABLE))

    def table_rows_count(self):
        rows = self.wait.until(EC.presence_of_all_elements_located(Locators.TABLE_ROWS))
        return len(rows)

    def wait_table_empty(self):
        return self.wait.until(EC.invisibility_of_element_located(Locators.TABLE_ROWS))