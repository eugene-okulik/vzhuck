from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_1_send_text(driver):
    test_data = 'cat'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(test_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == test_data
    print(test_data)


def test_2_submit_form(driver):
    name = 'Bob'
    last_name = 'Marley'
    email = 'bob@gh.com'
    phone = '1234567890'
    subject = 'subject'
    address = '12 Privet Drive'
    driver.get('https://demoqa.com/automation-practice-form')
    text_name = driver.find_element(By.ID, 'firstName')
    text_name.send_keys(name)
    text_lastname = driver.find_element(By.ID, 'lastName')
    text_lastname.send_keys(last_name)
    text_email = driver.find_element(By.ID, 'userEmail')
    text_email.send_keys(email)
    text_email = driver.find_element(By.ID, 'userNumber')
    text_email.send_keys(phone)
    text_subject = driver.find_element(By.ID, 'subjectsInput')
    text_subject.send_keys(subject)
    text_address = driver.find_element(By.ID, 'currentAddress')
    text_address.send_keys(address)
    dropdown_state = driver.find_element(By.CLASS_NAME, 'css-19bqh2r')
    dropdown_state.click()
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Haryana']"))
    )
    option.click()
    dropdown_city = driver.find_element(
        By.CLASS_NAME, 'css-tlfecz-indicatorContainer'
    )
    dropdown_city.click()
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Karnal']"))
    )
    option.click()
    radio_button = driver.find_element(By.CLASS_NAME, 'custom-control-label')
    radio_button.click()
    birth_month = driver.find_element(By.ID, 'dateOfBirthInput')
    birth_month.click()
    select = driver.find_element(
        By.CLASS_NAME, 'react-datepicker__month-select'
    )
    dropdown = Select(select)
    dropdown.select_by_visible_text('February')
    select = driver.find_element(
        By.CLASS_NAME, 'react-datepicker__year-select'
    )
    dropdown = Select(select)
    dropdown.select_by_visible_text('1990')
    date_element = driver.find_element(
        By.XPATH, "//div[@aria-label='Choose Tuesday, February 20th, 1990']"
    )
    date_element.click()
    button = driver.find_element(By.ID, 'submit')
    button.click()
    table = driver.find_element(By.CSS_SELECTOR, "table.table")
    headers = table.find_elements(By.CSS_SELECTOR, "thead th")
    header_text = [header.text for header in headers]
    print(" | ".join(header_text))
    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_text = [cell.text for cell in cells]
        print(" | ".join(cell_text))


def test_3_choose_language(driver):
    test_data = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element(By.NAME, 'choose_language')
    dropdown = Select(select)
    dropdown.select_by_visible_text(test_data)
    button = driver.find_element(By.NAME, 'submit')
    button.click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == test_data


def test_4_check_hello_world(driver):
    text = 'Hello World!'
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="start"]/button'))
    )
    button.click()
    message = driver.find_element(By.ID, 'finish')
    assert message.text == text
