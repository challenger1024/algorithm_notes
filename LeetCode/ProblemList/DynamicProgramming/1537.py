MOD=10**9+7
class Solution:
	def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
		m,n=len(nums1),len(nums2)
		i=j=0
		best1=0#最后一个数字是nums1中的
		best2=0#最后一个数字是nums2中的
		while i<m or j<n:
			if i<m and j<n:
				if nums1[i]<nums2[j]:
					best1+=nums1[i]
					i+=1
				elif nums1[i]>nums2[j]:
					best2+=nums2[j]
					j+=1
				else:
					best=nums1[i]+(best1 if best1>best2 else best2)
					best1=best2=best
					i+=1
					j+=1
			elif i<m:
				best1+=nums1[i]
				i+=1
			elif j<n:
				best2+=nums2[j]
				j+=1
		return (best1 if best1>best2 else best2)%MOD