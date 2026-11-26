import pytest
from pages.labels_page import LabelsPage


@pytest.fixture
def page(driver, url):
    page = LabelsPage(driver)
    page.open(url)
    page.login("user", "pass")
    page.go_to_labels()
    return page


def test_create_label(actions, page):
    assert actions.page_title().text == "Labels"

    name = page.open_create_label_form()
    assert name.is_displayed()
    assert actions.page_title().text == "Create Label"    

    page.create_label("new_name")
    assert actions.page_title().text == "Label new_name"
    page.go_to_labels()
    assert page.is_label_displayed("new_name")


def test_labels_list(page):
    is_visible, rows_count, names = page.get_table_state()
    assert is_visible
    assert rows_count == len(names) > 0
    assert all(cell.text.strip() != "" for cell in names)


def test_edit_label(page, actions):
    name = page.select_label_to_edit("feature")
    assert actions.page_title().text == "Label feature"
    assert name.is_displayed()
    assert page.save_button().is_displayed()
    assert not page.save_button().is_enabled()

    page.fill_label_fields(name="new_label")
    assert actions.page_title().text == "Labels"
    assert not page.is_label_displayed("feature")
    assert page.is_label_displayed("new_label")


def test_delete_one_label(page, actions):
    label_to_delete = [("bug")]

    for name in label_to_delete:
        page.select_label(name)
    assert "1 item selected" in actions.selection_count().text
    
    page.click_delete_label()
    for name in label_to_delete:
        assert page.wait_until_label_deleted(name)


def test_delete_multiple_labels(page, actions):
    label_to_delete = [
        ("bug"),
        ("feature"),
        ("task")
    ]

    for name in label_to_delete:
        page.select_label(name)
    assert "3 items selected" in actions.selection_count().text
    
    page.click_delete_label()
    for name in label_to_delete:
        assert page.wait_until_label_deleted(name)


def test_delete_all_labels(page, actions):
    page.select_all_labels()
    assert "items selected" in actions.selection_count().text

    page.click_delete_label()
    assert page.is_table_empty