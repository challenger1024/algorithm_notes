class Solution:
	def replaceWords(self, d: List[str], sentence: str) -> str:
		s=sentence.split()
		data=set(d)
		for j,word  in enumerate(s):
			for i in range(1,len(word)+1):
				if word[:i] in data:
					s[j]=word[:i]
					break
		return ' '.join(s)