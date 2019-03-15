# 生成buzzfeed-test-parse-html-output.txt 

import re
import pprint
import json
import requests
import time
from urllib import request, parse
import ssl

# 使用 ssl 未经验证的上下文
context = ssl._create_unverified_context()

url = 'https://www.buzzfeed.com/dianaprince23/tell-us-what-you-eat-in-a-day-and-well-tell-you-w-9ho7d7dgbg'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}


# # 封装 request
req = request.Request(url, data=None, headers=headers, method='GET')

# # 进行请求
response = request.urlopen(req, context=context)

html = response.read().decode('utf-8')


# allresult = re.findall(r'"(\w+)":', json.dumps(out, indent=4))
# print(allresult)

pattern = re.compile('"subbuzz":(.*?),\s*?"sharing":', re.S)
result_txt = re.search(pattern, html).group(1)
out = json.loads(result_txt)
print(json.dumps(out, indent=4))


with open('buzzfeed-test-parse-html-output.txt', 'w', encoding='UTF-8') as f:
    f.write(json.dumps(out, indent=4))
    f.close()
