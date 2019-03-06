# coding:utf-8

# 1.以固定化列数重新格式化文本
s="Look into my eyes,look into my eyes,the eyes,the eyes,  \
  the eyes, not around the eyes, don't look around the eyes,  \
  look into my eyes, you're under."

import textwrap
print(textwrap.fill(s,70))



# 2.在文本中处理HTML和XML实体
s = "Elements are written as '<tag>text<tag>'"


# 3.文本分词
text = 'foo = 23 +42 +10'

tokens = [{'NAME','foo'},{'EQ','='},{'NUM','123'},{'PLUS','+'},{'NUM','42'},{'TIMES','*'},{'NUM':10}]


import re
NAME = r'(?P<NAME>[a-zA-z_][a-zA-z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat= re.compile("|".join([NAME,NUM,PLUS,TIMES,EQ,WS]))
master_plist= "|".join([NAME,NUM,PLUS,TIMES,EQ,WS])
print("master_plist=%s"%master_plist)

#
scanner = master_pat.scanner("foo=42")
print(scanner.match())

# 将这项技术转化为代码,轻松将其包含在一个生成器函数中
from collections import namedtuple
Token = namedtuple('Token',['type','value'])
def generate_tokens(pat,text):
    scanner = pat.scanner(text)
    for m  in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())


for tok in generate_tokens(master_pat,'foo = 42'):
    print(tok)
    print(tok.value)