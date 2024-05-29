class Solution:
	def calc(self,nums,x,days):
		ans=1
		sum=0
		for num in nums:
			if sum+num>x:
				ans+=1
				sum=0
			sum+=num
		return ans<=days
	def shipWithinDays(self, weights, days: int) -> int:
		l,r=max(weights),sum(weights)
		while l<=r:
			mid=(l+r)//2
			if self.calc(weights,mid,days):
				r=mid-1
			else:
				l=mid+1
		return l
