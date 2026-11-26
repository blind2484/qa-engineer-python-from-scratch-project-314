from actions.actions_statuses import ActionStatuses
from pages.start_page import StartPage


class StatusesPage(StartPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.statuses_actions = ActionStatuses(driver)

    def open_create_status_form(self):
        self.statuses_actions.find_create_button().click()
        name = self.statuses_actions.find_name_field()
        slug = self.statuses_actions.find_slug_field()
        return name, slug

    def create_status(self, name, slug):
        self.statuses_actions.enter_name(name)
        self.statuses_actions.enter_slug(slug)
        self.statuses_actions.click_save_button()

    def open_status_to_edit(self, name, slug):
        row = self.statuses_actions.get_status_row(name, slug)
        row.click()

    def is_status_displayed(self, name, slug):
        return self.statuses_actions.is_status_exists(name, slug)

    def wait_until_status_deleted(self, name, slug):
        return self.statuses_actions.wait_status_disappear(name, slug)

    def get_table_state(self):
        table = self.actions.find_table()
        rows = self.actions.table_rows_count()
        names = self.statuses_actions.names()
        slugs = self.statuses_actions.slugs()
        return table.is_displayed(), rows, names, slugs

    def select_status_to_edit(self, name, slug):
        self.statuses_actions.select_status_row(name, slug)
        name_filed = self.statuses_actions.find_name_field()
        slug_filed = self.statuses_actions.find_slug_field()
        return name_filed, slug_filed

    def save_button(self):
        button = self.actions.find_save_button()
        return button

    def fill_status_fields(self, name="", slug=""):
        self.statuses_actions.enter_name(name)
        self.statuses_actions.enter_slug(slug)
        self.statuses_actions.click_save_button()

    def select_status(self, name, slug):
        row = self.statuses_actions.get_status_row(name, slug)
        checkbox = self.actions.find_checkbox(row)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def click_delete_status(self):
        self.statuses_actions.click_delete_button()

    def select_all_statuses(self):
        self.actions.click_select_all()

    def is_table_empty(self):
        return self.actions.wait_table_empty()