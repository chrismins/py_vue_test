import requests
import base_url

# print(base_url.url)
url = base_url.url
r = requests.get(url=url)
print(r.status_code)
