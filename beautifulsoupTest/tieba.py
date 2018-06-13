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
        r = requests.get(url, timeout=30)
        # r = requests.request('get',url)
        r.raise_for_status()  # 如果状态不是200，跑出异常
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(str(e))
        return '产生异常'


if __name__ == '__main__':
    html = getHTMLText("https://tieba.baidu.com/")
    soup = BeautifulSoup(html, "html.parser")
    ul = soup.find('ul', id='new_list')
    new_list = ul.findAll('li',{'class':'clearfix j_feed_li '})
    news = []
    for item in new_list:
        title = item.select('a.title')
        click_num = item.select('span[class="list-post-num"] em')
        news_title = ""
        news_click_num = 0
        if len(title)>0:
            news_title = title[0].get_text()
        if len(click_num)>0:
            news_click_num = click_num[0].get_text()
        news.append((news_title, news_click_num))
    for new in news:
        print(new)



