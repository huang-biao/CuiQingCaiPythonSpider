from urllib import parse,request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://httpbin.org/post'
headers = \
    {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host':'huangbiaozhuji.org'
    }
dict = {'name':'HuangBiao'}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')