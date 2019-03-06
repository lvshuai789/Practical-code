# coding:utf-8

# 1.从字符串中去掉不需要的字符
# 1.strip()方法可以用来从字符串的开始和结尾处除去不需要的字符
s = 'hello world\n'
final_result = s.strip()
print("final_result=%s"%final_result)

t = '-----hello====='
final_result2 = t.lstrip("-")
print("final_result2=%s"%final_result2)

final_result3 = t.strip("-=")
print("final_result3=%s"%final_result3)


# match函数采用命名函数获取匹配到的结果
# import re
# str = "123"
# res = re.match(r'(?P<number>\d+)',str)
# print(res.group("number"))

import re

# 方法一
# sub的第二个参数可以是函数的引用 也可以是函数的调用形式
# 如果是函数的引用,这里是相当于执行函数function(正则匹配到的对象),此函数不用写成装饰器的形式
def pythonReSubDemo():
    '''
    demo python re.sub
    :return:
    '''
    inputstr = "hello 123 world 456"

    def __add111(matched):
        intStr = matched.group("number")
        intValue = int(intStr)
        addedValue = intValue + 111
        addedValueStr = str(addedValue)
        return addedValueStr

    replacedStr = re.sub("(?P<number>\d+)",__add111,inputstr)
    print "replacedStr=",replacedStr


# 方法二
# sub的第二个参数可以是函数的引用 也可以是函数的调用形式
# 如果是调用函数,这里是相当于执行函数function(原来函数的参数)(正则匹配到的对象),此函数得写成装饰器的形式
input_str = "hello 123 world 456"
def pythonReSubDemo():

    def inner_function(m):
        text = m.group("number")
        intvalue = int(text)
        addedvalue = intvalue + 111
        addedvalueStr = str(addedvalue)
        return addedvalueStr
    return inner_function

final_result4 = re.sub("(?P<number>\d+)",pythonReSubDemo(),input_str,flags=re.IGNORECASE)
print("final_result4=%s"%final_result4)




# 2.文本的过滤和清理
s = 'python\fis\tawesome\r\n'
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None   # Deleted
}

a = s.translate(remap)
print("a=%s"%a)


# 3.适合python3把所有的Unicode组合字符都去掉
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)) )
b = unicodedata.normalize('NFD',a)


# 4.构建庞大的转换表,将unicode组合字符都去掉
digitmap = {c:ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c))=="Nd"}
print(len(digitmap))

x = '\u0661\u0662\u0663'
x.translate(digitmap)

# 5.用来清理文本的技术 转换Unicode编码的技术
a = "不正确编码的字符串"
b = unicodedata.normalize('NFD',a)
b = b.encode("ascii","ignore").decode("ascii")