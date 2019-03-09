# buzzfeed
'''
{
    "data":
    {
        "content":
        {
            "questions":
            [
                {
                    "answers":
                        [
                            {
                                "pid": "answer-1551854837408-5997",
                                "resultId": "result-1551854816125-3035",
                                "text": "Chipotle"
                            },
                            {
                                "pid": "answer-1551854837408-8612",
                                "resultId": "result-1551854723649-5570",
                                "text": "McDonald\u0027s"
                            },
                            {
                                "pid": "answer-1551854837408-6453",
                                "resultId": "result-1551854777148-5808", "text": "In-N-Out"
                            },
                            {
                                "pid": "answer-1551854837408-3147",
                                "resultId": "result-1551854795051-6594",
                                "text": "Sweet Tomatoes"
                            }
                        ],
                    "color": "blue",
                    "pid": "question-1551854723650-2919",
                    "title": "Pick your favorite restaurant!"
                },

                ...

            ], 


            "results": 
                [
                    { 
                        "description": "You live your life free of kids, without being tied down anywhere!", 
                        "image": "", 
                        "pid": "result-1551854723649-5570", 
                        "title": "Zero" 
                    },

                    ...

                ]
        }, 
        "meta": 
        { 
            "images": [], 
            "timestamp": 1552062676 
        }
    },
    "formatName": "instant_quiz",
    "renderKitUrl": "https://www.buzzfeed.com/static-assets/buzz-format-platform/instant_quiz/js/render_kit.0765b01c97c88904d43e.js",
    "id": "122423272"
}

'''

from urllib import request, parse
import ssl

#使用 ssl 未经验证的上下文
context = ssl._create_unverified_context()

#定义请求 url 和 header
url = 'https://www.buzzfeed.com/jstelnik/pick-your-favorite-foods-and-we-will-say-how-many-e00glkiquu'
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

def write_to_file(item):
    with open('buzzfeed.txt', 'a', encoding='UTF-8') as f:
        f.write(item)
        f.close()
        
#把请求的参数转化为 byte
data = bytes(parse.urlencode(dict), 'utf-8')

#封装 request
req = request.Request(url, data=None, headers=headers, method='GET')

#进行请求
response = request.urlopen(req, context=context)

#打印结果，登录成功：{"rsm":{"url":"https:\/\/biihu.cc\/home\/first_login-TRUE"},"errno":1,"err":null}
# print(response.read().decode('utf-8'))
write_to_file(response.read().decode('utf-8'))

