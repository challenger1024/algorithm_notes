from bisect import *
class Solution:
	def LIS(self, nums ) -> int:
		d=[]
		for num in nums:
			if not d or num>=d[-1]:
				d.append(num)
			else:
				loc=bisect_right(d,num)
				d[loc]=num
		return len(nums) - len(d)
	def kIncreasing(self, arr , k: int) -> int:
		ans=0
		n=len(arr)
		for i in range(k):
			ans+=self.LIS(arr[i::k])
		return ans

#test entry
s=Solution()
arr=[4,1,5,2,6,2]
k=2
print(s.kIncreasing(arr,k))