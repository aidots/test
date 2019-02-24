import chardet

data = '离离原上草，一岁一枯荣'.encode('gbk')

data2 = '最新の主要ニュース'.encode('euc-jp')

print(chardet.detect(b'Hello, world!'))

print(chardet.detect(data))

print(chardet.detect(data2))

