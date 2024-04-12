class Solution:
	def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
		m,n=len(dungeon),len(dungeon[0])
		ans=dungeon[0][0]
		for i in range(m):
			for j in range(n):
				if i==0 and j==0:continue
				elif i==0:
					dungeon[i][j]+=dungeon[i][j-1]
				elif j==0:
					dungeon[i][j]+=dungeon[i-1][j]
				else:
					dungeon[i][j]+=max(dungeon[i-1][j],dungeon[i][j-1])
				ans=min(ans,dungeon[i][j])
		return -ans +1 if ans<0 else 1