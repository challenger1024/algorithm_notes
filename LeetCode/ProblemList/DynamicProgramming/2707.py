class Solution:
	def minExtraChar(self, s: str, wd) -> int:
		trie={}#字典树的跟
		for i,word in enumerate(wd):
			cur=trie#每次拿到一个词都将指针指向跟部
			for c in word:
				if c not in cur:#避免重复添加同一个键
					cur[c]={}
				cur=cur[c]#指针指向下一层
			cur['#']=len(wd[i])#标记单词结束
		n=len(s)
		dp=[0]*(n+1)
		cur=trie
		for i in range(n+1):
			j=i
			dp[i]=dp[i-1] if i>0 and dp[i-1]>=dp[i] else dp[i]
			while True:
				if '#' in cur:
					dp[j]=max(dp[j],dp[i]+cur['#'])
				if j>=n or s[j] not in cur:
					cur=trie
					break
				else:
					cur=cur[s[j]]
					j+=1
#		print(dp)
		return n-dp[-1]

#solution
so=Solution()
s="kevlplxozaizdhxoimmraiakbak"#'leeta'#"leetcode"
d=["yv","bmab","hv","bnsll","mra","jjqf","g","aiyzi","ip","pfctr","flr","ybbcl","biu","ke","lpl","iak","pirua","ilhqd","zdhx","fux","xaw","pdfvt","xf","t","wq","r","cgmud","aokas","xv","jf","cyys","wcaz","rvegf","ysg","xo","uwb","lw","okgk","vbmi","v","mvo","fxyx","ad","e"]#["leet","code","leetcode"]
print(so.minExtraChar(s,d))