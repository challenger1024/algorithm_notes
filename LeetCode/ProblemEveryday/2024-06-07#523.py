class Solution:
	def checkSubarraySum(self, nums: List[int], k: int) -> bool:
		n=len(nums)
		if n<2:
			return False
		presum=[0]
		cnt=Counter()
		cnt[0]=-1
		for i,a in enumerate(nums):
			presum.append(a+presum[-1])
			if presum[-1]%k in cnt:
				if i-cnt[presum[-1]%k]>=2:
					return True
			else:
				cnt[presum[-1]%k]=i
		return False
