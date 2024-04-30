from collections import Counter
class Solution:
	def wonderfulSubstrings(self, word: str) -> int:
		mask,ans=0,0
		freq=Counter([0])
		for c in word:
			idx=ord(c)-ord('a')
			mask^=(1<<idx)
			if mask in freq:
				ans+=freq[mask]
			for i in range(10):
				mask_pre=mask^(1<<i)
				if mask_pre in freq:
					ans+=freq[mask_pre]
			freq[mask]+=1
		return ans