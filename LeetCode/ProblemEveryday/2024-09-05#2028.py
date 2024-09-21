class Solution:
	def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
		s=sum(rolls)
		m=len(rolls)
		if  mean*(m+n)-s>6*n or (mean*(m+n)-s)//n<=0 :
			return []
		ans=[(mean*(m+n)-s)//n]*n
		end=(mean*(m+n)-s)%n
		for i in range(end):
			ans[i]+=1
		return ans
