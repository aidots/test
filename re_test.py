'''
https://zhuanlan.zhihu.com/p/55916454
'''
import re

content = 'Xiaoshuaib has 100 bananas'
res = re.match('^Xi.*(\d+)\s.*s$',content)
print(res.group(1))

'''
import re

content = """Xiaoshuaib has 100 
bananas"""
res = re.match('^Xi.*?(\d+)\s.*s$',content,re.S)
print(res.group(1))
'''

'''
import re

content = """Xiaoshuaib has 100 
bananas"""
res = re.search('Xi.*?(\d+)\s.*s',content,re.S)
print(res.group(1))
'''

'''
import re

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
res = re.findall('Xi.*?(\d+)\s.*?s;',content,re.S)
print(res)
# ['100', '100', '100', '100']
'''

'''
import re

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
content = re.sub('\d+','250',content)
print(content)

#Xiaoshuaib has 250 bananas;
#Xiaoshuaib has 250 bananas;
#Xiaoshuaib has 250 bananas;
#Xiaoshuaib has 250 bananas;
'''

'''
import re

content = "Xiaoshuaib has 100 bananas"
pattern = re.compile('Xi.*?(\d+)\s.*s',re.S)
res = re.match(pattern,content)

print(res.group(1))
#其实和我们之前写的一样的
#res = re.match('^Xi.*?(\d+)\s.*s$',content,re.S)
#只不过 compile 一下 便于以后复用
'''

