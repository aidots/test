'''
https://domain-registry.appspot.com/check?domain=xxx.dev

返回check.json文件：{"status":"success","available":false,"reason":"In use"}
'''
import re
import json
import requests

def list_from_file(f):

    return f.read().splitlines(False)


def main():
    f = open('getdotdev_search.txt','r')
    domain_list = list_from_file(f)
    # 清空搜索结果文件
    f=open('getdotdev_result.txt','w')
    f.truncate()
    for domain in domain_list:
        output_string = domain+': '
        result_item = json_from_check(domain)
        if(result_item['available']):
            output_string += '可以注册'
            write_available_to_file(output_string)
        else:
            output_string += '不能注册'
            write_NA_to_file(output_string)

        write_item_to_file(output_string)
        

#获得结果的dict
def json_from_check(domain_string):
    url = 'https://domain-registry.appspot.com/check?domain='+domain_string+'.dev'
    html = request_dev(url)
    dict = json.loads(s=html)
    #print(dict)

    return dict

def request_dev(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def write_item_to_file(item):
    #print('开始写入数据 ====> ' + str(item))
    with open('getdotdev_result.txt', 'a', encoding='UTF-8') as f:
        # f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.write(item+'\n')
        f.close()

'''
把可以注册的写在文件里
'''
def write_available_to_file(item):
    with open('getdotdev_available.txt', 'a', encoding='UTF-8') as f:
        ff = open('getdotdev_available.txt','r')
        existed_available_list = list_from_file(ff)
        if(existed_available_list.count(item)==0):
            f.write(item+'\n')
        f.close()
'''
把不可以注册的写在文件里
'''
def write_NA_to_file(item):
    with open('getdotdev_na.txt', 'a', encoding='UTF-8') as f:
        ff = open('getdotdev_na.txt','r')
        existed_available_list = list_from_file(ff)
        if(existed_available_list.count(item)==0):
            f.write(item+'\n')
        f.close()

if __name__ == "__main__":
    main()
