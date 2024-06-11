class Solution:
	def maxSubarrays(self, nums: List[int]) -> int:
		n=len(nums)
		small=-1
		ans=0
		for a in nums:
			small&=a
			if small==0:
				ans+=1
				small=-1
		return max(ans,1)

#solution
'''
因为与运算的操作数越多结果越小
所以最小分数一定是整个数组nums的与运算结果
因此设nums数组的与运算结果为small,分成两种情况
1. small=0,有几个子数组的与运算结果为0，即为答案；
2. small>0,此时如果有两个或以上的子数组与运算结果为small,那么其分数和即为2*small或更大，不满足题意，
因此，small>0时，只能有一个子数组，就是nums本身。
据此枚举nums中的每一个数，进行运算。
'''