#41#First Missing Positive
#accept code:
#start
class Solution:
	def firstMissingPositive(self, nums) -> int:
		n=len(nums)
		for i in range(n):
			if nums[i]<=0: nums[i]=n+1
		for num in nums:
			temp=abs(num)
			if temp<n+1 and nums[temp-1]>0:
				nums[temp-1]=-nums[temp-1]
		for i in range(n):
			if nums[i]>0:
				return i+1
		return n+1
#end

#test entry
s=Solution()
#nums=[1,2,0]
nums=[3,4,-1,1]
#nums=[1]
#nums = [1,2,0]
#nums = [3,4,-1,1]
#nums = [7,8,9,11,12]
print(s.firstMissingPositive(nums))

#Description
'''Given an unsorted integer array  nums
. Return the  smallest positive integer that is  not present in  nums
.
You must implement an algorithm that runs in  O(n)
 time and uses  O(1)
 auxiliary space.
  Example 1: Input: nums = [1,2,0]
 Output: 3
 Explanation:  The numbers in the range [1,2] are all in the array.
 Example 2: Input: nums = [3,4,-1,1]
 Output: 2
 Explanation:  1 is in the array but 2 is missing.
 Example 3: Input: nums = [7,8,9,11,12]
 Output: 1
 Explanation:  The smallest positive integer 1 is missing.

  Constraints:
•  1 <= nums.length <= 105
•  -231 <= nums[i] <= 231 - 1'''

#Solution
'''According to the description of the problem, if the array length is n, the answer is in the interval [1,n+1].
 Suppose the answer is >=n+2, then if the n numbers in the array happen to be [1,n], then the answer should be n+1, which contradicts the problem.
 If the number in the array is not [1,n], then there must be positive integers in [1,n] that are not in the array, also contradicting the assumption.
 Here is the annotated code:'''
class Solution:
	def firstMissingPositive(self, nums) -> int:
		n=len(nums)#the length of nums
		for i in range(n):
			if nums[i]<=0: nums[i]=n+1#Since the numbers in nums may be <=0, setting them all to n+1 does not affect the accuracy of the answer
		for num in nums:
			temp=abs(num)#absolute value
			if temp<n+1 and nums[temp-1]>0:
				nums[temp-1]=-nums[temp-1]Use an index as a hash table to mark the presence or absence of a number
		for i in range(n):
			if nums[i]>0:
				return i+1
		return n+1