class Solution:
	def maximumsSplicedArray(self, nums1, nums2) -> int:
		sum1,sum2=0,0
		pre1,pre2=0,0
		mi,ma=pre1,pre2
		for i in range(len(nums1)):
			pre1=min(pre1+nums1[i]-nums2[i],nums1[i]-nums2[i])
			pre2=max(pre2+nums1[i]-nums2[i],nums1[i]-nums2[i])
			mi=min(pre1,mi)
			ma=max(ma,pre2)
			sum1+=nums1[i]
			sum2+=nums2[i]
		return max(sum1-mi,sum2+ma)

#test entry
s=Solution()
#nums2 = [7,11,13]
#nums1 = [1,1,1]
nums2=[60,60,60]
nums1=[10,90,10]
print(s.maximumsSplicedArray(nums1,nums2))