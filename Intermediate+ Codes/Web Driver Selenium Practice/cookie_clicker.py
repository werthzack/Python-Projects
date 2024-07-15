from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

cookie_link = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(cookie_link)

cookie = driver.find_element(By.ID, "cookie")
store = driver.find_element(By.ID, "store")
money = driver.find_element(By.ID, "money")


def store_upgrade():
    store_items = store.find_elements(By.CSS_SELECTOR, "div")
    item_ids = [item.get_attribute("id") for item in store_items][::-1]
    for i, item in enumerate(store_items[::-1]):
        try:
            item_data = item.find_element(By.CSS_SELECTOR, "b").text.split()
        except:
            print("error caught")
            continue
        if len(item_data) < 1:
            continue

        item_price = int(item_data[-1].replace(",", ""))
        cookie_amount = int(money.text)
        if cookie_amount > item_price:
            try:
                item.click()
            except StaleElementReferenceException:
                item = store.find_element(By.ID, item_ids[i])
                item.click()


def main():
    cookie_amount = 0
    abort_time = time.time() + 300
    shop_time = time.time() + 5
    while time.time() < abort_time:
        try:
            cookie.click()
            cookie_amount = money.text
            if time.time() > shop_time:
                shop_time = time.time() + 5
                store_upgrade()
            time.sleep(0.01)
        except NoSuchWindowException:
            print(f"Window has been closed. Final Score: {cookie_amount}")
            driver.quit()
            break
        except KeyboardInterrupt:
            print(f"Program has been terminated. Final Score: {cookie_amount}")
            break

    print(f"Time has elapsed")


main()
