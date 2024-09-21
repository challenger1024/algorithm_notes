MOD=10**9+7
class Solution:
	def rangeSum(self, nums, n: int, left: int, right: int) -> int:
		s=[]
		for i in range(n):
			now=0
			for j in range(i,-1,-1):
				now+=nums[j]
				s.append(now)
		s.sort()
		ans=sum(s[left-1:right])
		return ans%MOD