MOD=10**9+7
class Solution:
	def distinctSubseqII(self, s: str) -> int:
		letter=[-1]*26
		n=len(s)
		dp=[1]*n
		for i,c in enumerate(s):
			for j in range(26):
				if letter[j]>=0:
					dp[i]+=dp[letter[j]]%MOD
			letter[ord(s[i])-ord('a')]=i
		return sum(dp[letter[i]] for i in range(26) if letter[i]>=0)%MOD