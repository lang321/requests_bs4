# coding:utf-8
import requests
# 类BeautifulSoup
from bs4 import BeautifulSoup


def getHTMLText(url):
    # 通用代码框架
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()  # 如果状态不是200，跑出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__ == '__main__':
    # html = getHTMLText("http://tieba.baidu.com/f/index/forumclass")

    # print(html)
    soup = BeautifulSoup(open('index.html', 'rb'), "html.parser")
    # print(soup.prettify())
    print(soup.body.contents)
    print(len(soup.body.contents))   #body字标签

    # find
    print(soup.findAll('a'))