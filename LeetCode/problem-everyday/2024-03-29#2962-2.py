#2962#Count Subarrays Where Max Element Appears at Least K Times
#This code is a bit cumbersome to write, the same idea as '2962-1.py', but '2962-1' to optimize the code
#start
class Solution:
	def countSubarrays(self, nums, k: int) -> int:
		n=len(nums)
		value=max(nums)
		times=0
		l,r=0,n-1
		ans=0
		for i in range(n):
			if nums[i]==value :times+=1
		if times<k: return 0
		for i in range(n):
			if times==k and nums[i]==value:
				l=i
				break
			if nums[i]==value: times-=1
		while r>=l and r>=k-1:
#			print(str(times)+','+str(l+1))
			if times>=k: ans+=l+1
			if nums[r]==value:times-=1
			r-=1
			while l>0 and times<k:
				l-=1
				if nums[l]==value: times+=1
		return ans
#end

#test entry
s=Solution()
nums = [1,4,2,1]
k = 3
#nums = [1,3,2,3,3] 
#k = 2
print(s.countSubarrays(nums,k))