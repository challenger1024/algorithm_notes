class Solution:
	def maxScore(self, cardPoints: List[int], k: int) -> int:
		k=len(cardPoints)-k
		s=0
		ret=0
		ans=float('inf')
		for i,v in enumerate(cardPoints):
			s+=v
			ret+=v
			if i>=k:
				ret-=cardPoints[i-k]
			if i>=k-1:
				ans=min(ans,ret)
		return s-ans