from helpers import build_label_xpath, build_status_xpath, build_user_xpath
from selenium.webdriver.common.by import By


class Locators:
#Локаторы для login/logout
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    USER = (By.CSS_SELECTOR, 'button[aria-label="Profile"]')
    LOGOUT_BUTTON = (By.XPATH, "//li[contains(., 'Logout')]")

#Локаторы для переходов на страницы
    USERS_PAGE = (By.CSS_SELECTOR, "a[href='#/users']")
    STATUSES_PAGE = (By.CSS_SELECTOR, "a[href='#/task_statuses']")
    LABELS_PAGE = (By.CSS_SELECTOR, "a[href='#/labels']")
    TASKS_PAGE = (By.CSS_SELECTOR, "a[href='#/tasks']")

#Локаторы общие, для всех страниц
    CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    PAGE_TITLE = (By.ID, "react-admin-title")
    ALERT = (By.CSS_SELECTOR, "div[role='alert'].RaNotification-error")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Save']")
    CREATE_BUTTON = (By.CSS_SELECTOR, "a[aria-label='Create']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Delete']")
    SELECT_ALL = (By.CSS_SELECTOR, 'input[aria-label="Select all"]')
    TABLE = (By.TAG_NAME, "table")
    TABLE_ROWS = (By.CSS_SELECTOR, "tbody tr")
    SELECTION_COUNT = (By.CSS_SELECTOR, "[data-test='bulk-actions-toolbar'] h6")

# Локаторы для страницы USERS
    EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lastName"]')
    EMAILS = (By.CSS_SELECTOR, "tbody td.column-email")
    FIRST_NAMES = (By.CSS_SELECTOR, "tbody td.column-firstName")
    LAST_NAMES = (By.CSS_SELECTOR, "tbody td.column-lastName")

    @staticmethod
    def user_row(email, first_name, last_name):
        return (By.XPATH, build_user_xpath(email, first_name, last_name))
    
#Локаторы для страницы STATUSES
    NAME = (By.CSS_SELECTOR, 'input[name="name"]')
    SLUG = (By.CSS_SELECTOR, 'input[name="slug"]')
    NAMES = (By.CSS_SELECTOR, "tbody td.column-name")
    SLUGS = (By.CSS_SELECTOR, "tbody td.column-slug")

    @staticmethod
    def status_row(name, slug):
        return (By.XPATH, build_status_xpath(name, slug))

#Локаторы для страницы LABELS
    @staticmethod
    def label_row(name):
        return (By.XPATH, build_label_xpath(name))

#Локаторы для страницы TASKS
    ASSIGNEE = (By.CSS_SELECTOR, ".ra-input-assignee_id div[role='combobox']")
    STATUS = (By.CSS_SELECTOR, ".ra-input-status_id div[role='combobox']")
    LABEL = (By.CSS_SELECTOR, ".ra-input-label_id div[role='combobox']")
    TITLE = (By.CSS_SELECTOR, 'input[name="title"]')
    CONTENT = (By.CSS_SELECTOR, 'textarea[name="content"]')

    TASK = (By.CSS_SELECTOR, "[data-rfd-draggable-id='13']")
    COLUMN = (By.CSS_SELECTOR, "[data-rfd-droppable-id='2']")
    NEW_TASK = (By.XPATH, "//h6[normalize-space()='To Be Fixed']/following-sibling::div//div[normalize-space()='New Task']")
    EDIT_TASK_BUTTON = (By.CSS_SELECTOR, "[aria-label='Edit']")

    #локаторы для выбора CREATE/EDIT и отображения на доске
    SELECTED_ASSIGNEE = (By.XPATH, "//li[@role='option' and normalize-space()='alice@hotmail.com']")
    SELECTED_STATUS = (By.XPATH, "//li[@role='option' and normalize-space()='To Be Fixed']")
    SELECTED_LABEL = (By.XPATH, "//li[@role='option' and normalize-space()='task']")
    MODIFIED_STATUS = (By.XPATH, "//li[@role='option' and normalize-space()='To Publish']")

    #локаторы для доски задач
    DISPLAYED_TASKS = (By.CSS_SELECTOR, "[data-rfd-draggable-id]")
    CLEAR_IN_POPUP_MENU = (By.CSS_SELECTOR, "ul[role='listbox'] li[role='option'][data-value='']")
    TASKS_ON_DESK = (By.CSS_SELECTOR, "[data-rfd-draggable-id]")
    EMPTY_FIELD = (By.CSS_SELECTOR, "ul[role='listbox'] li[role='option'][data-value='']")

    TASK_TO_EDIT = (By.XPATH, "//div[normalize-space()='Task 13']")
    MODIFIED_TASK = (By.XPATH, "//h6[normalize-space()='To Publish']/following-sibling::div//div[normalize-space()='Modified task 13']")

    TASK_OLD_LOCATION = (By.XPATH, "//h6[normalize-space()='To Be Fixed']/following-sibling::div//div[normalize-space()='Task 13']")
    TASK_NEW_LOCATION = (By.XPATH, "//h6[normalize-space()='To Review']/following-sibling::div//div[normalize-space()='Task 13']")
