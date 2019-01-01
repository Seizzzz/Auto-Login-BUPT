import requests

user = ' '  #账号
passwd = ' ' #密码

###以下内容无需修改###
url = 'http://10.3.8.217/login'
data={'user': user,
      'pass': passwd,
      'line': 'CUC-BRAS'} #联通线路

def getcookie():
    session = requests.session()
    result = session.post(url,data=data)
    cookies = requests.utils.dict_from_cookiejar(session.cookies)
    return str(cookies)[15:31]

def login():
    postdata = data
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               #'Content-Length': '44',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': 'SessionId=%s' %getcookie(),
               'Host': '10.3.8.217',
               'Origin': 'http://10.3.8.217',
               'Referer': 'http://10.3.8.217/index',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    requests.post(url, data=postdata)

login()
