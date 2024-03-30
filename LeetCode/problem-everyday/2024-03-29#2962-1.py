#2962#Count Subarrays Where Max Element Appears at Least K Times
#Simple sliding window:
#start
class Solution:
	def countSubarrays(self, nums, k: int) -> int:
		l=0
		ans=0
		cnt=0
		value=max(nums)
		for num in nums:
			if num==value: cnt+=1
			while cnt==k:
				if nums[l]==value:cnt-=1
				l+=1
			ans+=l
		return ans
#end

#test entry
s=Solution()
#nums = [1,4,2,1]
#k = 3
nums = [1,3,2,3,3] 
k = 2
print(s.countSubarrays(nums,k))

#Solution
'''Divided into zones [l,r], the outer layer is convenient r, the inner layer is convenient l.
class Solution:
	def countSubarrays(self, nums, k: int) -> int:
		l=0
		ans=0
		cnt=0#counter of max value
		value=max(nums)#calculate the max value 
		for num in nums:#num is nums[r],I don't use index r
			if num==value: cnt+=1#nums[r]=max_value,counter+=1
			while cnt==k:#When max_value occurs k times in the interval [l,r], the left pointer is moved
				if nums[l]==value:cnt-=1#nums[l]==max_value,counter-=1
				l+=1
			ans+=l#When the left pointer is ending of moving, the position of the left pointer is just the next index of l  in the interval [l,r] that meets the condition of the problem, and all the subarrays with the left end point of l meet the condition, so the answer is updated
		return ans
'''