class Solution:
	def longestEqualSubarray(self, nums, k: int) -> int:
		n=len(nums)
		cnt=defaultdict(int)
		ans=0
		l=0
		for r,num in enumerate(nums):
			cnt[num]+=1
			while l<n and cnt[nums[l]]+k<r-l+1:
				cnt[nums[l]]-=1
				l+=1
			ans=max(ans,cnt[nums[r]])
		return ans

#test entry
s=Solution()
nums=[1,2,1]
k=2
print(s.longestEqualSubarray(nums,k))