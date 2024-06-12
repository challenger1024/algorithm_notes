class Solution:
	def maximumOr(self, nums: List[int], k: int) -> int:
		n=len(nums)
		suf=[0]*(n+1)
		for i in range(n-1,0,-1):
			suf[i]=suf[i+1]|nums[i]
		ans=pre=0
		for i,a in enumerate(nums):
			ans=max(ans,pre|(a<<k)|suf[i+1])
			pre|=a
		return ans

#solution
'''
要将nums[i]*2相当于将nums[i]二进制表示左移一位；
要想nums或和最大，就要只对指定的一个数nums[i]进行k次*2操作，但问题就是怎么确定选nums中的哪个数；
利用前缀或和和后缀或和；
预先求出后缀和存储在suf数组中
在求前缀和的同时枚举每次nums[i]<<k,看哪个nums[i]被左移k位后得到的结果最大，即为答案。
'''