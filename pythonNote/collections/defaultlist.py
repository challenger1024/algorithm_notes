from collections import defaultlist
#常用于图论相关算法中，用于构造邻接表
#本质是一个字典
#详见题目：#1129
g=defaultdict(list)#键为节点编号，值为当前节点能直接连接到的其他节点的列表,因为值为列表，所以传入list作为参数
#假设有一条鞭从x指向y
x,y=0,1
g[x].append(y)
print(g)
