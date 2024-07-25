from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (this example uses Chrome)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.tops.co.th/en/search/8850144226574")

# Wait for the results to load
time.sleep(3) 

# Click on the first link in the search results
first_result = driver.find_element(By.CLASS_NAME, 'product-item-inner-wrap')
first_result.click()
print("clicked")

getSeleniumUrl = driver.current_url

driver.quit


import requests

productCode = "8850144226574"

url = getSeleniumUrl
print(url)

rawHTML = requests.get(url)

file = open("response.html", "w")
file.write(rawHTML.text)
file.close
