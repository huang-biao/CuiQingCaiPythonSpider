import requests

data = {'name': 'germey', 'age': '22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
'''
我们成功获得了返回结果，其中 form 部分就是提交的数据，这就证明 POST 请求成功发送了。
'''