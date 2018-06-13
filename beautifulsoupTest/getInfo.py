# coding:utf-8
import requests
# 类BeautifulSoup
from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    # 通用代码框架
    pro = { "http": "http://127.0.0.1:80", "https": "127.0.0.1:80"}
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    }
    try:
        # r = requests.get(url, timeout=30)
        r = requests.request('get',url, proxies = pro)
        r.raise_for_status()  # 如果状态不是200，跑出异常
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(str(e))
        return '产生异常'


if __name__ == '__main__':
    html = getHTMLText("http://www.baidu.com")

    soup = BeautifulSoup(html, "html.parser")
    # soup = BeautifulSoup(open('index.html','rb'), "html.parser")
    # print(soup.prettify())
    # print(soup.body.contents)
    # print(len(soup.body.contents))   #body字标签

    # findAll(True)
    # for a in soup.findAll(re.compile('^i'), {'name':'ie'}):  # 匹配以b开头的
    #     print(a)
    for a in soup.findAll('a',{'class':re.compile('^mn')}):  # 匹配以b开头的
        print(a)
    # for a in soup.find_all(string = re.compile("百度")):  # 匹配以b开头的
    #     print(a)