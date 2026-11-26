import pytest
from pages.users_page import UsersPage


@pytest.fixture
def page(driver, url):
    page = UsersPage(driver)
    page.open(url)
    page.login("user", "pass")
    page.go_to_users()
    return page


def test_create_user(actions, page):
    assert actions.page_title().text == "Users"

    email, first_name, last_name = page.open_create_user_form()
    assert email.is_displayed()
    assert first_name.is_displayed()
    assert last_name.is_displayed()
    assert actions.page_title().text == "Create User"    

    page.create_user("mj23@mail.ru", "Michael", "Jordan")
    assert actions.page_title().text == "User mj23@mail.ru"
    page.go_to_users()
    assert page.is_user_displayed("mj23@mail.ru", "Michael", "Jordan")


def test_users_list(page):
    is_visible, rows_count, emails, first_names, last_names = page.get_table_state()
    assert is_visible
    assert rows_count == len(emails) == len(first_names) == len(last_names) > 0
    assert all(cell.text.strip() != "" for cell in emails)
    assert all(cell.text.strip() != "" for cell in first_names)
    assert all(cell.text.strip() != "" for cell in last_names)


def test_edit_user_valid(page, actions):
    email, first_name, last_name = page.select_user_to_edit()
    assert actions.page_title().text == "User john@google.com"
    assert email.is_displayed()
    assert first_name.is_displayed()
    assert last_name.is_displayed()
    assert page.save_button().is_displayed()
    assert not page.save_button().is_enabled()

    page.fill_user_fields(email="mj23@mail.ru", first_name="Michael", last_name="Jordan")
    assert actions.page_title().text == "Users"
    assert not page.is_user_displayed("john@google.com", "John", "Doe")
    assert page.is_user_displayed("mj23@mail.ru", "Michael", "Jordan")


def test_edit_user_invalid_email(page, actions):
    page.select_user_to_edit()
    page.fill_user_fields(email="mj23mail.ru", first_name="Michael", last_name="Jordan")
    assert "The form is not valid. Please check for errors" in actions.alert().text


def test_edit_user_invalid_first_name(page, actions):
    page.select_user_to_edit()
    page.fill_user_fields(email="mj23@mail.ru", last_name="Jordan")
    assert "The form is not valid. Please check for errors" in actions.alert().text


def test_edit_user_invalid_last_name(page, actions):
    page.select_user_to_edit()
    page.fill_user_fields(email="mj23@mail.ru", first_name="Michael")
    assert "The form is not valid. Please check for errors" in actions.alert().text


def test_delete_one_user(page, actions):
    users_to_delete = [("john@google.com", "John", "Doe")]

    for email, first_name, last_name in users_to_delete:
        page.select_user(email, first_name, last_name)
    assert "1 item selected" in actions.selection_count().text
    
    page.click_delete_user()
    for email, first_name, last_name in users_to_delete:
        assert page.wait_until_user_deleted(email, first_name, last_name)


def test_delete_multiple_users(page, actions):
    users_to_delete = [
        ("john@google.com", "John", "Doe"),
        ("jane@gmail.com", "Jane", "Smith"),
        ("peter@outlook.com", "Peter", "Brown"),
    ]

    for email, first_name, last_name in users_to_delete:
        page.select_user(email, first_name, last_name)
    assert "3 items selected" in actions.selection_count().text
    
    page.click_delete_user()
    for email, first_name, last_name in users_to_delete:
        assert page.wait_until_user_deleted(email, first_name, last_name)


def test_delete_all_users(page, actions):
    page.select_all_users()
    assert "items selected" in actions.selection_count().text

    page.click_delete_user()
    assert page.is_table_empty