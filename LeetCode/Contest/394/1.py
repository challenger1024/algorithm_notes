from collections import Counter
class Solution:
	def numberOfSpecialChars(self, word: str) -> int:
		cnt=Counter(word)
		ans=0
		for i in range(26):
			if cnt[chr(65+i)]>0 and cnt[chr(97+i)]>0:
				ans+=1
		return ans

#test entry
s=Solution()
#word = "abBCab"
#word = "abc"
word = "aaAbcBC"
print(s.numberOfSpecialChars(word))