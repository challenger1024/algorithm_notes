class Solution:
	def longestSubarray(self, nums: List[int], limit: int) -> int:
		n=len(nums)
		big,small=deque(),deque()
		l,r=0,0
		ans=0
		while r<n:
			while big and big[-1]<nums[r]:
				big.pop()
			while small and small[-1]>nums[r]:
				small.pop()
			big.append(nums[r])
			small.append(nums[r])
			while big and small and big[0]-small[0]>limit:
				if big[0]==nums[l]:
					big.popleft()
				if small[0]==nums[l]:
					small.popleft()
				l+=1
			ans=max(ans,r-l+1)
			r+=1
		return ans