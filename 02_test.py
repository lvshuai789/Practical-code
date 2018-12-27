#### 1.与字典有关的计算问题
prices = {
    "ACME":45.23,
    "APPL":612.78,
    "IBM":205.55,
    "HPQ":37.20,
    "FB":10.75
}

min_price=min(zip(prices.values(),prices.keys()))
print(min_price)

max_price=max(zip(prices.values(),prices.keys()))
print(max_price)


#### 还可以使用zip()和sorted()函数来配合使用
prices_sorted = sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)


## ********** 需要注意的一点是 **************
#zip创建的迭代器只能被消费一次
prices_and_names = zip(prices.values(),prices.keys())
try:
    print(min(prices_and_names))
    print(max(prices_and_names))
except Exception as e:
    print(e,"主要原因是zip创建的迭代器只能被消费一次")


## 还有一种简单的办法.判断值从而返回键:
    min=min(prices,key=lambda k:prices[k])
    print(min)

    max=max(prices,key=lambda k:prices[k])
    print(max)
## 如果是要得到值的话
    min_value=prices[min]
    max_value=prices[max]
    print("只得到最小值min_value=%s"%min_value)
    print("只得到最大值max_value=%s" % max_value)



####突发奇想,使用01_test.py中的有序排列队列依然可以得出排序中的最大最小值,只需调整priority参数即可
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index +=1
    ## 返回队列优先级别高的新建类
    def pop(self):
        return heapq.heappop(self._queue)[-1]
#### min
q=PriorityQueue()
for item_key,item_value in prices.items():
    q.push(item_key,-item_value)
print("min=%s"%q.pop())
#### max
for item_key,item_value in prices.items():
    q.push(item_key,item_value)
print("max=%s"%q.pop())




####2. 在两个字典中寻找相同点

a={"x":1,
   "y":2,
   "z":3}

b={"w":10,
   "x":11,
   "y":2}

# find keys in common
common = a.keys() & b.keys()
print(common)

# find keys in a that are not in b
differ = a.keys() - b.keys()
print(differ)

# find (key,value) pairs in common
common_key_and_value = a.items() & b.items()
print(common_key_and_value)


# make a new dictionary with certain keys removed
c = {key:a[key]for key in a.keys() - {"z","w"}}
print("c is %s"%c)



####3. 从序列中移除重复项元素并且保持元素间的顺序不变

def dedupe(items):
    seen=set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

alist = [1,5,2,1,9,1,5,10]
print("dedupe type:%s"%dedupe(a))
for item in dedupe(a):
    print("item=%s"%item)

print(list(dedupe(a)))


#### 消除a=[{"x":1,"y":2},{"x":1,"y":3},{"x":1,"y":2},{"x":2,"y":4}]
def dedupe(it,key=None):
    seen=set()
    for item in it:
        val=item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# c = lambda d:(d["x"],d["y"])
# a=[{"x":1,"y":2},{"x":1,"y":3}]
# for item in a:
#     print(item)
# print(c({'x': 1, 'y': 2}))

a=[{"x":1,"y":2},{"x":1,"y":3},{"x":1,"y":2},{"x":2,"y":4}]
print(list(dedupe(a,key=lambda d: (d["x"],d["y"]))))
print(list(dedupe(a,key=lambda d: d["x"])))

#### 通常也可以去除文件的重复行
with open("somthing.txt",'r') as f:
    for line in dedupe(f):
        print(line)


####4. 对切片命名
record = '....................100.......513.25..........'
# record='....................100.......513.25..........'
# cost = int(record[20:22]) * float(record[30:35])
# print(cost)

SHARES = slice(20,22)
PRICE = slice(30,35)
cost = int(record[SHARES])*float(record[PRICE])
print("cost=%s"%cost)
# print(record[20:22])
# print(record[30:35])


####5. 对于列表
items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(a)
print(items[2:4])
print(items[a])
del items[a]
print(items)



### indices的作用是在a.slice切片的基础上定位end位置的元素索引,如果在slice范围内就更新slice上的end位置元素,如果超过了就不更新end还是slice切片范围
print(a.indices(100))


####6.找出序列中出现的元素次数最多的元素
words = [
    'look','into','my','eyes','look','into','my','eyes','eyes'
]
#### 统计most_common中所填写的数量的高频率单词从高到底
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(4)
print(top_three)

eyes_count=word_counts["eyes"]
print(eyes_count)

#### 在原来的基础上增加计数
more_words = [
    'look','into','my','eyes','look','into','my','eyes','eyes'
]
####1.手动计数
for word in more_words:
    word_counts[word] += 1
print(word_counts)

####2.可以使用word_counts的update方法来更新元素出现的次数
word_counts.update(more_words)
print(word_counts)

####3.同时Counter对象也有一个特性,那就是他们可以轻松的同各种数学运算结合起来使用
a=Counter(words)
b=Counter(more_words)

print("a=%s"%a)
print("b=%s"%b)

c=a+b
print('c=%s'%c)

d=a-b
print("d=%s"%d)

##### *********Counter类可以用来进行数据制表或者计数问题**********