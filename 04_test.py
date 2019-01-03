#### 1.将名称映射到序列的元素
#    我们可以通过collections.namedtuple()方法返回一个python标准元组类型的子类。
#    可以给他提供一个类型名称和相应的字段,它可以返回一个实例化的类,为你已经定义好的字段传入值

from collections import namedtuple
Subscriber = namedtuple("Subscriber",['addr','joined'])

sub = Subscriber("lxb_savior@163.com","2019-01-03")
print(sub)
print("sub's addr is %s"%sub.addr)
print("sub's joined is %s"%sub.joined)
print(len(sub))

#### 分解
addr , joined = sub
print(addr)
print(joined)

def compute_cost(records):
    total = 0
    for rec in records:
        # print("rec=",rec)
        total += rec[1] * rec[2]
    return total


tu = (("Bob",1,2),("Tony",2,3))
toal = compute_cost(tu)
print(toal)

# 如果要在固定位置之前插入一列属性元祖的话,那么此段代码就会报错
# tu = (("Bob","m",1,2),("Tony","m",2,3))

from collections import namedtuple
# 此处要添加一列数据的时候,可以在namedtuple中新添加一列字段,然后实例访问的时候把该字段通过实例传入,从而保证了代码的可用性
stock = namedtuple("Stock",["name","shares","price"])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = stock(*rec)
        total += s.shares * s.price
    return total

tum = (("Bob",1,2),("Tony",2,3))
print(compute_cost(tum))

# namedtuple是可以用来替代字典的,并且当字典中的数据比较大的时候,namedtuple是占用内存比较小的,会比较高效
# 但是namedtuple类似于实例化一个对象以后,对象的某些属性是不会改变的,因此要使用对象的_replace方法

s=stock("ACME",100,123.5)
print(s)

# 错误赋值
# s.shares = 75
# print(s)

# 正确赋值
s = s._replace(shares=75)
print(s)



from  collections import namedtuple

Stock = namedtuple('Stock',['name','shares','price','date','time'])

# create a prototype instance
stock_prototype = Stock("",0,0.0,None,None)

# function to convert a dictionary to a stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {"name":"ACME","shares":100,"price":123.45}
print(dict_to_stock(a))

b = {"name":"ACME","shares":100,"price":123.45,"date":'12/17/2012'}
print(dict_to_stock(b))
print(dict_to_stock(b).date)

# 另外如果定义的目标是一个高效的数据结构,而且会修改各种实例属性,那么使用namedtuple并不是最佳的属性,相反可以定义一个__slots__属性的类