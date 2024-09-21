#字典树
class Solution:
	def replaceWords(self, dictionary: List[str], sentence: str) -> str:
		trie={}#字典树的跟
		for word in dictionary:
			cur=trie每次拿到一个词都将指针指向跟部
			for c in word:
				if c not in cur:#避免重复添加同一个键
					cur[c]={}
				cur=cur[c]#指针指向下一层
			cur['#']={}#设置'#'作为结束本单词的标记
		words=sentence.split(' ')
		for i,word in enumerate(words):
			cur=trie#指向字典树的跟
			for j,c in enumerate(word):
				if '#' in cur:#说明查找到了单词word
					words[i]=word[:j]
					break
				if c not in cur:#说明后面没有可以匹配的字符了，直接退出循环
					break
				cur=cur[c]#指针指向下一层
		return ' '.join(words)

#solution
'''
使用字典树存储每个词的前缀
字典树的好处在于每个字符都作为一个键，查起来特别方便
'''