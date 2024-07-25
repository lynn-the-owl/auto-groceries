import requests
from bs4 import BeautifulSoup
import re


def getPriceFromBigC(product_code):
    url = 'https://www.bigc.co.th/search?q=' + product_code
    rawHTML = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(rawHTML.text, 'html.parser')

    # Find the element with the class 'productCard_baht__cMDbh'
    baht_element = soup.find('div', class_='productCard_price__9T3J8')

    # Extract the text (currency symbol in this case)
    price_text = baht_element.getText(strip=True)

    price_value = re.findall(r'\d+\.\d+', price_text)

    # Get the first match if available
    price_value = price_value[0] if price_value else None

    return f"฿{price_value}"
