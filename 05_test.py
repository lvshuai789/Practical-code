#### 1.将多个映射合并成单个映射
from collections import ChainMap

values = ChainMap()
values["x"] = 1

values = values.new_child()
values["x"] = 2

values = values.new_child()
values["x"] = 3

print("values=%s"%values)

values1 = values["x"]
print("first values=%s"%values1)

#discard last mapping
values = values.parents
print("values.parents1=%s"%values["x"])

# discard last mapping
values = values.parents
print("values parents2=%s"%values["x"])


#### 和chainmap作用相同的有字典的update方法
a = {"x":1,"z":3}
b = {"y":2,"z":4}
merged = dict(b)
merged.update(a)
print(merged["z"])

#### 但是如果a b两个字典中的任意一个字典做了修改,merged中的字典可能都不会改变
a["x"] =12
print(merged["x"])

#### 但是如果用chainmap方法的话就没有这个问题

a = {"x":1,"z":3}
b = {"y":2,"z":4}
merged = ChainMap(a,b)
print("merged['x']=%s"%merged["x"])
a["x"] = 42
print("end merged['x']=%s"%merged["x"])



# 2.字符串操作(split,startswith,endswith,)
import re
line = 'asdf fjdk; afed, fjek,asdf,   foo'

fields = re.split(r'(;|,|\s)\s*',line)
print(fields)
values = fields[::2]
print("values = %s"%values)

delimiters = fields[1::2] + ['']



uni = list(zip(values,delimiters))
print("uni = %s"%uni)
old_str = ''.join(v+d for v,d in zip(values,delimiters))
print("old_str = %s"%old_str)

import re
result_list = re.split(r'(?:,|;|\s)\s*',line)
print("result_list = %s"%result_list)





#### 在字符串的开头或者结尾处做文本匹配
filename = "spam.txt"
result = filename.endswith(".txt")
print("finally result = %s"%result)

url = "http://www.python.org"
url_result = url.startswith('http:')
print("url_result =%s"%url_result)



import os
filenames = os.listdir('.')
print("filename = %s"%filenames)


# 判断当前的目录下方是否含py文件
if any(name.endswith('.py') for name in filenames):
    print("has py file!!!!")



from urllib.request import urlopen

def read_data(name):
    print("name=%s"%name)
    if name.startswith(('http:','https','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


result_data = read_data('http://www.baidu.com')
print("result_data = %s"%result_data)


chioces = ['http:','ftp:']
url = 'http://www.python.org'
result3 = url.startswith(tuple(chioces))
print("result3=")


#### 利用shell通配符做字符串的匹配(类似于在linux下方的正则通配符匹配操作)<fnmatch fnmatchcase>
from fnmatch import fnmatch,fnmatchcase
names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
up_list = [ name for name in names if fnmatch(name,'Dat*.csv')]
print("up_list =%s "%up_list)


result = fnmatchcase('foo.txt','*.TXT')
print("result = %s"%result)


# 处理街道名字的信息
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

ST_list = [addr for addr in addresses if fnmatchcase(addr,'* ST')]
print('ST_list = %s'%ST_list)


#### 3.文本模式的匹配和查找
text = 'yeah, but no,but yeah,but no,but yeah'
text1 = '11/27/2017'
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

#### 正则匹配预编译
#### 如果是对统一种模式来进行多次匹配,通常会将正则表达式模式预编译成一个模式对象
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print("yes")
else:
    print("no")


tt = 'Today is 11/27/2012. PyCon starts 3/13/2013'
final_list = datepat.findall(tt)
print("final_list = %s"%final_list)



#### 引入捕获组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2017')
print(m.groups())

for month,day,year in datepat.findall(tt):
    print("{}-{}-{}".format(year,month,day))

month,day,year = m.groups()


#### 采用迭代的方法找出所有的匹配项
for m in datepat.finditer(tt):
    print(m.groups())

#### 以上操作采用先将模式编译,然后再重复使用

#### 4.查找和替换文本
# str.replace()
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah','yep'))


####sub()方法
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', tt))

#### month_addr方法可以将数字转化为英语单词
#### 对于复杂的情况还可以指定一个替换回调函数
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

print(datepat.sub(change_date,tt))

#### subn()方法还可以得到一共完成了多少次替换
newtext,n = datepat.subn(r'\3-\1-\2',tt)
print(newtext)
print(n)