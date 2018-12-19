# coding: utf-8
import requests

url = 'http://ngw.bupt.edu.cn/login'

def login():
    # replace following ***
    # permanent address http://10.3.8.217/
    postdata = {'user': '***',#account
                'pass': '***',#password
                'line': 'CUC-BRAS'}
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Content-Length': '44',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': '***',#cookie
               'Host': 'ngw.bupt.edu.cn',
               'Origin': 'http://ngw.bupt.edu.cn',
               'Referer': 'http://ngw.bupt.edu.cn/index',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    requests.post(url, data=postdata)

login()
