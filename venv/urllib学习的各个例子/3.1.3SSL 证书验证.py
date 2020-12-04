import requests

response = requests.get('https://www.12306.cn')
print(response.status_code)