from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

amazon_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
python_url = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(python_url)

# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_decimal = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_whole.text}.{price_decimal.text}")

# event_list = driver.find_element(By.CSS_SELECTOR, ".event-widget ul")
# event_items = event_list.find_elements(By.TAG_NAME, "li")
# event_data = {i: {'time': event.find_element(By.TAG_NAME, "time").text,
#                   'name': event.find_element(By.TAG_NAME, "a").text}
#               for i, event in enumerate(event_items)}
#
# print(event_data)

driver.quit()
