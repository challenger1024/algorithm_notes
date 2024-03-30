class Solution:
	def cal(self,nums,k):
		cnt=[0]*int(2e4+1)
		l,r=0,0
		ans=0
		dif=0
		while r<len(nums):
			cnt[nums[r]]+=1
			if cnt[nums[r]]==1:
				dif+=1
			while dif>k :
				cnt[nums[l]]-=1
				if cnt[nums[l]]==0:
					dif-=1
				l+=1
			r+=1
			ans+=r-l
		return ans

	def subarraysWithKDistinct(self, nums, k: int) -> int:
		return self.cal(nums,k)-self.cal(nums,k-1)

#test entry
s=Solution()
nums = [1,2,1,2,3]
k = 2
print(s.subarraysWithKDistinct(nums,k))
#想想怎么让内层循环在dif=k+1的时候进入循环，小于k的时候才退出，=k的时候不能进入循环。