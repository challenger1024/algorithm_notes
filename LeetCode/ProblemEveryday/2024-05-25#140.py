class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
		wd=set(wordDict)
		ans=[]
		@lru_cache(None)
		def dfs(i,stack):
			if i>=len(s):
				ans.append(' '.join(stack))
				return
			for j in range(i,len(s)):
				if s[i:j+1] in wd:
					stack.append(s[i:j+1])
					dfs(j+1,stack)
					stack.pop()
		dfs(0,[])
		return ans