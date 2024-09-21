class Solution:
	def xorQueries(self, arr, queries):# -> List[int]:
		ans=[]
		preSum=[0]
		for i in range(len(arr)):
			preSum.append(preSum[-1]^arr[i])
		for l,r in queries:
			ans.append(preSum[r+1]^preSum[l])
		return ans
