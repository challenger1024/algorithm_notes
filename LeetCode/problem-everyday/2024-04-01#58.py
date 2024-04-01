class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		l=0
		s=s[::-1]
		for i,c in enumerate(s):
			if c!=' ' :
				for j in range(i,len(s)):
					if s[j]==' ':return j-i
				return len(s)-i

#test entry
so=Solution()
s='a '
#s = "   fly me   to   the moon  "
#s='hello'
#s = "luffy is still joyboy"
print(so.lengthOfLastWord(s))