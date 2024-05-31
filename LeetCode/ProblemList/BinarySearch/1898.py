class Solution:
	def calc(self,s,t,remove,k):
		ns,nt=len(s),len(t)
		revs=[True]*ns
		for i in range(k):
			revs[remove[i]]=False
		i=0
		for j ,c in enumerate(s):
			if i<nt and  revs[j] and t[i]==c:
				i+=1
		return i==nt
	def maximumRemovals(self, s: str, p: str, rem: List[int]) -> int:
		l,r=1,len(rem)
		while l<=r:
			mid=(l+r)//2
			if self.calc(s,p,rem,mid):
				l=mid+1
			else:
				r=mid-1
		return l-1