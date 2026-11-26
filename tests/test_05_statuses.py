import pytest
from pages.statuses_page import StatusesPage


@pytest.fixture
def page(driver, url):
    page = StatusesPage(driver)
    page.open(url)
    page.login("user", "pass")
    page.go_to_statuses()
    return page


def test_create_status(actions, page):
    assert actions.page_title().text == "Task statuses"

    name, slug = page.open_create_status_form()
    assert name.is_displayed()
    assert slug.is_displayed()
    assert actions.page_title().text == "Create Task status"    

    page.create_status("New Name", "new_name_slug")
    assert actions.page_title().text == "Task status New Name"
    page.go_to_statuses()
    assert page.is_status_displayed("New Name", "new_name_slug")


def test_statuses_list(page):
    is_visible, rows_count, names, slugs = page.get_table_state()
    assert is_visible
    assert rows_count == len(names) == len(slugs) > 0
    assert all(cell.text.strip() != "" for cell in names)
    assert all(cell.text.strip() != "" for cell in slugs)


def test_edit_status(page, actions):
    name, slug = page.select_status_to_edit("Draft", "draft")
    assert actions.page_title().text == "Task status Draft"
    assert name.is_displayed()
    assert slug.is_displayed()
    assert page.save_button().is_displayed()
    assert not page.save_button().is_enabled()

    page.fill_status_fields(name="New Name", slug="new_name_slug")
    assert actions.page_title().text == "Task statuses"
    assert not page.is_status_displayed("Draft", "draft")
    assert page.is_status_displayed("New Name", "new_name_slug")


def test_delete_one_status(page, actions):
    status_to_delete = [("Draft", "draft")]

    for name, slug in status_to_delete:
        page.select_status(name, slug)
    assert "1 item selected" in actions.selection_count().text
    
    page.click_delete_status()
    for name, slug in status_to_delete:
        assert page.wait_until_status_deleted(name, slug)


def test_delete_multiple_statuses(page, actions):
    status_to_delete = [
        ("Draft", "draft"),
        ("To Be Fixed", "to_be_fixed"),
        ("To Publish", "to_publish")
    ]

    for name, slug in status_to_delete:
        page.select_status(name, slug)
    assert "3 items selected" in actions.selection_count().text
    
    page.click_delete_status()
    for name, slug in status_to_delete:
        assert page.wait_until_status_deleted(name, slug)


def test_delete_all_statuses(page, actions):
    page.select_all_statuses()
    assert "items selected" in actions.selection_count().text

    page.click_delete_status()
    assert page.is_table_empty