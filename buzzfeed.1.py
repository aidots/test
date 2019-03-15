#

import os
import re
import pprint
import json
import requests
import time
import ssl
from urllib import request, parse

'''
下载图片到本地，并重命名
url = "https://img.buzzfeed.com/buzzfeed-static/static/2019-03/10/16/enhanced/buzzfeed-prod-web-05/original-23766-1552251326-3.png"
base = "/Users/billowfay/Documents/PythonProjects/test/"
new = "1.png"
TODO 转换成jpg格式
注意basepath最后要带斜杠，newname要带后缀
'''
def download_image(imgurl, basepath, newname):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    response = requests.get(imgurl, headers=headers, stream=True)

    if not os.path.exists(basepath):
        os.makedirs(basepath)

    with open(basepath + newname, 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


'''
从网页源码爬出quiz对象的字符串，生成quiz对象
'''
def generate_quiz_object(quizurl):
    # 使用 ssl 未经验证的上下文
    context = ssl._create_unverified_context()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    req = request.Request(quizurl, data=None, headers=headers, method='GET')
    response = request.urlopen(req, context=context)
    html = response.read().decode('utf-8')
    # allresult = re.findall(r'"(\w+)":', json.dumps(out, indent=4))
    # print(allresult)
    pattern = re.compile(r'"subbuzz":(.*?),\s*?"sharing":', re.S)

    if(re.search(pattern, html)==None):
        return None

    result_txt = re.search(pattern, html).group(1)

    return json.loads(result_txt)


# [{title: "", image: "", url: ""}]
def getQuizList(quizzes_url):
    quiz_list = []

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

    return quiz_list


quizzesurl = "https://www.buzzfeed.com/quizzes/personality"

q_list = getQuizList(quizzesurl)

for i, q in enumerate(q_list):
    quiz_url = q["url"]

    quiz = generate_quiz_object(quiz_url)

    if(quiz == None):
        print("这个不符合格式："+str(i+11))
        continue
    # "id": 1,
    # "image": "",
    # "value": "",
    # "ques_ans": []:{
    #                 "question": "",
    #                 "type": "",
    #                 "answer": []:{ "img": "", "txt": "", "res": 0 },
    #             },
    # "result": []:{
    #         "content": "",
    #         "type": "",
    #         "res_img": "",
    #         "description": ""
    #     }

    out = {}
    out["id"] = i+11
    out["image"] = q["image"]
    out["value"] = q["title"]

    out["ques_ans"] = [
        {
            "question": val["image"],
            "type":"image",
            "answers":
            [
                {"img": v["image"], "txt": v["header"],
                    "res": v["personality_index"]}
                for v in val["answers"]
            ]
        }
        for val in quiz["questions"]
    ]

    out["result"] = [
        {"content": vv["header"], "type":"image",
            "res_img":vv["image"], "description":vv["description"]}
        for vv in quiz["results"]
    ]

    localbasepath = "/Users/billowfay/Documents/PythonProjects/test/buzz/" + \
        str(out["id"])+"/"

    # 下载封面图片
    download_image(out["image"], localbasepath, "front_img"+str(out["id"])+".jpg")

    # 下载questions&answers的图片
    for i, v in enumerate(out["ques_ans"]):
        download_image(v["question"], localbasepath,
                    str(out["id"])+"-q-"+str(i+1)+".png")
        time.sleep(2)

        for ii, vv in enumerate(v["answers"]):
            download_image(vv["img"], localbasepath, str(
                out["id"])+"-"+str(i+1)+"-"+str(ii+1)+".png")
            time.sleep(2)

    # 下载result图片
    for iii, vvv in enumerate(out["result"]):
        download_image(vvv["res_img"], localbasepath,
                    "result_pic_"+str(out["id"])+"_"+str(iii+1)+".png")
        time.sleep(2)


    # 重命名questions&answers的图片名称
    for i, v in enumerate(out["ques_ans"]):
        v["question"] = str(out["id"])+"-q-"+str(i+1)+".jpg"
        for ii, vv in enumerate(v["answers"]):
            vv["img"] = str(out["id"])+"-"+str(i+1)+"-"+str(ii+1)+".jpg"

    # 重命名result的图片名称
    for iiii, vvvv in enumerate(out["result"]):
        vvvv["res_img"] = "result_pic_"+str(out["id"])+"_"+str(iiii+1)+".jpg"






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

    with open('buzzfeed.'+str(out["id"])+'.py-output.txt', 'w', encoding='UTF-8') as f:
        f.write(re.sub(r'"(\w+)":', r'\1:', json.dumps(out, indent=4)))
        f.close()

    time.sleep(5)
