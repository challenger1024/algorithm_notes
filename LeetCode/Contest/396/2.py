from collections import Counter
class Solution:
	def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
		n=len(word)
		s=[]
		for i in range(0,n,k):
			s.append(word[i:i+k])
		cnt=Counter(s)
#		print(s)
		ans=max(cnt.values())
		return len(s)-ans

#test entry
s=Solution()
word = "leetcoleet"
k = 2
#word = "leetcodeleet"
#k = 4
print(s.minimumOperationsToMakeKPeriodic(word,k))