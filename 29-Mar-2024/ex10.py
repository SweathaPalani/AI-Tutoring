#lxml

#pip install requests lxml

import requests
from lxml import html

# The URL we want to scrape
url = 'https:///realpython.github.io/fake-jobs/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with lxml
tree = html.fromstring(response.content)

# Use XPath to extract the job titles
job_titles = tree.xpath('//h2[@class="title is-5"]/text()')

# Print each job title
for title in job_titles:
    print(title)

