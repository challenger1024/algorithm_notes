class Solution:
	def minExtraChar(self, s: str, dictionary: List[str]) -> int:
		trie={}
		for w in dictionary:
			cur=trie
			for c in w:
				if c not in cur:
					cur[c]={}
				cur=cur[c]
			cur['#']=len(w)
		n=len(s)
		dp=[0]*(n+1)
		cur=trie
		for i in range(n+1):
			j=i
			dp[i]=dp[i-1] if i>0 and dp[i-1]>dp[i] else dp[i]
			while True:
				if '#' in cur:
					dp[j]=max(dp[j],dp[i]+cur['#'])
				if j>=n or s[j] not in cur:
					cur=trie
					break
				else:
					cur=cur[s[j]]
					j+=1
		return n - dp[-1]