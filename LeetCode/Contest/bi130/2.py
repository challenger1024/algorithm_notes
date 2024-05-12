class Solution:
	def maxPointsInsideSquare(self, points, s: str) -> int:
		n=len(s)
		data=[]
		for i in range(n):
			data.append((points[i][0],points[i][1],s[i]))
		data.sort(key=lambda x: max(abs(x[0]),abs(x[1])))
#		print(data)
		record=set()
		ans=0
		i=0
		for x,y,c in data:
			if c in record:
				ans=max(abs(x),abs(y))-1
				return len(record)
			record.add(c)
			i+=1

s=Solution()
#points = [[1,1],[-2,-2],[-2,2]]str = "abb"
##points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]str = "abdca"
#points = [[1,1],[-1,-1],[2,-2]]str = "ccd"
points=[[0,1],[0,0]]
str="aa"
print(s.maxPointsInsideSquare(points,str))