class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		cnt1=[0]*26
		cnt2=[0]*26
		k=len(p)
		ans=[]
		for c in p:
			cnt1[ord(c)-ord('a')]+=1
		for i,c in enumerate(s):
			cnt2[ord(c)-ord('a')]+=1
			if i>=k:
				cnt2[ord(s[i-k])-ord('a')]-=1
			if i>=k-1:
				flag=True
				for j in range(26):
					if cnt1[j]!=cnt2[j]:
						flag=False
						break
				if flag:
					ans.append(i-k+1)
		return ans