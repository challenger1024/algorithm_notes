class Solution:
	def matrixScore(self, grid: List[List[int]]) -> int:
		m,n=len(grid),len(grid[0])
		ans=m*(2**(n-1))
		for j in range(1,n):
			k=0
			for i in range(m):
				if grid[i][j]==grid[i][0]:
					k+=1
			k=max(k,m-k)
			ans+=k*(2**(n-j-1))
		return ans

#solution
'''
贪心解决问题
核心贪心思路：
1. 最高数位要=1
2. 翻转结果中1要尽可能的多
因为二进制数中，1的位置在越高的数位，这个二进制数就越大，所以考虑直接把矩阵中第一列0都变为1.
剩余列则判断是否与第一列相等，相等的话说明第一列需要翻转成1的话，第第[i][j]个位置也翻转成了1，则可以统计第j列中1的数目，
第j列中0的数目=m-第j列中1的数目，两者取最大，就是这一列翻转后1的数目，加入答案中。

'''