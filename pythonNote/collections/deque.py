'''deque又称为双端队列，在bfs里是非常好用的'''
from collections import deque#导入deque 类

l=[1,2,3,4,5]
q1=deque(l)#用列表初始化deque
print(q1)
q1.append(1)#右端添加元素
print('右端添加元素后：'+str(q1))
r=q1.pop()#右端删除元素,并返回删除的元素
print('删除了'+str(r))
print('右端删除元素后：'+str(q1))
q1.appendleft(1)#左端添加元素
print('左端添加元素后:'+str(q1))
left=q1.popleft()#左端删除元素，并返回被删除的元素
print('左端删除了'+str(left))
print('左端删除元素后:'+str(q1))
