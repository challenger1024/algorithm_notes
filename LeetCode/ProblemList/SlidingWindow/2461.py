from collections import Counter
class Solution:
	def maximumSubarraySum(self, nums, k: int) -> int:
		n=len(nums)
		ans=0
		s=0
		cnt=Counter()
		for i in range(n):
			cnt[nums[i]]+=1
			s+=nums[i]
#			print(s)
			if i>=k:
				cnt[nums[i-k]]-=1
				if cnt[nums[i-k]]==0:del(cnt[nums[i-k]])
				s-=nums[i-k]
			if len(cnt.keys())==k:
				ans=max(ans,s)
		return ans

#test entry
s=Solution()
nums=[1,5,4,2,9,9,9]
k=3
print(s.maximumSubarraySum(nums,k))