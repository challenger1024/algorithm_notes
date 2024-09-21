from collections import Counter
class Solution:
	def longestPalindrome(self, s: str) -> int:
		ans=0
		cnt=Counter(s)
		flag=False
		for (k,v) in cnt.items():
			if v%2 and not flag:
				ans+=v
				flag=True
			else:
				ans+=v//2*2
		return ans

#test entry
so=Solution()
s='abccccdd'

print(so.longestPalindrome(s))