class Solution:
	def addedInteger(self, nums1, nums2) -> int:
		s=sum(nums1)
		t=sum(nums2)
		ans=t-s
		return ans//len(nums1)

#test entry
s=Solution()
nums1 = [2,6,4]
nums2 = [9,7,5]
#nums1 = [10]nums2 = [5]
#nums1 = [1,1,1,1]nums2 = [1,1,1,1]
print(s.addedInteger(nums1,nums2))