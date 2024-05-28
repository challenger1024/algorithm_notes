class Solution:
	def countCompleteSubarrays(self, nums: List[int]) -> int:
		less=len(Counter(nums))
		sub=Counter()
		ans=0
		l=0
		for r, num in enumerate(nums):
			sub[num]+=1
			while less==len(sub):
				sub[nums[l]]-=1
				if sub[nums[l]]==0 : del(sub[nums[l]])
				l+=1
			ans+=l
		return ans