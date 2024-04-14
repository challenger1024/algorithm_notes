class Solution:
	def minRectanglesToCoverPoints(self, points, w: int) -> int:
		points.sort()
		ans=1
		i=points[0][0]
		for point in points:
			if point[0]<=i+w:
				continue
			i=point[0]
			ans+=1
		return ans

#test entry
s=Solution()
points = [[2,3],[1,2]]
w = 0
#points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
#w = 2
#points=[[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]
#w=1
print(s.minRectanglesToCoverPoints(points,w))