#### 1.通过公共键对字典列表进行排序 (operator中的itemgetter类并且性能比较高)
rows = [
    {"fname":"Brain","lname":"Jones","uid":1003},
    {"fname":"David","lname":"Beazley","uid":1002}
        ]

from operator import itemgetter,attrgetter

rows_by_name = sorted(rows,key=itemgetter("fname"))
print(rows_by_name)

rows_by_id = sorted(rows,key=itemgetter("uid"))
print(rows_by_id)

rows_by_lname = sorted(rows,key=itemgetter("lname","fname"))
print(rows_by_lname)


mmin = min(rows,key=itemgetter("uid"))
print(mmin)

mmax = max(rows,key=itemgetter("uid"))
print(mmax)

#### 2.对不原生支持比较操作的对象排序

class User:
    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.user_name = user_name

    def __repr__(self):
        return  "User({}) and username({})".format(self.user_id,self.user_name)

# users = [User(1),User(10),User(100)]
# class_sort = sorted(users,key=lambda u:u.user_id)
# print(class_sort)
#
# users_2 = [User(1),User(10),User(100)]
# class_sort2 = sorted(users,key=attrgetter("user_id"))
# print(class_sort2)

users_3 = [User(1,"B"),User(2,"A"),User(3,"C")]
by_name = sorted(users_3,key=attrgetter("user_name"))
print(by_name)


#### 3.根据字段将记录分组
from operator import itemgetter
from itertools import groupby

rows = [
    {"address":"5412 N CLARK","date":"07/01/2012"},
    {"address":"5448 N CLARK","date":"07/04/2012"},
    {"address":"5800 E 58TH","date":"07/02/2012"},
    {"address":"2122 N CLARK","date":"07/03/2012"}
        ]



# sort by the desired field first
rows.sort(key=itemgetter("date"))
print(rows)


print("groupby",groupby(rows,key=itemgetter("date")))

for date , items in groupby(rows,key=itemgetter("date")):
    print(date)
    for i in items:
        print(" ",i)

# 如果只是简单地根据日期将数据分组到一起,然后放入一个大的数据结构中允许访问的话,可以采用defaultdict()构建一个一键多值字典,这个例子相对于前面先排序后分组
# 占用的
from collections import defaultdict
rows_by_date =  defaultdict(list)
for row in rows:
    rows_by_date[row["date"]].append(row)
print("rows_by_date",rows_by_date)


for r in rows_by_date["07/04/2012"]:
    print(r)


#### 4.筛选序列中的元素
mylist = [1,4,-5,10,-7,2,3,-1]

list_comprehension = [n for n in mylist if n>0]
print(list_comprehension)

# 如果原始输入非常大的话,那么这样做可能会产生一个庞大的结果.所以可以使用生成器表达式通过迭代的方式产生筛选的结果
pos = (n for n in mylist if n>0)
print(pos)
for x in pos:
    print(x)


values = ["1","2","-3","-","4","N/A","5"]

def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int,values))
print(ivals)



# 表达式除了可以生成数据还可以用来转换数据
import math
# math.sqrt用来开平方根
convert_list = [math.sqrt(n) for n in mylist if n > 0]
print(convert_list)


clip_neg = [n if n>0 else 0 for n in mylist]
print(clip_neg)


#### itertools.compress()函数接受一个可以迭代的对象和一个布尔选择器序列作为输入,同时会输出true对应的序列元素
addresses = [
    '5412 N',
    '5148 N',
    '5800 E',
    '2122 N',
    '5645 N',
    '1060 W',
    '4801 N',
    '1039 w'
]
counts = [0,3,10,4,1,7,6,1]
from itertools import compress
more5 = [n>5 for n in counts]
print(more5)
select_trueitem = list(compress(addresses,more5))
print(select_trueitem)