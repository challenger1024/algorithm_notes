class Solution:
	def findRelativeRanks(self, score: List[int]) -> List[str]:
		d={}
		for i,s in enumerate(score):
			d[s]=i
		keys=sorted(d.items(),key=lambda x: x[0],reverse=True)
		i=0
		for v,k in keys:
			score[d[v]]=str(i+1)
			if i==0:
				score[d[v]]='Gold Medal'
			if i==1:
				score[d[v]]='Silver Medal'
			if i==2:
				score[d[v]]='Bronze Medal'
			i+=1
		return score