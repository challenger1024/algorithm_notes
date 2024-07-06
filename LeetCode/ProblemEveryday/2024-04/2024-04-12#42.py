class Solution:
	def trap(self, height: List[int]) -> int:
		n=len(height)
		l=[0]*n
		r=[0]*n
		l[0]=height[0]
		r[n-1]=height[n-1]
		for i in range(1,n):
			l[i]=max(l[i-1],height[i])
		for i in range(n-2,-1,-1):
			r[i]=max(r[i+1],height[i])
		ans=0
		for i in range(n):
			ans+=min(l[i],r[i])-height[i]
		return ans