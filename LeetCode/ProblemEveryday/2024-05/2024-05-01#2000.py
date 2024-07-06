class Solution:
	def reversePrefix(self, word: str, ch: str) -> str:
		idx=word.find(ch)
		return word[idx::-1]+word[idx+1:] if idx!=-1 else word

#test entry
s=Solution()
word='abcdefg'
ch='h'
print(s.reversePrefix(word,ch))