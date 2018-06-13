# encoding:utf-8

from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getHtml(url):
    # 异常处理
    try:
        return urlopen(url)
    except HTTPError as e:
        print(e)
        return None

if __name__ == '__main__':
    html = getHtml('http://www.pythonscraping.com/pages/warandpeace.html')
    if html==None:
        print('error')
    else:
        soup = BeautifulSoup(html.read(),'html.parser')
        p = soup.findAll('p', limit=3)
        print(len(p))   #<class 'bs4.element.ResultSet'>

    # html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    # bsObj = BeautifulSoup(html)
    # images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
    # for image in images:
    #     print(image["src"])


def tests():
    print()