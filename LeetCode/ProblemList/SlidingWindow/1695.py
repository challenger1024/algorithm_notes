from collections import Counter
class Solution:
	def maximumUniqueSubarray(self, nums ) -> int:
		n=len(nums)
		cnt=Counter()
		sum,ans=0,0
		l,r=0,0
		while r<n:
			cnt[nums[r]]+=1
			sum+=nums[r]
			while l<n and len(cnt) <r-l+1:
				cnt[nums[l]]-=1
				if cnt[nums[l]]==0:del(cnt[nums[l]])
				sum-=nums[l]
				l+=1
			ans=max(ans,sum)
			r+=1
		return ans

#test entry
s=Solution()
nums=[2,2,1]
print(s.maximumUniqueSubarray(nums))