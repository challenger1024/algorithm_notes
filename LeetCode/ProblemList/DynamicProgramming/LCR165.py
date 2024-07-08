#同题目91类似
class Solution:
	def crackNumber(self, ct: int) -> int:
		s=str(ct)
		wd=[]
		for i in range(26):
			wd.append(str(i))
		trie={}#字典树的跟
		for i,word in enumerate(wd):
			cur=trie#每次拿到一个词都将指针指向跟部
			for c in word:
				if c not in cur:#避免重复添加同一个键
					cur[c]={}
				cur=cur[c]#指针指向下一层
			cur['#']={}#标记单词结束
		n=len(s)
		dp=[0]*(n+1)
		dp[0]=1
		cur=trie
		for i in range(n+1):
			if dp[i]==0:
				continue
			j=i
			while True:
				if '#' in cur:
					dp[j]+=dp[i]
				if j>=n or s[j] not in cur:
					cur=trie
					break
				else:
					cur=cur[s[j]]
					j+=1
		return dp[-1] 