class Solution:
	def duplicateNumbersXOR(self, nums) -> int:
		num=[0]*(51)
		for n in nums:
			num[n]+=1
		ans=0
		for i in range(1,51):
			if num[i]==2:
				ans^=i
		return ans

#test entry
s=Solution()
#nums = [1,2,1,3]
#nums = [1,2,3]
nums = [1,2,2,1]
print(s.duplicateNumbersXOR(nums))