# encoding:utf-8
import re

if __name__ == '__main__':
    m = re.search('(?=abc)abcdef', 'abcdef')  #前瞻断言
    m = re.search('(?<=abc)def', 'abcdef')  # 首先 断言需要匹配
    m = re.search('(?!\d{4})cdef', 'abcdef')  # 负面前瞻断言，如果不匹配，则从后面开始匹配

    m = re.search('^(/wiki/)((?!:).)*q$', '/wiki/abcdeq')
    if m!=None:
        print(m.group(0))