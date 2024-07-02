class Solution:
	def wordBreak(self, s: str, wd) -> bool:
		wd.sort(key=lambda x:len(x))
		