class Solution:
	def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
		n=len(obstacles)
		ans=[1]*n
		d=[]
		ret=1
		for i in range(n):
			if not d or d[-1]<=obstacles[i]:
				d.append(obstacles[i])
				ans[i]=len(d)
			else:
				l,r=0,len(d)-1
				loc=r
				while l<=r:
					mid=(l+r)//2
					if d[mid]>obstacles[i]:
						loc=mid
						r=mid-1
					else:
						l=mid+1
				d[loc]=obstacles[i]
				ans[i]=loc+1
		return ans