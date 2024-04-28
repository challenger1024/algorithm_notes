class Solution:
	def getAverages(self, nums: List[int], k: int) -> List[int]:
		n=len(nums)
		ans=[-1]*n
		l,i,r=0,k,2*k
		if r>=n:
			return ans
		s=sum(nums[l:r+1])
		ans[i]=s//(2*k+1)
		while r<n-1:
			s-=nums[l]
			l+=1
			r+=1
			s+=nums[r]
			i+=1
			ans[i]=s//(2*k+1)
		return ans
