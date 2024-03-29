#713#Subarray Product Less Than K 
#PrefixSum and dichotomous answers
#accept code
#start
import math
import bisect
class Solution:
	def numSubarrayProductLessThanK(self, nums, k: int) -> int:
		if k==0:return 0
		n=len(nums)
		ans=0
		k=math.log(k)
		pre=[0 for _ in range(n+1)]
		for i in range(n):
			pre[i+1]=pre[i]+math.log(nums[i])
		for right in range(1,n+1):
			left=bisect.bisect_right(pre,pre[right]-k+1e-10,0,right)
			ans+=right-left
		return ans
#end

#test entry
s=Solution()
nums = [10,5,2,6] 
k = 100
print(s.numSubarrayProductLessThanK(nums,k))