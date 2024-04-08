class Solution:
	def maxSumSubmatrix(self, matrix, k: int) -> int:
		def cal( nums) -> int:
			n=len(nums)
			pre=nums[0]
			ans=pre
			for i in range(1,n):
				pre=max(pre+nums[i],nums[i])
#				pre=nums[i] if pre+nums[i]>k else pre+nums[i]
				ans=max(ans,pre)
			return ans
		m,n=len(matrix),len(matrix[0])
		sumArray=[[0]*n for _ in range(m)]
		res=float('-inf')
		for i in range(n):
			sumArray[0][i]=matrix[0][i]
		for i in range(1,m):
			for j in range(n):
				sumArray[i][j]=sumArray[i-1][j]+matrix[i][j]
		for i in range(m):
			for j in range(i,m):
				nums=[]
				for k in range(n):
					nums.append(sumArray[j][k]-sumArray[i][k])
				res=max(res,cal(nums))
		return res

#test entry
s=Solution()
#matrix = [[1,0,1],[0,-2,3]]
#k = 2
matrix = [[2,2,-1]]
k = 3
print(s.maxSumSubmatrix(matrix,k))