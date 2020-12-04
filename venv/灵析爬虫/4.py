import requests
import bs4          # 爬网站必备两个模块不解释
import os           # 用来创建文件夹的
import sys          # 没啥用单纯为了好看
import time
import random       # 使用随机数设置延时
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    "Cookie": "_abcde_qweasd=0; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1583122664; bdshare_firstime=1583122664212; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1583145548",
    "Host": "www.xbiquge.la"}      # 设置头尽量多一点 以防万一
b_n = ""
def get_title_url():
    x = str(input("输入书名或作者名:"))
    data = {'searchkey': x}
    url = 'http://www.xbiquge.la/modules/article/waps.php'
    global headers, b_n
    r = requests.post(url, data=data, headers=headers)
    soup = bs4.BeautifulSoup(r.text.encode('ISO-8859-1'), "html.parser")
    book_author = soup.find_all("td", class_="even")
    books = []          #　 书名
    authors = []        #  作者名
    directory = []      #  目录链接
    tem = 1
    for each in book_author:
        if tem == 1:
            books.append(each.text)
            tem -= 1
            directory.append(each.a.get("href"))
        else:
            authors.append(each.text)
            tem += 1
    print('搜索结果：')
    for num,book, author in zip(range(1, len(books)+1),books, authors):
        print((str(num)+": ").ljust(4)+(book+"\t").ljust(25) + ("\t作者：" + author).ljust(20))
    search = dict(zip(books, directory))
    if books == []:
        print("没有找到任何一本书，请重新输入!")
        get_title_url()
    try:
        i = int(input("输入需要下载的序列号(重新搜索输入'0')"))
    except:
        print("输入错误重新输入:")
        i = int(input("输入需要下载的序列号(重新搜索输入'0')"))
    if i == 0:
        books = []
        authors = []
        directory = []
        get_title_url()
    if i>len(books) or i<0:
        print("输入错误重新输入:")
        i = int(input("输入需要下载的序列号(重新搜索输入'0')"))
    b_n=books[i-1]
    try:
        os.mkdir(books[i-1])
        os.chdir(b_n)
    except:
        os.chdir(b_n)
        b_n = books[i - 1]
    return search[books[i-1]]

def get_text_url(titel_url):
    url = titel_url
    global headers
    r = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.text.encode('ISO-8859-1'), "html.parser")
    titles = soup.find_all("dd")
    texts = []
    names = []
    texts_names = []
    for each in titles:
        texts.append("http://www.xbiquge.la"+each.a["href"])
        names.append(each.a.text)
    texts_names.append(texts)
    texts_names.append(names)
    return texts_names          #  注意这里的返回值是一个包含两个列表的列表！！


def readnovel(texts_url):
    global headers,b_n
    count=1
    max=len(texts_url[1])
    print("预计耗时{}分钟".format((max // 60)+1))
    tishi = input(str(b_n)+"一共{}章，确认下载输入'y',输入其他键取消".format(max))
    if tishi == "y"or tishi =="Y":
        for n in range(max):
            url = texts_url[0][n]
            name = texts_url[1][n]
            req = requests.get(url=url,headers=headers)
            time.sleep(random.uniform(0, 0.5))          # 即使设置了延迟，他还有会可能503（没办法小网站）
            req.encoding = 'UTF-8'                      # 这里的编码是UTF-8，跟目录不一样，要注意！
            html = req.text
            soup = bs4.BeautifulSoup(html, features="html.parser")
            texts = soup.find_all("div", id="content")
            while (len(texts) == 0):                    #   他如果503的话，读取内容就什么都木有，那直接让他再读一次，直到读出来为止。
                req = requests.get(url=url, headers=headers)
                time.sleep(random.uniform(0,0.5))
                req.encoding = 'UTF-8'
                html = req.text
                soup = bs4.BeautifulSoup(html, features="html.parser")
                texts = soup.find_all("div", id="content")
            else:
                content = texts[0].text.replace('\xa0' * 8, '\n\n')
                content=content.replace("亲,点击进去,给个好评呗,分数越高更新越快,据说给新笔趣阁打满分的最后都找到了漂亮的老婆哦!手机站全新改版升级地址：http://m.xbiquge.la，数据和书签与电脑站同步，无广告清新阅读！","\n")
                # 使用text属性，提取文本内容，滤除br标签，随后使用replace方法，去掉八个空格符号，并用回车代替 再去除每一页都有得结尾
            with open(name+'.txt',"w",encoding='utf-8')as f:
                f.write(content)
                sys.stdout.write("\r已下载{}章，还剩下{}章".format(count,max-count))     # sys模块就在这用了一次，为了不让他换行。。。
                count += 1
        print("\n全部下载完毕")
    else:
        print("已取消!")
        os.chdir('..')
        os.rmdir(b_n)
        main()

def main():
    titel_url = get_title_url()
    texts_url = get_text_url(titel_url)
    readnovel(texts_url)
    input("输入任意键退出")


if __name__ == '__main__':
    print("小说资源全部来自于'新笔趣阁'---》http://www.xbiquge.la\n所以搜不到我也没办法..........@晓轩\n为了确保下载完整，每章设置了0.5秒到1秒延时！")
    main()