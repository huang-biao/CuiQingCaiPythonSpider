"""Ajax:微博前十页面爬取"""
import time
from urllib.parse import urlencode
from pyquery import PyQuery as Pq
import requests
from pymongo import MongoClient

# 基本URL，代表前半部分
base_url = 'https://m.weibo.cn/api/container/getIndex?'
# 构造请求头，page是可变参数
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_page(page):
    """页面请求函数"""
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page,
    }
    # 使用urlencode()方法将参数转化为URL的GET请求参数，类似a='1'&b='2'&c='3'形式，然后拼接到一起
    url = base_url + urlencode(params)
    print(url)
    # 提供异常捕捉,并发送请求，判断响应是否成功(status_code==200)?
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error:', e.args)


def parse_page(json):
    """页面解析函数"""
    if json:
        items = json.get('data').get('cards')
        # 分析json格式发现，偶数元素才包含mblog，所以判断mblog是否存在
        # 再执行下面的操作
        for item in items:
            item = item.get('mblog')
            if item == None:
                pass
            else:
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = Pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reports'] = item.get('reposts_count')
                yield weibo


# 数据库操作初始化
client = MongoClient(host='localhost', port=27017)
db = client['weibo']
collection = db['weibo']


def save_to_mgdb(result):
    """信息写入到Mongo数据库"""
    if collection.insert(result):
        print('Saved to Mongo')


if __name__ == '__main__':
    for page in range(0, 5):
        json = get_page(page)
        time.sleep(1)
        results = parse_page(json)
        for result in results:
            save_to_mgdb(result)








