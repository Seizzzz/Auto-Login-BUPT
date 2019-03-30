import requests

user = ' '  #账号
passwd = ' ' #密码

###以下内容无需修改###
url0 = 'http://10.3.8.216/login'
url1 = 'http://10.3.8.217/index'
url2 = 'http://10.3.8.217/login'

data0 = {'user': user,
        'pass': passwd}
data1 = {'user': user,
        'pass': passwd,
        'line': 'CUC-BRAS'} #联通线路

requests.post(url0, data0)
requests.post(url1, data1)
requests.post(url2, data1)
