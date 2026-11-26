import pytest
from pages.tasks_page import TasksPage


@pytest.fixture
def page(driver, url):
    page = TasksPage(driver)
    page.open(url)
    page.login("user", "pass")
    page.go_to_tasks()
    return page


def test_create_task(actions, page):
    assert actions.page_title().text == "Tasks"
    page.open_create_task_form()
    assert actions.page_title().text == "Create Task"
    page.create_task(title="New Task", content="new task content")
    assert actions.page_title().text == "Task New Task"
    page.go_to_tasks()
    assert actions.page_title().text == "Tasks"
    assert page.is_new_task_displayed_in_right_column()


def test_tasks_list(page):
    page.wait_tasks_loaded()
    all_tasks = page.tasks_displayed_on_desk()
    assert all_tasks > 0
    
    page.select_assignee()
    assert page.wait_tasks_count_less_than(all_tasks)
    page.empty_assignee()
    assert page.wait_tasks_count_equals(all_tasks)

    page.select_status()
    assert page.wait_tasks_count_less_than(all_tasks)
    page.empty_status()
    assert page.wait_tasks_count_equals(all_tasks)

    page.select_label()
    assert page.wait_tasks_count_less_than(all_tasks)
    page.empty_label()
    assert page.wait_tasks_count_equals(all_tasks)    


def test_task_edit(actions, page):
    page.go_to_edit_task()
    assert actions.page_title().text == "Task Task 13"
    page.edit_task(title="Modified task 13", content="Modified task 13 description")
    assert actions.page_title().text == "Tasks"
    assert page.is_old_name_not_displayed()
    assert page.is_modified_task_displayed_in_right_column()


def test_drag_and_drop_task(page):
    page.drag_and_drop_task()
    assert page.is_task_moved()


def test_delete_task(actions, page):
    page.go_to_edit_task()
    assert actions.page_title().text == "Task Task 13"
    page.click_delete_task()
    assert actions.page_title().text == "Tasks"
    assert page.is_deleted_task_not_displayed()