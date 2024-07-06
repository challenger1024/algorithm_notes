class Solution:
	def wordBreak(self, s: str, wd) -> bool:
		trie={}#字典树
		for w in wd:
			cur=trie#指针指向字典树根部
			for c in w:
				if c not in cur:
					cur[c]={}
				cur=cur[c]
			cur['#']={}#单词结束标记

		n=len(s)
		dp=[True]+[False]*n
		for i in range(n):
			if not dp[i]:
				continue
			j=i
			cur=trie
			while True:
				if '#' in cur:
					dp[j]=True
				if j>=n:
					break
				if s[j] in cur:
					cur=cur[s[j]]
					j+=1
				else:
					break
#		print(dp)
		return dp[-1]

#test entry
so=Solution()
s="leetcode"
wordDict=["leet","code"]
print(so.wordBreak(s,wordDict))