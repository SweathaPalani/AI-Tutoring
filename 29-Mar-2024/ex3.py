#Navigating the DOM with BeautifulSoup

from bs4 import BeautifulSoup
import requests

# Sample URL
url = "http://example.com"

# Send a GET request to the URL
response = requests.get(url)

# If the response was successful, parse the HTML
if response.status_code == 200:
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find an element by ID
    element_by_id = soup.find(id="some-id")

    # Find elements by HTML tag
    elements_by_tag = soup.find_all('a')

    # Find elements with a specific class
    elements_by_class = soup.find_all(class_="some-class")

    # Accessing attributes of a tag
    for link in elements_by_tag:
        href = link.get('href')
        text = link.text
        print(f"Link Text: {text}, URL: {href}")

else:
    print("Failed to retrieve the web page")
