#状态机dp
class Solution:
	def maxNonDecreasingLength(self, nums1, nums2) -> int:
		n=len(nums1)
		dp=[[1]*2 for _ in range(n)]
		ans=1
		for i in range(1,n):
			if nums1[i]>=nums1[i-1]:
				dp[i][0]=dp[i-1][0]+1
			if nums1[i]>=nums2[i-1]:
				dp[i][0]=max(dp[i][0],dp[i-1][1]+1)
			if nums2[i] >= nums2[i-1]:
				dp[i][1]=dp[i-1][1]+1
			if nums2[i]>=nums1[i-1]:
				dp[i][1]=max(dp[i][1],dp[i-1][0]+1)
			ans=max(ans,dp[i][0],dp[i][1])
		print(dp)
		return ans

#test entry
s=Solution()
nums1=[4,19,4]
nums2=[13,13,16]
print(s.maxNonDecreasingLength(nums1,nums2))