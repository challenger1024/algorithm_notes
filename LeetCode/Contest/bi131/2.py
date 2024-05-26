class Solution:
	def occurrencesOfElement(self, nums, queries, x: int):# -> List[int]:
		dp=[0]
		for i,num in enumerate(nums):
			if num==x:
				dp.append(i)
		ans=[]
#		print(dp)
		for i,q in enumerate(queries):
			if q>=len(dp):
				ans.append(-1)
			else:
				ans.append(dp[q])
#		print(ans)
		return ans

#test entry
s=Solution()
#nums = [1,2,3]queries = [10]x = 5
nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1
print(s.occurrencesOfElement(nums, queries, x))
