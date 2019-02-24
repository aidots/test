'''
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
'''

'''
https://zhuanlan.zhihu.com/p/55487119

模拟登陆「逼乎」: https://biihu.cc/

'''
from urllib import request, parse
import ssl

#使用 ssl 未经验证的上下文
context = ssl._create_unverified_context()

#定义请求 url 和 header
url = 'https://biihu.cc//account/ajax/login_process/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

#定义请求参数
dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'fkandshit',
    'password':'123456',
    '_post_type':'ajax',
}

#把请求的参数转化为 byte
data = bytes(parse.urlencode(dict), 'utf-8')

#封装 request
req = request.Request(url, data=data, headers=headers, method='POST')

#进行请求
response = request.urlopen(req, context=context)

#打印结果，登录成功：{"rsm":{"url":"https:\/\/biihu.cc\/home\/first_login-TRUE"},"errno":1,"err":null}
print(response.read().decode('utf-8'))