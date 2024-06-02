from collections import Counter#方便记录数组中元素出现的频率，继承于dict
origin_data=[1,1,1,2,2,2,2,3,3,3,4,4,5]
cnt=Counter(origin_data)#用列表初始化Counter
print(cnt)
l=cnt.most_common(len(origin_data))#返回一个列表，根据元素出现的频率从大到小排序，函数的参数可以是任意数字n,也可以省略，如果省略，则默认为Counter长度
print(l)
len(cnt)#获取cnt中键的数量
del(cnt[key])删除cnt中的某个键值对
