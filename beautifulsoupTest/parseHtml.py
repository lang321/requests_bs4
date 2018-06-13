# coding:utf-8
import requests
# 类BeautifulSoup
from bs4 import BeautifulSoup

def getHTMLText(url):
    # 通用代码框架
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status() # 如果状态不是200，跑出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == '__main__':
    # html = getHTMLText("http://tieba.baidu.com/f/index/forumclass")

    # print(html)
    soup = BeautifulSoup(open('index.html','rb'), "html.parser")
    # print(soup.prettify())
    print(soup.title) #<title>...</title>
    print(soup.a)
    print(soup.a.name)
    print(soup.a.parent.name)
    # print(soup.a.parent.parent.parent.parent.parent.name)
    print(soup.a.attrs)
    print(soup.a.attrs['class'])
    print(soup.a.attrs['href'])
    print(soup.a.string)   # NavigableString
    print(soup.p.string)   # 跨越多个标签层次

    