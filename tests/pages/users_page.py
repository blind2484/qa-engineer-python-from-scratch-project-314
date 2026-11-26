from actions.actions_users import ActionUsers
from pages.start_page import StartPage


class UsersPage(StartPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.users_actions = ActionUsers(driver)

    def open_create_user_form(self):
        self.users_actions.find_create_button().click()
        email = self.users_actions.find_email_field()
        first_name = self.users_actions.find_first_name_field()
        last_name = self.users_actions.find_last_name_field()
        return email, first_name, last_name

    def create_user(self, email, first_name, last_name):
        self.users_actions.enter_email(email)
        self.users_actions.enter_first_name(first_name)
        self.users_actions.enter_last_name(last_name)
        self.users_actions.click_save_button()

    def open_user_to_edit(self, email, first_name, last_name):
        row = self.users_actions.get_user_row(email, first_name, last_name)
        row.click()

    def is_user_displayed(self, email, first_name, last_name):
        return self.users_actions.is_user_exists(email, first_name, last_name)

    def wait_until_user_deleted(self, email, first_name, last_name):
        return self.users_actions.wait_user_disappear(email, first_name, last_name)

    def get_table_state(self):
        table = self.actions.find_table()
        rows = self.actions.table_rows_count()
        emails = self.users_actions.emails()
        first_names = self.users_actions.first_names()
        last_names = self.users_actions.last_names()
        return table.is_displayed(), rows, emails, first_names, last_names

    def select_user_to_edit(self, email="john@google.com", first_name="John", last_name="Doe"):
        self.users_actions.select_user_row(email, first_name, last_name)
        email_filed = self.users_actions.find_email_field()
        first_name_filed = self.users_actions.find_first_name_field()
        last_name_filed = self.users_actions.find_last_name_field()
        return email_filed, first_name_filed, last_name_filed

    def save_button(self):
        button = self.actions.find_save_button()
        return button

    def fill_user_fields(self, email="", first_name="", last_name=""):
        self.users_actions.enter_email(email)
        self.users_actions.enter_first_name(first_name)
        self.users_actions.enter_last_name(last_name)
        self.users_actions.click_save_button()

    def select_user(self, email, first_name, last_name):
        row = self.users_actions.get_user_row(email, first_name, last_name)
        checkbox = self.actions.find_checkbox(row)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def click_delete_user(self):
        self.users_actions.click_delete_button()

    def select_all_users(self):
        self.actions.click_select_all()

    def is_table_empty(self):
        return self.actions.wait_table_empty()