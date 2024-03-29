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