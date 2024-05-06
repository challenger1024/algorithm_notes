class Solution:
	def isValid(self, word: str) -> bool:
		n=len(word)
		if n<3:
			return False
		o='aeiouAEIOU'
		c='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
		e='#@$'
		x,y,z=0,0,0
		for ch in word:
			if ch in c:
				x+=1
			if ch in o:
				y+=1
			if ch in e:
				z+=1
		return x>=1 and y>=1 and z==0


#test entry
s=Solution()
word="Ya$"
#word = "234Adas"
#word = "b3"
#word=''
print(s.isValid(word))