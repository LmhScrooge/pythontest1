# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    url = 'http://www.whatismyip.com.tw/'
    #proxy = {'http':'180.173.52.202:53281'}
    #创建proxyhandler
    #proxy_support = request.ProxyHandler(proxy)
    #创建open
    #opener = request.build_opener(proxy_support)
    #添加user agent
    #opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装open
    #request.install_opener(opener)
    req = request.urlopen(url)
    html = req.read().decode('utf-8')
    print(html)