#哈希集合
class Solution:
	def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
		m=set(bannedWords)
		ret=0
		for w in message:
			if w in m:
				ret+=1
				if ret>=2:
					return True
		return False