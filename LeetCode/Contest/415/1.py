
class Solution:
	def minValidStrings(self, words, target: str) -> int:
		trie={}#字典树的跟
		for i,word in enumerate(words):
			cur=trie#每次拿到一个词都将指针指向跟部
			for c in word:
				if c not in cur:#避免重复添加同一个键
					cur[c]={}
				cur=cur[c]#指针指向下一层
			cur['#']={}#标记单词结束
#		@cache
		#cur=trie
		def dfs(cur,i):
			if i>=len(target):
				return 1
			c=target[i]
			if c not in cur and c not in trie:
				return float('inf')
			a=float('inf')
			if c in trie:
				a=1+dfs(trie[c],i+1)
			if c in cur:
				a=min(a,dfs(cur[c],i+1))
			return a
		ans =dfs(trie,0) 
		return ans if ans!=float('inf') else -1

#test
s=Solution()
#words=["abababab","ab"]
#target="ababaababa"
#words = ["abcdef"]
#target = "xyz"
words = ["abc","aaaaa","bcdef"]
target = "aabcdabc"
print('这是一个测试')
print(s.minValidStrings(words,target))