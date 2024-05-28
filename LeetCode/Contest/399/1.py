class Solution:
	def numberOfPairs(self, nums1, nums2, k: int) -> int:
		n,m=len(nums1),len(nums2)
		ans=0
		for i ,x in enumerate(nums1):
			if x%k!=0:
				continue
			for j,y in enumerate(nums2):
				if x%(y*k)==0:
					ans+=1
		return ans
#test entry
s=Solution()
nums1=[2,12]
nums2=[4,3]
k=4
#nums1 = [1,3,4]
#nums2 = [1,3,4]
#k = 1
print(s.numberOfPairs(nums1,nums2,k))