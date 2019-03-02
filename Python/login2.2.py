import requests

user = ' '  #账号
passwd = ' ' #密码

###以下内容无需修改###
url = 'http://10.3.8.217/login'
data={'user': user,
      'pass': passwd,
      'line': 'CUC-BRAS'} #联通线路

requests.post(url, data)
