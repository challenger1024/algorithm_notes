class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		cnt1=[0]*26
		cnt2=[0]*26
		k=len(s1)
		for c in s1:
			cnt1[ord(c)-ord('a')]+=1
		for i,c in enumerate(s2):
			cnt2[ord(c)-ord('a')]+=1
			if i>=k:
				cnt2[ord(s2[i-k])-ord('a')]-=1
			if i>=k-1:
				flag=True
				for i in range(26):
					if cnt1[i]!=cnt2[i]:
						flag=False
						break
				if flag:
					return True
		return False