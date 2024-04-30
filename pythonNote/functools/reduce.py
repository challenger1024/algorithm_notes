from functools import reduce
def add(a,b):
	return a+b
nums=[1,2,3,4,5]
ans=reduce(add,nums,5)
print(ans)
'''
从左到右对一个序列的项目累计地应用有两个参数的函数，以此合并序列到一个单一值。
reduce有三个参数：
function：有两个参数的额函数，           必需参数，上面的实例中是add()函数
sequence: 元组、列表等可迭代对象，  必需参数，上面的实例中是nums
inital： 初始值，                                     可选参数,上面的实例中是5，可以不写
'''