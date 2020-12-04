import requests
from bs4 import BeautifulSoup

url='http://www.biquge.info/67_67794/'
response=requests.get(url)
html=response.text.encode('latin-1').decode('utf-8')
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup.find_all(name='dd'))
# print(soup.dd.contents)

# for i, child in enumerate(soup.dl.contents):
#     print(i, child.string)
#
# for dl in soup.find_all(name='dl'):
#     print(dd.find_all(name='dd'))
# #--------------------------------------------
# for dl in soup.find_all(name='dl'):
#     # print(dl.find_all(name='dd'))
#     for dd in dl.find_all(name='dd'):
#         print(dd.string)
#--------------------------------------------
for dl in soup.find_all(name='dl'):
    print(dl.find_all(name='dd'))
    for dd in dl.find_all(name='dd'):
        print(dd.a)