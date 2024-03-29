#713#Subarray Product Less Than K 
#Simple sliding window:
#accept code
#start
class Solution:
	def numSubarrayProductLessThanK(self, nums, k: int) -> int:
		if k==0:return 0
		ans=0
		x=1
		i=0
		for j,num in enumerate(nums):
			x*=num
			while i<=j and x>=k:
				x//=nums[i]
				i+=1
			ans+=j-i+1
		return ans
#end

#test entry
s=Solution()
nums = [10,5,2,6] 
k = 100
print(s.numSubarrayProductLessThanK(nums,k))

#Solution
'''Simple sliding window:
class Solution:
	def numSubarrayProductLessThanK(self, nums, k: int) -> int:
		if k==0:return 0
		ans=0
		x=1#record the product of the interval [i,j]
		i=0
		for j,num in enumerate(nums):
			x*=num#interval to right
			while i<=j and x>=k:
				x//=nums[i]
				i+=1#i to right
			ans+=j-i+1#find the result of the [i,j],acculate the num of subarray
		return ans'''