#字典树+动态规划


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
		def search(idx):#查找匹配到前缀在target中下一个结尾的索引
			cur=trie
			while idx<len(target) and target[idx] in cur:
				cur=cur[target[idx]]
				idx+=1
			return idx
		n=len(target)
		dp=[0]+[inf]*n
		for i in range(n):
			if dp[i]==inf:
				continue
			end=search(i)
			for j in range(i,end):
				dp[j+1]=min(dp[j+1],dp[i]+1)
		return dp[-1] if dp[-1]!=inf else -1