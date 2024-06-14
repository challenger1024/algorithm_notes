class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		ans=0
		yes=0#删除一个0后的连续1数量
		no=0#什么都没删除的时候，连续1的数量
		for a in nums:
			if a==0:
				no,yes=0,no
			else:
				no+=1
				yes+=1
			ans=max(ans,yes)
		return ans if ans !=len(nums) else ans-1

#solution
'''
定义两个变量yes和no
yes:删除一个0后，连续1的数量
no:什么都不删除，连续1的数量
便利数组nums
以nums[i]=a为结尾的子数组有下面两种情况:
1. 如果a==0
说明当前元素可以被删除
`yes=no`删除掉这个0,后，连续1的数量最多为以上一个数字为结尾的什么都不删除的连续1的数量
`no=0`连续1的数量变为0
2. 如果a==1
yes和no都可以+1，表示连续1的数量增加了1
循环中，每次判断当前yes是否>ans，如果是，更新答案。

'''