import pytest
from selenium import webdriver
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
    driver.get('https://demoqa.com/automation-practice-form')
    driver.execute_script("window.scrollBy(0, 300);")
    form_data = {
        "firstName": "Bob",
        "lastName": "Marley",
        "userEmail": "bob@gh.com",
        "userNumber": "1234567890",
        "subjectsInput": "subject info",
        "currentAddress": "12 Privet Drive"
    }
    for field_id, value in form_data.items():
        driver.find_element(By.ID, field_id).send_keys(value)
    driver.execute_script("window.scrollBy(0, 300);")
    driver.find_element(By.CLASS_NAME, 'css-19bqh2r').click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Haryana']"))
    ).click()
    driver.find_element(
        By.CLASS_NAME, 'css-tlfecz-indicatorContainer'
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Karnal']"))
    ).click()
    driver.find_element(By.CLASS_NAME, 'custom-control-label').click()
    driver.find_element(By.ID, 'dateOfBirthInput').click()
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
    driver.find_element(By.CLASS_NAME, 'css-19bqh2r').click()
    driver.execute_script("window.scrollBy(0, 300);")
    button = driver.find_element(By.ID, 'submit')
    button.click()
    table = driver.find_element(By.CSS_SELECTOR, "table.table")
    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
    headers = table.find_elements(By.CSS_SELECTOR, "thead th")
    header_text = [header.text for header in headers]
    print(" | ".join(header_text))

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_text = [cell.text for cell in cells]
        print(" | ".join(cell_text))

    expected_table_data = {
        "Student Name": f"{form_data['firstName']} {form_data['lastName']}",
        "Student Email": form_data['userEmail'],
        "Gender": "Male",
        "Mobile": form_data['userNumber'],
        "Date of Birth": "20 February,1990",
        "Subjects": form_data['subjectsInput'],
        "Hobbies": "",
        "Picture": "",
        "Address": form_data['currentAddress'],
        "State and City": "Haryana Karnal"
    }
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        label = cells[0].text
        value = cells[1].text
        expected_value = expected_table_data[label]
        assert value == expected_value, (
            f"Error: Expected Values: '{expected_value}', "
            f"Actual: '{value}' in Label: '{label}'"
        )


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
