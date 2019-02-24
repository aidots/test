import re
import requests

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html_content = request_url(url)
    items = parse_content(html_content)

    for item in items:
        #write_to_file(item)
        print(item)

def request_url(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
    except requests.RequestException:
        return None

def parse_content(html_content):
    pattern = re.compile('<li>.*?<div\sclass="list_num\s(?:|red)">.*?</div>.*?<div\sclass="pic">.*?title="(.*?)".*?</li>', re.S)
    items = re.findall(pattern, html_content)
    for item in items:
        yield {
            '作者': item
        }

if __name__ == "__main__":
    main(1)