# buzzfeed


'''
思路：
输入url，类似：https://www.buzzfeed.com/dianaprince23/tell-us-what-you-eat-in-a-day-and-well-tell-you-w-9ho7d7dgbg
匹配搜索到的第一个 <title></title>之间的，作为标题

quiz封面图片不在这个页面，需要手动处理

匹配 "subbuzz": 的那一段，进行处理：
取题目图片： "image": "https://img.buzzfeed.com/buzzfeed-static/static/2019-03/10/16/enhanced/buzzfeed-prod-web-05/original-23766-1552251326-3.png",

取答案：
文本："header": "Air",
图片："image": "https://img.buzzfeed.com/buzzfeed-static/static/2019-03/10/16/enhanced/buzzfeed-prod-web-01/enhanced-buzz-27293-1552248633-0.jpg",
对应结果索引："personality_index": 1,

取结果：
图片："results" -> "image": "https://img.buzzfeed.com/buzzfeed-static/static/2019-03/10/16/enhanced/buzzfeed-prod-web-04/enhanced-21316-1552251278-3.jpg",
标题："results" -> "header": "The Fighter",
描述："results" -> "description": "When you set your mind to something, you will not rest until it's done. You're ambitious, highly motivated, and impossible to knock down. Challenges are exciting to you, not something to back away from. You love a good, spirited debate\u2014 and you love being right, too. Sure, your impatience and occasional stubbornness might frustrate those around you sometimes, but they appreciate the fact that you always get things done. Your strong will and tireless energy will take you far in life. Just don't forget to take a little time to breathe, too.",

输出到新建的一个对象里面，格式为
"id": 1,
"image": "",#quiz的图片
"value": "",
"ques_ans": []:{
                "question": "",
                "type": "",
                "answer": []:{ "img": "", "txt": "", "res": 0 },
},
"result": []:{
        "content": "",
        "type": "",
        "res_img": "",
        "description": ""
}

弄完后，用正则表达式去掉双引号。然后把对象存为一个文本文件里面。（能自动对齐格式最好，不能也没事，可以在外部搞）

'''

import re
from urllib import request, parse
import ssl
import requests
from urllib.request import urlretrieve

# 使用 ssl 未经验证的上下文
context = ssl._create_unverified_context()

# 定义请求 url 和 header
url = 'https://www.buzzfeed.com/dianaprince23/tell-us-what-you-eat-in-a-day-and-well-tell-you-w-9ho7d7dgbg'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
}


def parse_result(html):
    # pattern = re.compile('"subbuzz":.*?"image":"(.*?)",.*?"sharing":',re.S)
    pattern = re.compile('"subbuzz":.*?"sharing":', re.S)
    first = re.search(pattern, html).group()
    print(first)

    pattern2 = re.compile('.*?"image":"(.+?png)",.*?', re.S)
    second = re.findall(pattern2, first)
    # print(second)
    # print(len(second))
    return second

#    items = re.findall(pattern,html)
#    for item in items:
#        yield {
#            'range': item[0],
#            'image': item[1],
#            'title': item[2],
#            'recommend': item[3],
#            'author': item[4],
#            'times': item[5],
#            'price': item[6]
#        }


def write_to_file(item):
    with open('buzzfeed.txt', 'a', encoding='UTF-8') as f:
        f.write(item)
        f.close()


# # 封装 request
# req = request.Request(url, data=None, headers=headers, method='GET')

# # 进行请求
# response = request.urlopen(req, context=context)

# images = parse_result(response.read().decode('utf-8'))

# print(images)

# 下载给定url的图片到本地
# image_url = 'https://img.buzzfeed.com/buzzfeed-static/static/2019-03/8/12/enhanced/buzzfeed-prod-web-04/enhanced-25395-1552067600-1.png'
# pattern = re.compile('//.*?/.*?/.*?/.*?/.*?/.*?/.*?/.*?/(.*?).png', re.S)
# image_name = re.findall(pattern, image_url)[0]
# print(image_name)


def download_image(base_dir, image_url):
    print('basedir is :'+base_dir+' image_url is :'+image_url)
    pattern = re.compile('//.*?/.*?/.*?/.*?/.*?/.*?/.*?/.*?/(.*?).png', re.S)
    image_name = re.findall(pattern, image_url)[0]
    print(image_name)
    # 获取图片的名称, image_url = http://i.meizitu.net/2017/04/24b01.jpg 这种格式
    file_name = base_dir+image_name+".png"
    print('file_name is :'+file_name)
    urlretrieve(image_url, file_name)

    # r = requests.get(image_url, stream=True)    
    # with open(file_name, 'wb') as f:
    #     for chunk in r.iter_content(chunk_size=32):
    #         f.write(chunk)

    

# for img in images:
    # print("img:"+img)
download_image('./Users/billowfay/Downloads/buzz/','https://img.buzzfeed.com/buzzfeed-static/static/2019-03/8/12/enhanced/buzzfeed-prod-web-03/enhanced-12078-1552067601-1.png')
    # write_to_file()
