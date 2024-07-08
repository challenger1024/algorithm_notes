class Solution:
	def findTheWinner(self, n: int, k: int) -> int:
		ans=1
		for i in range(2,n+1):
			ans=(k+ans-1)%i+1
		return ans