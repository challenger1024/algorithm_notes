#字典树模版
class Solution:
	def minimumCost(self, target: str, wd, costs) -> int:
		trie={}#字典树的跟
		for i,word in enumerate(wd):
			cur=trie#每次拿到一个词都将指针指向跟部
			for c in word:
				if c not in cur:#避免重复添加同一个键
					cur[c]={}
				cur=cur[c]#指针指向下一层
			cur['#']={}#标记单词结束