class Solution:
	def calculateMinimumHP(self, dungeon) -> int:
		m,n=len(dungeon),len(dungeon[0])
#		ans=dungeon[0][0]
		dungeon[m-1][n-1]=1-dungeon[m-1][n-1] if dungeon[m-1][n-1]<0 else 1
		for i in range(m-1,-1,-1):
			for j in range(n-1,-1,-1):
				if i==m-1 and j==n-1:continue
				elif i==m-1:
					dungeon[i][j]=dungeon[i][j+1]-dungeon[i][j]
				elif j==n-1:
					dungeon[i][j]=dungeon[i+1][j]-dungeon[i][j]
				else:
					dungeon[i][j]=min(dungeon[i+1][j],dungeon[i][j+1])-dungeon[i][j]
				dungeon[i][j]=max(dungeon[i][j],1)
		return max(dungeon[0][0],1)

#test entry
s=Solution()
#dungeon = [[0]]
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(s.calculateMinimumHP(dungeon))