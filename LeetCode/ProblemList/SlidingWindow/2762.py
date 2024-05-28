class Solution:
	def continuousSubarrays(self, nums: List[int]) -> int:
		big=deque()
		small=deque()
		ans=0
		l=0
		for r,num in enumerate(nums):
			while big and big[-1]<num:
				big.pop()
			while small and small[-1]>num:
				small.pop()
			big.append(num)
			small.append(num)
			while abs(big[0]-small[0]) >2:
				if big[0]==nums[l]:
					big.popleft()
				if small[0]==nums[l]:
					small.popleft()
				l+=1	
			ans+=r-l+1
		return ans