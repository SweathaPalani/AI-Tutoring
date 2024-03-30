#Generating CSV from data

import requests
from bs4 import BeautifulSoup
import csv

# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

all_products = []

# Assuming products are selected correctly with 'div.thumbnail'
products = soup.select('div.thumbnail')
for product in products:
    # Extracting product information
    name = product.select_one('h4 > a').text.strip()
    price = product.select_one('.price').text.strip()
    reviews = product.select_one('.ratings > p.pull-right').text.strip()
    rating = len(product.select('.ratings .glyphicon-star'))

    product_info = {
        'name': name,
        'price': price,
        'reviews': reviews,
        'rating': rating,
    }
    all_products.append(product_info)

# Check if we have any products scraped before proceeding
if all_products:
    keys = all_products[0].keys()
    with open('products.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_products)
else:
    print('No products found.')
