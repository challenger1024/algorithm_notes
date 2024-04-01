#LeetCode#442#Find All Duplicates in an Array
#accept code of python
#start
class Solution:
	def findDuplicates(self, nums):
		ret=[]
		for num in nums:
			i=abs(num)
			if nums[i-1]<0:
				ret.append(i)
			else:
				nums[i-1]=-nums[i-1]
		return ret
#end

#test entry
s= Solution()
#nums = [4,3,2,7,8,2,3,1]
#Output:[2,3]
#nums = [1,1,2]
#Output: [1]
nums = [1]
#Output: []
print(s.findDuplicates(nums))

#Description
'''Given an integer array  nums
 of length  n
 where all the integers of  nums
 are in the range  [1, n]
 and each integer appears  once
 or  twice, return  an array of all the integers that appears  twice.
You must write an algorithm that runs in  O(n) 
time and uses only constant extra space.
  Example 1: Input: nums = [4,3,2,7,8,2,3,1]
 Output: [2,3]
 Example 2: Input: nums = [1,1,2]
 Output: [1]
 Example 3: Input: nums = [1]
 Output: []

  Constraints:
•  n == nums.length
•  1 <= n <= 105
•  1 <= nums[i] <= n
•  Each element in  nums
 appears  once or  twice.'''

#Solution
'''Because the values of the elements in the nums range from 1 to n, and the index is 0 to n-1, the index is directly used as the number of elements.
 An element that has already occurred is set to negative as the element to which the index points.
 Here is the annotated code:
class Solution:
	def findDuplicates(self, nums):
		ret=[]# The result that will be return by function
		for num in nums:#Facilitate each element in the array nums
			i=abs(num)#Converts the current number to a positive number because it may be a negative number, which cannot be used as an index of the array
			if nums[i-1]<0:#Since elements in nums take values from 1 to n, and indexes from 0 to n-1, -1 is required
				ret.append(i)#The number corresponding to the index already exists and is added to the result list
			else:#
				nums[i-1]=-nums[i-1]#If the number does not appear, the element in this position is set to its Opposite number
		return ret
