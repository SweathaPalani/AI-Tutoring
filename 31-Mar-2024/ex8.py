import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://ocs.ca/collections/dried-flower?product=8868588454196&sort_by=products_price_per_uom_asc"

# Sending a request to the URL
response = requests.get(url)


# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# # Find all elements with the specified class
# prices = soup.find_all(class_="product-tile__price__main js-price-shown")

# # Print all found prices
# for price in prices:
#     print(price.get_text().strip())

# Find all elements with the specified classes for products and prices
products = soup.find_all(class_="product-tile__title h4")
prices = soup.find_all(class_="product-tile__price__main js-price-shown")

# Extract and print product names and prices
for product, price in zip(products, prices):
    product_name = product.get_text().strip()
    product_price = price.get_text().strip()
    print(f"Product: {product_name}, Price: {product_price}")
