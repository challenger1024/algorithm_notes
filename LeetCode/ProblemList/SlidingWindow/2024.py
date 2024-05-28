class Solution:
	def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
		n=len(answerKey)
		ans=0
		f,t=0,0
		ans=0
		lf,lt=0,0
		for r,c in enumerate(answerKey):
			if c=='F':f+=1
			else:t+=1
			while lf<n and f>k:
				if answerKey[lf]=='F':
					f-=1
				lf+=1
			while lt<n and t>k:
				if answerKey[lt]=='T':
					t-=1
				lt+=1
			ans=max(ans,r-lf+1,r-lt+1)
		return ans