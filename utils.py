import requests
from requests.cookies import RequestsCookieJar
from bs4 import BeautifulSoup
import re
from csv import DictWriter


def get_price_and_product_title_from_big_c(product_code):
    url = 'https://www.bigc.co.th/en/search?q=' + product_code
    headers = {
        'Accept-Language': 'en-US,en;q=0.9'
    }
    jar = RequestsCookieJar()
    jar.set('language', 'en', domain="www.bigc.co.th", path="/")

    rawHTML = requests.get(url, headers, cookies=jar)

    soup = BeautifulSoup(rawHTML.text, 'html.parser')

    title_element = soup.find("div", class_='productCard_title__f1ohZ')
    baht_element = soup.find('div', class_='productCard_price__9T3J8')

    # Extract the text (currency symbol in this case)
    price_text = baht_element.getText(strip=True)
    product_title = title_element.get_text()

    price_value = re.findall(r'\d+\.\d+', price_text)

    # Get the first match if available
    price_value = price_value[0] if price_value else None

    write_to_csv({"Title": product_title, "Value": price_value})

    return f"{product_title} : ฿{price_value}"


def write_to_csv(product):

    field_names = ["Title", "Value"]

    with open('event.csv', 'a') as f_object:

        dictwriter_object = DictWriter(f_object, fieldnames=field_names)

        dictwriter_object.writerow(product)

        f_object.close()

    return
