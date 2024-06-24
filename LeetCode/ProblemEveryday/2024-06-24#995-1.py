class Solution:
	def minKBitFlips(self, nums: List[int], k: int) -> int:
		n=len(nums)
		ans,cnt=0,0
		diff=[0]*(n+1)
		for i in range(n):
			cnt+=diff[i]
			if (nums[i]+cnt)%2==0:
				if i+k>n:
					return -1
				ans+=1
				cnt+=1
				diff[i+k]-=1
		return ans