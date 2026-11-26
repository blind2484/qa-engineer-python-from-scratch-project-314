from selenium.webdriver.common.by import By


def open_page(driver, base_url: str, page: str = "") -> None:
    driver.get(f"{base_url}{page}")


def login(driver, username="user", password="pass"):
    driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Sign in']").submit()


def build_user_xpath(email, first_name, last_name):
    return (
        "//tr["
        f".//td[contains(@class, 'column-email') and normalize-space()='{email}'] and "
        f".//td[contains(@class, 'column-firstName') and normalize-space()='{first_name}'] and "
        f".//td[contains(@class, 'column-lastName') and normalize-space()='{last_name}']"
        "]"
    )


def build_status_xpath(name, slug):
    return (
        "//tr["
        f".//td[contains(@class, 'column-name') and normalize-space()='{name}'] and "
        f".//td[contains(@class, 'column-slug') and normalize-space()='{slug}']"
        "]"
    )


def build_label_xpath(name):
    return (
        "//tr["
        f".//td[contains(@class, 'column-name') and normalize-space()='{name}']"
        "]"
    )