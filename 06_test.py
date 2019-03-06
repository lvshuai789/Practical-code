# coding:utf-8
# 1.以不区分大小写的方式对文本做查找和替换
# 主要的方式有re.I和re.IGNORECASE
import re
text = "UPPER PYTHON,lower python,Mixed Python"
result = re.findall('python',text,flags=re.IGNORECASE)
# result = re.findall('python',text,re.I)
print("findall result=%s"%result)


def matchcase(word):
    def repalce(m):
        text = m.group()
        print("text=%s"%text)
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return repalce


result = re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
print("re.sub result=%s"%result)

# 2.实现定义最短匹配的正则表达式
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
find_result = str_pat.findall(text1)
print("find_result=%s"%find_result)

# *操作符在正则表达式中采用的是贪心策略
text2 = 'Computer says "no." Phone says "yes."'
find_result2 =  str_pat.findall(text2)
print("find_result2=%s"%find_result2)

# 防止贪婪策略匹配符号?
str_pat = re.compile(r'\"(.*?)\"')
find_result3 = str_pat.findall(text2)
print("find_result3=%s"%find_result3)


# 3.编写多行模式的正则表达式
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment */ '''
result1 = comment.findall(text1)
result2 = comment.findall(text2)
print("result1=%s"%result1)
print("result2=%s"%result2)

# (?:.|\n)指定一个非捕获组(只做匹配但是不捕获结果,也不会分配组号)
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
result3 = comment.findall(text2)
print("result3=%s"%result3)


# re.compile()
# 可以接收一个有用的标记re.DOTAll使得正则表达式中的句点(.)可以匹配所有的子符,也包括换行符号
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
result4 = comment.findall(text2)
print("result4=%s"%result4)


## 2.9将unicode文本统一表示为规范形式
# 用正则表达式处理unicode字符
num = re.compile('\d+')
# acsii digits
result = num.match('123')
print("match ascii digits=%s"%result.group())

# arabic digits
result2 = num.match('\u0661\u0662\u0663')
print("match arabic digits=%s"%result2.group())


# 从字符串中去掉不需要的字符

