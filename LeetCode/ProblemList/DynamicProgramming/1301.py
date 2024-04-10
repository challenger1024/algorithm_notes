class Solution:
	def pathsWithMaxScore(self, board: List[str]) -> List[int]:
		n=len(board)
		dp=[[[0,0]]*(n+1) for _ in range(n+1)]
		dp[n-1][n-1][1]=1
		for i in range(n-1,-1,-1):
			for j in range(n-1,-1,-1):
				if board[i][j]!='X' and board[i][j]!='S':
					value=max(dp[i][j+1][0],dp[i+1][j+1][0],dp[i+1][j][0])
					if value==dp[i+1][j][0]:dp[i][j][1]+=dp[i+1][j][1]
					if value==dp[i][j+1][0]:dp[i][j][1]+=dp[i][j+1][1]
					if value==dp[i+1][j+1][0]:dp[i][j][1]+=dp[i+1][j+1][1]
					score=(ord(board[i][j])-ord('0')) if board[i][j]!='E' else 0
					dp[i][j][0]=value+score
		return dp[0][0]

