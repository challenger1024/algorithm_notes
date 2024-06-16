class Solution:
	def getMaxLen(self, nums: List[int]) -> int:
		n=len(nums)
		nega=[0]*n
		poss=[0]*n
		if nums[0]>0:
			poss[0]=1
		elif nums[0]<0:
			nega[0]=1
		ans=poss[0]
		for i in range(1,n):
			if nums[i]>0:
				poss[i]=poss[i-1]+1
				nega[i]=(nega[i-1]+1 if nega[i-1]>0 else 0)
			elif nums[i]<0:
				poss[i]=(nega[i-1]+1 if nega[i-1]>0 else 0)
				nega[i]=poss[i-1]+1
			else:
				poss[i]=0
				nega[i]=0
			ans=max(poss[i],ans)
		return ans