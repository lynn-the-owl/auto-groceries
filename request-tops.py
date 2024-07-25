from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

product_id = "8850144226574"


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(options=chrome_options)

# Open the website
driver.get("https://www.tops.co.th/en/search/" + product_id)

# Wait for the results to load
time.sleep(0.5) 

# Click on the first link in the search results
first_result = driver.find_element(By.CLASS_NAME, 'product-item-inner-wrap')
first_result.click()
print("clicked")

getSeleniumUrl = driver.current_url

driver.quit


import requests

url = getSeleniumUrl
print(url)

rawHTML = requests.get(url).text


from bs4 import BeautifulSoup

soup = BeautifulSoup(rawHTML, 'html.parser')

pulledData = soup.find('script', id='meta-schema').get_text()
print(pulledData)

import json
from types import SimpleNamespace

x = json.loads(pulledData, object_hook=lambda d: SimpleNamespace(**d))
productName = x.name
productPrice = x.offers.price

print(productName)
print(productPrice)

