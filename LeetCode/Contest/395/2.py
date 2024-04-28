class Solution:
	def minimumAddedInteger(self, nums1, nums2) -> int:
		s=sum(nums1)
		t=sum(nums2)
		nums1.sort()
		nums2.sort()
#		print(s)
#		print(t)
#		print(len(nums2))
		ans=float('inf')
		for i in range(len(nums1)-1):
			for j in range(i+1,len(nums1)):
				temp=s-nums1[i]-nums1[j]
#				print(temp)
				if (t-temp)%len(nums2)==0:
					k,l,ret=0,0,(t-temp)//len(nums2)
					flag=True
					while k<len(nums1) and l<len(nums2):
						if k==i or k==j:
							k+=1
							continue
						if nums1[k]+ret!=nums2[l]:
							flag=False
							break
						k+=1
						l+=1
					if flag:
						ans=min(ans,(t-temp)//len(nums2))
		return ans

#test entry
s=Solution()
nums1=[7,9,1,4]
nums2=[0,8]
#nums1=[10,2,8,7,5,6,7,10]nums2=[5,8,5,3,8,4]
#nums1 = [3,5,5,3]
#nums2 = [7,7]
#nums1 = [4,20,16,12,8]nums2 = [14,18,10]
print(s.minimumAddedInteger(nums1,nums2))