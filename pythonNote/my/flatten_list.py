#一个函数定义，作用是将多为列表展开成一维列表
def flatten_list(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list(item)#用内层列表递归调用函数
        else:
            yield item#不是列表的话则直接返回

#上面函数的使用
nums=[[1,2,3],[4,5,6]]
print(list(flatten_list(nums)))
输出:
[1,2,3,4,5,6]