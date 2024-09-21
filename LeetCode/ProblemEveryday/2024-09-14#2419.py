class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		ans=bgst=cnt=0
		for a in nums:
			if a>bgst:
				bgst=a
				cnt=ans=1
			elif a==bgst:
				cnt+=1
				if cnt>ans:
					ans=cnt
			else:
				cnt=0
		return ans

#solution
'''
因为与运算多个数字，结果总是越来越小
所以与运算结果最大的子数组的最大值就是数组nums中的最大值
便利nums中的每个值
1. 如果当前a>bgst,更新bgst,此时a是子数组中的第一个元素
说明之前的数组长度不管有多长，其与运算的结果都不是最大值，抛弃掉,ans和cnt都归1；
2. 如果a==bgst,此时进行与运算后，值不会变小，a可以加入到子数组的末尾，
所以子数组长度cnt+1;
如果当前cnt>ans，更新答案
3. 如果a<bgst,说明子数组中不可能有a,cnt归0
'''