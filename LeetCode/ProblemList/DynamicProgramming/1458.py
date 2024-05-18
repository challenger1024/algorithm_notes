class Solution:
	def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
		m,n=len(nums1),len(nums2)
		dp=[[-inf]*n for _ in range(m)]
		dp[0][0]=0
		for i in range(m):
			for j in range(n):
				xij=nums1[i]*nums2[j]
				dp[i][j]=xij
				if i >0:
					dp[i][j]=max(dp[i][j],dp[i-1][j])
				if j>0:
					dp[i][j]=max(dp[i][j],dp[i][j-1])
				if i>0 and j>0:
					dp[i][j]=max(dp[i][j],dp[i-1][j-1]+xij)
		return dp[m-1][n-1]