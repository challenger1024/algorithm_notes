class Solution:
	def subarraysDivByK(self, nums: List[int], k: int) -> int:
		presum=[0]
		ans=0
		cnt=Counter([])
		cnt[0]=1
		for a in nums:
			presum.append(presum[-1]+a)
			cnt[presum[-1]%k]+=1
			ans+=cnt[presum[-1]%k]-1
		return ans
