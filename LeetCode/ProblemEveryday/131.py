class Solution:
	def partition(self, s: str):# -> List[List[str]]:
		ans=list()
		stack=list()
		def dfs(str,stack):
			if len(str)<=0:
#				print(stack)
				ans.append(stack[:])
#				print(ans)
				return
			for j in range(len(str)):
				if str[:j+1]==str[j::-1]:
					stack.append(str[:j+1])
					dfs(str[j+1:],stack)
					stack.pop()
		dfs(s,stack)
		return ans

#test entry
so=Solution()
s="aab"
print(so.partition(s))