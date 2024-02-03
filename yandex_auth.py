import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def wait_element(browser, delay_seconds=1, by=By.CLASS_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(expected_conditions.presence_of_element_located((by, value)))


def yandex_auth(login, password):
    path = ChromeDriverManager().install()
    browser_service = Service(executable_path=path)
    browser = Chrome(service=browser_service)
    browser.get('https://passport.yandex.ru/auth/')
    tag = browser.find_element(By.CLASS_NAME, 'Textinput-Control')
    tag.click()
    tag.send_keys(login)
    tag = browser.find_element(By.ID, 'passp:sign-in')
    tag.click()
    try:
        tag = wait_element(browser, 3, By.ID, 'passp-field-passwd')
    except:
        return "Wrong login"
    tag.click()
    tag.send_keys(password)
    tag = wait_element(browser, 3, By.ID, 'passp:sign-in')
    tag.click()
    try:
        tag = wait_element(browser, 5, By.ID, 'field:input-passwd:hint')
    except:
        wait_element(browser, 5, By.CLASS_NAME, 'PageTemplate_content__VT2in')
    if browser.current_url == "https://passport.yandex.ru/auth/welcome":
        return browser.current_url
    elif browser.current_url == "https://id.yandex.ru/":
        return browser.current_url
