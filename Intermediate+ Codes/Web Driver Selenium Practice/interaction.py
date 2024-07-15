from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
signup_url = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(signup_url)

# article_no = driver.find_element(By.CSS_SELECTOR, '#articlecount [title="Special:Statistics"]')
# article_no.click()
#
# search_bar = driver.find_element(By.NAME, "search")
# search_button = driver.find_element(By.XPATH, '//*[@id="p-search"]/a')
# search_button.click()
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

fname_field = driver.find_element(By.NAME, "fName")
lname_field = driver.find_element(By.NAME, "lName")
mail_field = driver.find_element(By.NAME, "email")

fname_field.send_keys(input("What's the first name? "))
lname_field.send_keys(input("What's the last name? "))
mail_field.send_keys(input("What's the email? "))

submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()
