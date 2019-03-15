# test https://www.buzzfeed.com/quizzes/personality
# 从这个页面抓取quiz的标题、封面图地址、链接
# 首页顶部1题，下面29题 
# 第二页： https://www.buzzfeed.com/quizzes/personality?page=2
# 第二页没有顶部题，有30题

import os
import re
import pprint
import json
import requests
import time
import ssl
from urllib import request, parse

# [{title: "", image: "", url: ""}]
quiz_list = []

quizzes_url = "https://www.buzzfeed.com/quizzes/personality"

# 使用 ssl 未经验证的上下文
context = ssl._create_unverified_context()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
}
req = request.Request(quizzes_url, data=None, headers=headers, method='GET')
response = request.urlopen(req, context=context)

data = response.read().decode('utf-8')

# with open('buzzfeed.2.py-output.txt', 'r') as myfile:
#   data = myfile.read()

# print(data)

# 注意这里的图是jpg，后缀要注意

result_0_1 = re.findall(r'<div class="wire-frame__img featured-image xs-relative card__image--big" style="background-image:url\((.*)\?output-format=auto&output-quality=100', data)
result_0_2 = re.findall(r'<h1 class="featured-card__headline link-gray">(.*?)</h1>',data)
result_0_3 = re.findall(r'<a href="(.+?)" data-bfa="@a:post;@d:0;@o:',data)
quiz_list.append({"title": result_0_2[0], "image": result_0_1[0], "url": result_0_3[0]})

result_1_29_titles = re.findall(r'dimension4:(.+?)};@e:',data)
result_1_29_urls = re.findall(r'<a href="(.+?)" data-bfa.+?dimension4:',data)
result_1_9_images = re.findall(r'style="background-image:url\(\'(.+?)\?output-format=auto',data)
result_10_29_images = re.findall(r'data-background-src="(.+?)" data-quality',data)


for i in range(len(result_1_9_images)):
    quiz_list.append({"title": result_1_29_titles[i], "image": result_1_9_images[i], "url": result_1_29_urls[i]})


for ii in range(len(result_1_9_images),len(result_1_29_titles)):
    quiz_list.append({"title": result_1_29_titles[ii], "image": result_10_29_images[ii-len(result_1_9_images)], "url": result_1_29_urls[ii]})


# for item in quiz_list:
#     print(json.dumps(item, indent=4))

for item in quiz_list:
    print(json.dumps(item, indent=4))
    with open('buzzfeed.2.py-output2.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, indent=4))
        f.close()

# result = re.findall(r'<a href="(.+?)" data-bfa.+?dimension4:(.+?)};@e:.+?background-image:url\(\'(.+?)\?output-format=auto',data)
# print(result[0])
# with open('buzzfeed.2.py-output.txt', 'w', encoding='UTF-8') as f:
#     f.write(html)
#     f.close()


# allresult = re.findall(r'"(\w+)":', json.dumps(out, indent=4))
# print(allresult)
# pattern = re.compile(r'', re.S)
# result_txt = re.search(pattern, html).group(1)






# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(out)

# print(out)

# 把  out 替换双引号  "xxx":   ->   xxx:
# 在vscode里 用  "(\w+)":   ->   $1:
# py里面 用 "(\w+)":   ->   \1:


# allresult = re.findall(r'"(\w+)":', json.dumps(out, indent=4))
# print(allresult)

# allresult2 = re.sub(r'"(\w+)":', r'\1:', json.dumps(out, indent=4))
# print(allresult2)

# with open('buzzfeed.1.py-output.txt', 'w', encoding='UTF-8') as f:
#     f.write(re.sub(r'"(\w+)":', r'\1:', json.dumps(out, indent=4)))
#     f.close()
