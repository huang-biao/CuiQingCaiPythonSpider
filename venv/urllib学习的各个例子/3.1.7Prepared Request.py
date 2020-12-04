'''
前面介绍 urllib 时，我们可以将请求表示为数据结构，其中各个参数都可以通过一个
Request 对象来表示。这在 requests 里同样可以做到，这个数据结构就叫
Prepared Request。我们用实例看一下：
这里我们引入了 Request，然后用 url、data 和 headers 参数构造了一个
Request 对象，这时需要再调用 Session 的 prepare_request() 方法将其转换为一个
Prepared Request 对象，然后调用 send() 方法发送即可
'''
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)