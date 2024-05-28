class Solution:
	def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
		n=len(nums)
		cnt=[0]*101
		ans=[0]*(n-k+1)
		for i in range(k-1):
			cnt[nums[i]]+=1
		for i, (l,r) in enumerate(zip(nums,nums[k-1:])):
			cnt[r]+=1
			flag=x
			for j in range(-50,0):
				flag-=cnt[j]
				if flag<=0:
					ans[i]=j
					break
			cnt[l]-=1
		return ans