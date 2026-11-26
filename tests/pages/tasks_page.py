from actions.actions_tasks import ActionTasks
from pages.start_page import StartPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TasksPage(StartPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.tasks_actions = ActionTasks(driver)

    def open_create_task_form(self):
        self.tasks_actions.find_create_button().click()
        '''assignee = self.tasks_actions.find_assignee_field()
        title = self.tasks_actions.find_title_field()
        content = self.tasks_actions.find_content_field()
        status = self.tasks_actions.find_status_field()
        label = self.tasks_actions.find_label_field()
        return assignee, title, content, status, label'''

    def create_task(self, title="", content=""):
        self.tasks_actions.enter_assignee()
        self.tasks_actions.enter_title(title)
        self.tasks_actions.enter_content(content)
        self.tasks_actions.enter_status()
        self.tasks_actions.enter_label()
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.tasks_actions.click_save_button()

    def is_new_task_displayed_in_right_column(self):
        return self.tasks_actions.is_new_task_exists()

    def wait_tasks_loaded(self):
        return self.tasks_actions.wait_initial_tasks_loaded()

    def tasks_displayed_on_desk(self):
        return self.tasks_actions.count_tasks_on_desk()

    def wait_tasks_count_less_than(self, initial_count):
        return self.wait.until(lambda d: self.tasks_displayed_on_desk() < initial_count)

    def wait_tasks_count_equals(self, initial_count):
        return self.wait.until(lambda d: self.tasks_displayed_on_desk() == initial_count)

    def select_assignee(self):
        self.tasks_actions.enter_assignee()

    def select_status(self):
        self.tasks_actions.enter_status()

    def select_label(self):
        self.tasks_actions.enter_label()

    def empty_assignee(self):
        self.tasks_actions.find_assignee_field().click()
        self.tasks_actions.select_empty()

    def empty_status(self):
        self.tasks_actions.find_status_field().click()
        self.tasks_actions.select_empty()

    def empty_label(self):
        self.tasks_actions.find_label_field().click()
        self.tasks_actions.select_empty()

    def go_to_edit_task(self):
        self.tasks_actions.find_edit_task_button().click()

    def edit_task(self, title="", content=""):
        self.tasks_actions.enter_assignee()
        self.tasks_actions.enter_title(title)
        self.tasks_actions.enter_content(content)
        self.tasks_actions.enter_modified_status()
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.tasks_actions.click_save_button()

    def is_old_name_not_displayed(self):
        return self.tasks_actions.find_old_name_task()

    def drag_and_drop_task(self):
        self.tasks_actions.move_task()

    def is_modified_task_displayed_in_right_column(self):
        return self.tasks_actions.is_modified_task_exists()

    def is_task_moved(self):
        return (self.tasks_actions.is_task_removed_from_old_location() and self.tasks_actions.is_moved_task_in_new_location())

    def click_delete_task(self):
        self.tasks_actions.click_delete_button()

    def is_deleted_task_not_displayed(self):
        return self.tasks_actions.is_deleted_task_not_visible()