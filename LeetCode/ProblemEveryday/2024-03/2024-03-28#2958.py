#2958#Length of Longest Subarray With at Most K Frequency
#accept code
#start
import collections
class Solution:
	def maxSubarrayLength(self, nums, k: int) -> int:
		ans=0
		l=0
		cnt=collections.Counter()
		for r , num in enumerate(nums):
			cnt[num]+=1
			while cnt[num]>k and l<=r:
				cnt[nums[l]]-=1
				l+=1
			ans=max(ans,r-l+1)
		return ans
#end
#test entry
s=Solution()
nums = [1,2,3,1,2,3,1,2]
k = 2
print(s.maxSubarrayLength(nums,k))

#Solution
'''Simple sliding window:
class Solution:
	def maxSubarrayLength(self, nums, k: int) -> int:
		ans=0
		l=0#left of subarray
		cnt=collections.Counter()#record the frequency of the numbers of nums
		for r , num in enumerate(nums):#r is the right of subarray
			cnt[num]+=1
			while cnt[num]>k and l<=r:
				cnt[nums[l]]-=1#if num appear more than k times,l goes to right
				l+=1
			ans=max(ans,r-l+1)#update answer
		return ans
'''