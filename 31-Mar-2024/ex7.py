import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://ocs.ca/collections/dried-flower?product=8868588454196&sort_by=products_price_per_uom_asc"

# Sending a request to the URL
response = requests.get(url)

# Parsing the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting the price of the product
# Note: Replace 'price_class_name' with the actual class name of the price element in the HTML
price_element = soup.find('span', class_="product-tile__price__main js-price-shown")

if price_element:
    price = price_element.get_text().strip()
    print("Price:", price)
else:
    print("Price element not found")
