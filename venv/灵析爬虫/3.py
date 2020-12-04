import requests
import re
from bs4 import BeautifulSoup

url='http://www.biquge.info/67_67794/12456785.html'
response=requests.get(url)
html=response.text.encode('latin-1').decode('utf-8')
# print(html)
soup = BeautifulSoup(html, 'html.parser')

content=str(soup.find_all(id='content'))
print(type(content))

# print(content)vvv
pattern = '<br/>'  # 选出所有以<br/>为结尾的
content1 = re.sub('<br/>', '',content)
content2 = re.sub('<div id="content"><!--go-->','',content1)
content3 = re.sub('</div>','',content2)
print(content1)
print(content2)
print(content3)
with open('小说.txt','w') as f:
    f.write(content1)


# for div in soup.find_all('div'):
#     print(div.find_all(name='dd'))
# for dl in soup.select('dl'):
#     print(dl.select('dd'))