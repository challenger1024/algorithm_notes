class Solution:
	def maxPointsInsideSquare(self, points, s: str) -> int:
		data=sorted(zip(points,s),key=lambda x: max(abs(x[0][0]),abs(x[0][1])))
		def calc(k):
			tags=set()
			for ([x,y],c) in data:
				if abs(x)>k or abs(y)>k:
					return True
				if c in tags:
					return False
				tags.add(c)
			return True

		l,r=0,max(abs(data[-1][0][0]),abs(data[-1][0][1]))
		while l<=r:
			mid=(l+r)//2
			if calc(mid) :
				l=mid+1
			else:
				r=mid-1
		loc=l-1
		ans=0
		for ([x,y],c) in data:
			if abs(x)>loc or abs(y)>loc:
				break
			ans+=1
		return ans

so=Solution()
#points=[[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]#s="abdca"
#points = [[1,1],[-2,-2],[-2,2]]s = "abb"
points = [[1,1],[-1,-1],[2,-2]]
s = "ccd"
print(so.maxPointsInsideSquare(points,s))