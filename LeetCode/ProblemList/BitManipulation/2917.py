class Solution:
	def findKOr(self, nums: List[int], k: int) -> int:
		n=max(nums)
		ans=0
		i=1
		while i<=n:
			x=0
			for num in nums:
				if num&i!=0:
					x+=1
			if x>=k:
				ans|=i
			i<<=1
		return ans