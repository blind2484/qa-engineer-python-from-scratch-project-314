from actions.actions_labels import ActionLabels
from pages.start_page import StartPage


class LabelsPage(StartPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.labels_actions = ActionLabels(driver)

    def open_create_label_form(self):
        self.labels_actions.find_create_button().click()
        name = self.labels_actions.find_name_field()
        return name

    def create_label(self, name):
        self.labels_actions.enter_name(name)
        self.labels_actions.click_save_button()

    def open_label_to_edit(self, name):
        row = self.labels_actions.get_label_row(name)
        row.click()

    def is_label_displayed(self, name):
        return self.labels_actions.is_label_exists(name)

    def wait_until_label_deleted(self, name):
        return self.labels_actions.wait_label_disappear(name)

    def get_table_state(self):
        table = self.actions.find_table()
        rows = self.actions.table_rows_count()
        names = self.labels_actions.names()
        return table.is_displayed(), rows, names

    def select_label_to_edit(self, name):
        self.labels_actions.select_label_row(name)
        name_filed = self.labels_actions.find_name_field()
        return name_filed

    def save_button(self):
        button = self.actions.find_save_button()
        return button

    def fill_label_fields(self, name=""):
        self.labels_actions.enter_name(name)
        self.labels_actions.click_save_button()

    def select_label(self, name):
        row = self.labels_actions.get_label_row(name)
        checkbox = self.actions.find_checkbox(row)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def click_delete_label(self):
        self.labels_actions.click_delete_button()

    def select_all_labels(self):
        self.actions.click_select_all()

    def is_table_empty(self):
        return self.actions.wait_table_empty()