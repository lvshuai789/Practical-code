##
####1. 使用deque找到相匹配的行以后保留之前的最后几项记录
from collections import deque

def search(lines,pattern,history):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)


##use example
if  __name__ == "__main__":
    with open("somthing.txt") as f:
        for line,prevlines in search(f,"python",5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end="")
            print("-"*20)




####2. 找到最大或者最小的N个元素
import heapq
nums=[1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

    #对于复杂情况,可以采用heapq和lambda函数结合

portfolio=[
    {"name":"IBM","shares":100,"price":91.1},
    {"name":"AAPL","shares":100,"price":91.1},
    {"name":"FB","shares":50,"price":21.09}
           ]

cheap=heapq.nsmallest(3,portfolio,key=lambda s:s["price"])
print(cheap)

expensive=heapq.nlargest(3,portfolio,key=lambda s:s["price"])
print(expensive)


####3.如果正在寻找最大或者最小的N个元素,并且同集合中的元素相比,N很小
nums=[1,8,2,23,7,-4,18,23,42,37,2]
import heapq
heap=list(nums)
heapq.heapify(heap)
print(10*"-"+"heap"+"-"*10)
print(heap)

    #### 此类问题是堆排序的算法,heap[0]始终是最小的元素,并且采用heap.heappop()方法,将顶部元素弹出,然后整个堆根据小顶堆调整使得算法的时间复杂度为logN
one=heapq.heappop(heap)
two=heapq.heappop(heap)
print("one=%s"%one)
print("two=%s"%two)

    #### 如果N的大小是和整个集合本身的大小相同,那么就采用sorted方法对整个集合排序,然后做切片操作比较简单
print(sorted(nums)[:3])



####4. 实现优先级队列
#### 此函数设置优先级别第一看push的第二个priority参数 第二个看内部的index(如果优先级别相同的话,谁先进堆谁先出来,第三个是item类,但是基本前两个字段就决定了他的优先级)
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



class Item:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "Item({!r})".format(self.name)


q=PriorityQueue()
q.push(Item("foo"),1)
q.push(Item("bar"),1)
q.push(Item("moo"),2)
a=q.pop()
b=q.pop()
print("a===%s"%a)
print("b==%s"%b)

#### 源码部分的分析
# heapq.heappush([],(-1,0,"m"))
#
# _siftdown([(-1,0,"foo"),(-5,1,"bar")], 0, 1)
# newitem = heap[1]


####5. 在字典中将键映射到多个值上
"""
d = {
    'a':[1,2,3],
    'b':[4,5]
    }
    
   
e = {
    'a':{1,2,3},
    'b':{4,5}
    } 


"""

from collections import defaultdict
"""
d = {
    'xxx':[ ],
    'xxx':[ ]
    }

"""
    #### 不论是否加入了元素,都创建了这个字典里嵌套的列表
d_list=defaultdict(list)
print(d_list)
d_list["a"].append(1)
d_list["a"].append(2)
d_list["b"].append(4)
print(10*"-"+"dlist"+"-"*10)
print(d_list)


d_set=defaultdict(set)
print(d_set)
d_set["a"].add(1)
d_set["a"].add(2)
d_set["b"].add(4)
d_set["b"].add(4)
print(10*"-"+"dset"+"-"*10)
print(d_set)


    ####循环构建的方法
d_list2=defaultdict(list)
pairs={"a":1,"b":2,"c":3}
for key,value in pairs.items():
    d_list2[key].append(value)
print(10 * "-" + "dlist" + "-" * 10)
print(d_list2)


####6. 让字典保持有序
####精确控制各个字段的顺序
#### 但是orderdict因为涉及到创建双向链表的缘故,因此他的存储大小是普通字典的2倍多,设计字典内容比较多的时候需要进行正确分析,是否采用orderdict是明智的选择
from collections import OrderedDict
d=OrderedDict()
d["foo"]=1
d["bar"]=2
d["spam"]=3
d["grok"]=4

for key in d:
    print(key,d[key])

#### 可以在json.dumps中将其序列化编码成为另外的一种结构
import json
json_data = json.dumps(d)
print(json_data)
