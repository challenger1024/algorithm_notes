class Solution:
	def canMakeSquare(self, grid) -> bool:
#		d=[[] for _ in range(4)]
		dirs=[0,1,1,0]
		for i in range(2):
			for j in range(2):
				x=grid[i][j]
				ret=1
				for k in range(3):
					di,dj=i+dirs[k],j+dirs[k+1]
#					print(f'x是{x},grid[di][dj]是{grid[di][dj]},i={di},j={dj}')
					if grid[di][dj]==x:
						ret+=1
				if ret==3 or ret==1 or ret==4:
					return True
		return False

#test entry
s=Solution()
grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
#grid = [["B","W","B"],["W","B","W"],["B","W","B"]]
#grid = [["B","W","B"],["B","W","W"],["B","W","W"]]
print(s.canMakeSquare(grid))