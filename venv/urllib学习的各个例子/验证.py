from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

'''
这里首先实例化 HTTPBasicAuthHandler 对象，其参数是 HTTPPasswordMgrWithDefaultRealm 对象，它利用 add_password() 添加进去用户名和密码，这样就建立了一个处理验证的 Handler。

接下来，利用这个 Handler 并使用 build_opener() 方法构建一个 Opener，这个 Opener 在发送请求时就相当于已经验证成功了。

接下来，利用 Opener 的 open() 方法打开链接，就可以完成验证了。这里获取到的结果就是验证后的页面源码内容。
'''
username = '*******'//自己的校园账号，统一认证码
password = '*********'//对应的校园账号的密码
url = 'http://ids.cqupt.edu.cn/authserver/login?service=http%3A%2F%2Fjwc.cqupt.edu.cn%2Ftysfrz%2Findex.php'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
