class Solution:
	def numberOfSpecialChars(self, word: str) -> int:
		small=[[] for _ in range(26)]
		big=[[] for _ in range(26)]
		ans=0
		for i,c in enumerate(word):
			w=0
			if 'a'<=c<='z' :
				w=ord(c)-ord('a')
				small[w].append(i)
			else:
				w=ord(c)-ord('A')
				big[w].append(i)
		for i in range(26):
			if small[i] and big[i] and small[i][-1]<big[i][0]:
				ans+=1
		return ans

#test entry
s=Solution()
word = "aaAbcBC"
#word = "abc"
#word = "AbBCab"
print(s.numberOfSpecialChars(word))