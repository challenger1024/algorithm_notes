class Solution:
	def countConsistentStrings(self, allowed: str, words) -> int:
		mp=set(allowed)
		ans=0
		for word in words:
			flag=True
			for c in word:
				if c not in mp:
					flag=False
					break
			ans+=1 if flag else 0
		return ans