class Solution:
	def uncommonFromSentences(self, s1: str, s2: str):# -> List[str]:
		ans=[]
		cnt=Counter(s1.split())+Counter(s2.split())
		for w,t in cnt.items():
			if t==1:
				ans.append(w)
		return ans