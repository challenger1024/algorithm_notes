class Solution:
	def commonChars(self, words):# -> List[str]:
		ret=[inf]*26
		for word in words:
			letters=[0]*26
			for c in word:
				letters[ord(c)-ord('a')]+=1
			for i in range(26):
				ret[i]=min(ret[i],letters[i])
		ans=[]
		for i in range(26):
			if ret[i]!=inf:
				for j in range(ret[i]):
					ans.append(chr(i+97))
		return ans
