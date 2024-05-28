class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		n=len(nums)
		ans=0
		cnt=0
		l,r=0,-1
		last=-1
		while l<n:
			if l>0:
				cnt-=nums[l-1]
			while r+1<n and (cnt+1==r-l+1 or cnt==r-l+1):
				cnt+=nums[r+1]
				r+=1
			ans=max(ans,cnt-1 if cnt==r-l+1 else cnt)
			l+=1
		return ans