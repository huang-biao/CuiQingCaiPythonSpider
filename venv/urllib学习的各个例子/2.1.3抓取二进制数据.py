# import requests
#
# r = requests.get("https://github.com/favicon.ico")
# print(r.text)
# print(r.content)
import requests

r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)