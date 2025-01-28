import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_add_item_in_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')
    first_tab = driver.current_window_handle
    top_left_item = driver.find_element(
        By.XPATH, "(//img[@class='card-img-top img-fluid'])[1]"
        )
    ActionChains(driver).key_down(Keys.CONTROL) \
        .click(top_left_item) \
        .key_up(Keys.CONTROL) \
        .perform()
    driver.switch_to.window(driver.window_handles[-1])
    add_to_cart_button = driver.find_element(
        By.XPATH, "//a[text()='Add to cart']"
        )
    add_to_cart_button.click()
    WebDriverWait(driver, 10).until(
            EC.alert_is_present()
        )
    alert = driver.switch_to.alert
    print("Product added", alert.text)
    alert.accept()
    driver.close()
    driver.switch_to.window(first_tab)
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    cart_item = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, "//td[text()='Samsung galaxy s6']"
            ))
    )
    assert cart_item.text == 'Samsung galaxy s6', "ITEM NOT FOUND"


def test_add_bag_to_compare(driver):
    driver.implicitly_wait(3)
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    bag = driver.find_element(By.XPATH, "//div[@class='product-item-info'][1]")
    add_to_compare = driver.find_element(
        By.XPATH, "//a[@class='action tocompare' and @title='Add to Compare']"
        )
    actions = ActionChains(driver)
    actions.move_to_element(bag)
    actions.move_to_element(add_to_compare)
    actions.click(add_to_compare)
    actions.perform()
    driver.execute_script("window.scrollBy(0, 300);")
    check_bag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'product-item-name'))
    )
    assert check_bag.text == 'Push It Messenger Bag', "ITEM NOT FOUND"
