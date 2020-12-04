from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
# HTTPPasswordMgrWithDefaultRealm
from urllib.request import URLError
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
username='1660076'
password='19936081789'
url='https://ids.cqupt.edu.cn/authserver/login?service=http%3A%2F%2Fjwc.cqupt.edu.cn%2Ftysfrz%2Findex.php'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler=HTTPBasicAuthHandler(p)
opener=build_opener(auth_handler)
try:
    result=opener.open(url)
    html=result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)