# coding:utf-8

# 1.对齐文本字符串
text = 'Hello World'
# ljust
ljust_str = text.ljust(20)
print("ljust_str = %s"%ljust_str)

# rjust
rjust_str = text.rjust(20)
print("rjust_str = %s"%rjust_str)

# center
center_str = text.center(20)
print("center_str = %s"%center_str)

# 这些方法均接收一个可选的字符来填充
r_str = text.rjust(20,"=")
print("r_str = %s"%r_str)

l_str = text.ljust(20,"*")
print("l_str = %s"%l_str)

# format函数也可以用来轻松完成对齐的任务,需要做的就是合理利用'<','>',或者'^'字符以及一个期望的宽度值
format1 = format('test','>20')
print("format1=%s"%format1)

format2 = format('test','<20')
print("format2=%s"%format2)

format3 = format('test','^20')
print("format3=%s"%format3)

# 也包含空格之外的填充字符
format4 = format('test','=>20s')
print("format4=%s"%format4)

format5 = format('test','*^20s')
print("format5=%s"%format5)


# format并不是特定于字符串的,能做用于任何值,使它更加通用
x = 1.2345
format6 = format(x,'>10')
print("format6=%s"%format6)

format7 = format(x,'^10.2f')
print("format7=%s"%format7)


# 当格式化多个值时,这些格式化代码也可以用format()方法
form_str = "{:>10s} {:>10s}".format('hello','world')
print("form_str=%s"%form_str)

# format函数要比%和rjust()此类方法更加通用


# 2.字符串的连接及合并
parts = ['IS','Chicago','Not','Chicago?']
print(' '.join(parts))

# 字符串的少量拼接
a  = "Is Chicago"
b = 'Not Chicago?'
# 1
print("{} {}".format(a,b))
# 2
print(a+" "+b)
# 3
c = 'hello' 'world'
print(c)

# 3.采用生成器表达式，将数据转换为字符串的同时完成连接操作
data = ['ACME',50,91.1]
final_data = ','.join(str(d) for d in data)
print("final_data=%s"%final_data)

# better print
a = "hello"
b = "python"
c = "world"
# print(a,b,c,sep=":")


# 我们编写的代码要从很多短字符串中构建输出则应该考虑编写生成器函数
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?!!!'

text = ''.join(sample())
print("text=%s"%text)

# with open('demo.txt','wb') as f:
#     for part in sample():
#         f.write(part)


# 4.以混合的方式将I/O操作智能化地结合在一起
def combine(source,maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0

    yield  ''.join(parts)

with open('demo.txt','wb') as f:
    for part in combine(sample(),32768):
        f.write(part)


# 5.给字符串种的变量名做插值处理
# 5.1
s = '{name} has {n} message'
format_str = s.format(name='guido',n=37)
print("format_str=%s"%format_str)


# 5.2
name = 'Guido'
n=37
# code version:python3
format_str2 = s.format_map(vars())
print(format_str2)



# 5.3
class Info:
    def __init__(self):
        self.name = name
        self.n = n

class safesub(dict):
    def __missing__(self, key):
        return '{'+ key +'}'

# # code version:python3
# a = Info('Guido',37)
# # format_str3 = s.format_map(vars(a))
# # print(format_str3)
# del n
# format_str3 = s.format_map(safesub(vars()))
# print(format_str3)


# code version:python3
import sys
def sub(text):
    # f_locals存储的是程序本身的局部变量,可以实现局部变量的拷贝,但是对于局部变量拷贝后的修改和覆盖是不能实现的
    return text.format_map(safesub(sys._getframe(1).f_locals))
name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('you have {n} messages'))
print(sub('Your favorite color is {color}'))



name = 'Guido'
n = 37
s = '%(name) has %(n) messages'%vars()
print("s=%s"%s)


#5.4
import string
s = string.Template('$name has $n messages.')
fina = s.substitute(vars())
print("fina=%s"%fina)
