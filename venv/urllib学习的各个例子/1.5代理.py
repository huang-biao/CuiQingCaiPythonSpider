'''
[Errno 61] Connection refused 这个代码失败了
'''
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)