# coding:utf-8

import telnetlib

if __name__ == '__main__':
    try:
        telnetlib.Telnet('127.0.0.1', port='80', timeout=20)
    except:
        print('connect failed')
    else:
        print('success')

    import requests

    try:
        requests.get('https://www.baidu.com/', proxies={'http':"http://127.0.0.1:80","https":"http://127.0.0.1:80"})
    except:
        print('connect failed')
    else:
        print('success')
