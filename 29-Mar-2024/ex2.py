#Hidden Websites

import requests
from requests.auth import HTTPBasicAuth

basic = HTTPBasicAuth('user', 'pass')
response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)

# Check if the request was successful
if response.status_code == 200:
    print("Success! The response is:", response.text)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
