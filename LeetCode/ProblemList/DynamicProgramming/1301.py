mod=10**9+7
class Solution:
	def pathsWithMaxScore(self, board):# -> List[int]:
		n=len(board)
		dp=[[[-1,0]]*n for _ in range(n)]
		dp[n-1][n-1]=[0,1]
		def update(x,y,u,v):
			if u>=n or v>=n or dp[u][v][0]==-1: #or board[u][v]=='X':
				return
			if dp[x][y][0]<dp[u][v][0]:
				dp[x][y]=dp[u][v][:]
			elif dp[x][y][0]==dp[u][v][0]:
				dp[x][y][1]+=dp[u][v][1]

		for i in range(n-1,-1,-1):
			for j in range(n-1,-1,-1):
				if board[i][j]!='S' and board[i][j]!='X':
					update(i,j,i,j+1)
					update(i,j,i+1,j)
					update(i,j,i+1,j+1)
					if dp[i][j][0]!=-1:
						score=0 if board[i][j]=='E'  else ord(board[i][j])-ord('0')
						dp[i][j][0]+=score
		return [0,0] if dp[0][0][0]==-1 else [dp[0][0][0],dp[0][0][1]%mod]





#test entry
s=Solution()
board = ["E12","1X1","21S"]
print(s.pathsWithMaxScore(board))