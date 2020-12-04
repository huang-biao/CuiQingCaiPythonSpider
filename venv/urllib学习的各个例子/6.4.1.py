from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

# 表示请求的URL的前半部分
base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# 我们通过PyMongo库里的MongoClient，第一个参数host是mongobd的地址，第二个参数是端口port（默认27017）
client = MongoClient(host='localhost', port=27017)
# 选择数据库
db = client['weibo1']
# 选择好数据库后我们需要指定要操作的集合，与数据库的选择类似
collection = db['weibo1']
max_page = 10


def get_page(page):
    # 构造参数字典，其中type、value、containerid是固定参数，page是可变参数
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    # 调用urlopen（）方法将参数转化为URL的GET请求参数，base_url与参数拼合形成一个新的URL
    url = base_url + urlencode(params)
    try:
        # requests请求这个链接，加入headers参数
        response = requests.get(url, headers=headers)
        # 判断响应的状态码，如果是200，则直接调用json（）方法将内容解析为JSON返回，否则不返回任何信息
        if response.status_code == 200:
            return response.json(), page
    # 如果出现异常，则捕获并输出其异常信息
    except requests.ConnectionError as e:
        print('Error', e.args)


# 定义一个解析方法，用来从结果中提取想要的信息
def parse_page(json, page: int):
    if json:
        # 可以先遍历cards
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                # 然后获取mblog中的各个信息，赋值为一个新的字典返回即可
                item = item.get('mblog', {})
                weibo = {}
                weibo['id'] = item.get('id')  # 微博的ID
                weibo['text'] = pq(item.get('text')).text()  # 正文
                weibo['attitudes'] = item.get('attitudes_Count')  # 点赞数
                weibo['comments'] = item.get('comments_Count')  # 评论数
                weibo['reports'] = item.get('reports_Count')  # 转发数
                yield weibo


def save_to_mongo(result):
    if collection.insert(result):
        print('Save to Mongo')


if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)
            save_to_mongo(result)


