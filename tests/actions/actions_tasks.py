from actions.actions import Actions
from locators import Locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class ActionTasks(Actions):
    def find_assignee_field(self):
        return self.driver.find_element(*Locators.ASSIGNEE)

    def find_title_field(self):
        return self.driver.find_element(*Locators.TITLE)

    def find_content_field(self):
        return self.driver.find_element(*Locators.CONTENT)

    def find_status_field(self):
        return self.driver.find_element(*Locators.STATUS)

    def find_label_field(self):
        return self.driver.find_element(*Locators.LABEL)

    def find_task(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.TASK))

    def find_column(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.COLUMN))

    def find_edit_task_button(self):
        task = self.find_task()
        return task.find_element(*Locators.EDIT_TASK_BUTTON)

    def enter_assignee(self):
        self.find_assignee_field().click()
        self.select_from_list(Locators.SELECTED_ASSIGNEE)

    def enter_title(self, text):
        self.fill_field(Locators.TITLE, text)

    def enter_content(self, text):
        self.fill_field(Locators.CONTENT, text)

    def enter_status(self):
        self.find_status_field().click()
        self.select_from_list(Locators.SELECTED_STATUS)

    def enter_modified_status(self):
        self.find_status_field().click()
        self.select_from_list(Locators.MODIFIED_STATUS)

    def enter_label(self):
        self.find_label_field().click()
        self.select_from_list(Locators.SELECTED_LABEL)

    def is_new_task_exists(self):
        try:
            self.wait.until(EC.visibility_of_element_located(Locators.NEW_TASK))
            return True
        except TimeoutException:
            return False

    def wait_initial_tasks_loaded(self):
        return self.wait.until(EC.visibility_of_all_elements_located(Locators.TASKS_ON_DESK))
    
    def count_tasks_on_desk(self):
        return len(self.driver.find_elements(*Locators.TASKS_ON_DESK))

    def select_empty(self):
        self.select_from_list(Locators.EMPTY_FIELD)

    def find_old_name_task(self):
        return self.wait.until(EC.invisibility_of_element_located(Locators.TASK_TO_EDIT))

    def is_modified_task_exists(self):
        try:
            self.wait.until(EC.visibility_of_element_located(Locators.MODIFIED_TASK))
            return True
        except TimeoutException:
            return False

    def move_task(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.find_task())
        action.move_by_offset(10, 10)
        action.pause(0.2)
        action.move_to_element(self.find_column())
        action.pause(0.2)
        action.release()
        action.perform()

    def is_task_removed_from_old_location(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(Locators.TASK_OLD_LOCATION))
            return True
        except TimeoutException:
            return False

    def is_moved_task_in_new_location(self):
        try:
            self.wait.until(EC.visibility_of_element_located(Locators.TASK_NEW_LOCATION))
            return True
        except TimeoutException:
            return False

    def is_deleted_task_not_visible(self):
        return self.wait.until(EC.invisibility_of_element_located(Locators.TASK))