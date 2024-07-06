from collections import deque
class Solution:
	def exist(self, board, word: str) -> bool:
		n=len(board)
		m=len(board[0])
		dir=[-1,0,1,0,-1]
		def check_index(i,j,k):
			if not 0<=i<n: return False
			if not 0<=j<m: return False
			if word[k]!=board[i][j]:return False
			return True
		checkup=[[False]*m for _ in range(n)]
		def dfs(i,j,k):
			if word[k]!=board[i][j]:
				return False
			if k==len(word)-1:
#				print(k)
				return True
			ret=False
			checkup[i][j]=True
			for index in range(4):
				ti,tj,tk=i+dir[index],j+dir[index+1],k+1
				if check_index(ti,tj,tk) and not checkup[ti][tj]:
					if  dfs(ti,tj,tk):
						ret=True
						break
			checkup[i][j]=False
			return ret

		for i in range(n):
			for j in range(m):
				if dfs(i,j,0):return True
		return False

#test entry
s=Solution()
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCB"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "ABCCED"
print(s.exist(board,word))