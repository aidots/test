import requests
'''
用法：
url = "https://img.buzzfeed.com/buzzfeed-static/static/2019-03/10/16/enhanced/buzzfeed-prod-web-05/original-23766-1552251326-3.png"
base = "/Users/billowfay/Documents/PythonProjects/test/"
new = "1.png"
注意basepath最后要带斜杠，newname要带后缀
'''
def download_image(imgurl,basepath,newname):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
    response = requests.get(imgurl, headers=headers, stream=True)

    with open(basepath+newname, 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

url = "https://img.buzzfeed.com/buzzfeed-static/static/2019-03/10/16/enhanced/buzzfeed-prod-web-05/original-23766-1552251326-3.png"
base = "/Users/billowfay/Documents/PythonProjects/test/"
new = "1.png"

download_image(url,base,new)
