class Solution:
	def countGood(self, nums: List[int], k: int) -> int:
		cnt=Counter()
		pairs=0
		ans=0
		l=0
		for r,num in enumerate(nums):
			pairs+=cnt[num]
			cnt[num]+=1
			while pairs>=k:
				cnt[nums[l]]-=1
				pairs-=cnt[nums[l]]
				l+=1
			ans+=l
		return ans