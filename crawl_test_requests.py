'''

https://zhuanlan.zhihu.com/p/55620986

'''
import requests

#一行代码 Get 请求
r = requests.get('https://api.github.com/events')

#一行代码 Post 请求
r = requests.post('https://httpbin.org/post', data = {'key':'value'})

#其它乱七八糟的 Http 请求
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

#想要携带请求参数是吧？
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

#假装自己是浏览器
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

#获取服务器响应文本内容
r = requests.get('https://api.github.com/events')
print(r.text)
# u'[{"repository":{"open_issues":0,"url":"https://github.com/...
print(r.encoding)
# 'utf-8'


#获取字节响应内容
print(r.content)
# b'[{"repository":{"open_issues":0,"url":"https://github.com/...

#获取响应码
r = requests.get('https://httpbin.org/get')
print(r.status_code)
# 200


#获取响应头
print(r.headers)
'''
{    
    'content-encoding': 'gzip',    
    'transfer-encoding': 'chunked',  
    'connection': 'close',    
    'server': 'nginx/1.0.4',    
    'x-runtime': '148ms',    
    'etag': '"e1ca502697e5c9317743dc078f67693f"',   
    'content-type': 'application/json'
}
'''

#获取 Json 响应内容
r = requests.get('https://api.github.com/events')
print(r.json())
# [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

#获取 socket 流响应内容
r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)
# <urllib3.response.HTTPResponse object at 0x101194810>

r.raw.read(10)
# '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'

#Post请求 当你想要一个键里面添加多个值的时候
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)
# {  ...  "form": {    "key1": [      "value1",      "value2"    ]  },  ...}
print(r1.text == r2.text)
#True

#请求的时候用 json 作为参数
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)

#想上传文件？
url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
print(r.text)
# {  ...  "files": {    "file": "<censored...binary...data>"  },  ...}

#获取 cookie 信息
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies['example_cookie_name'])
# 'example_cookie_value'

#发送 cookie 信息
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
# '{"cookies": {"cookies_are": "working"}}'


#设置超时
requests.get('https://github.com/', timeout=0.001)