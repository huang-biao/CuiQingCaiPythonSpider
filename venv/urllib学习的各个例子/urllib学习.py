# import urllib
# request = urllib.Resquest('http:www.baidu.com')
# response = urllib.urlopen(request)
# print(response.read())
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data,timeout=1)
print(response.read().decode('utf-8'))