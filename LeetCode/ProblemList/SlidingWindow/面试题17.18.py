class Solution:
	def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
		cnt_small=Counter(small)
		cnt_big=Counter()
		less=len(small)
		ansl,ansr=-1,len(big)
		l=0
		for r,num in enumerate(big):
			cnt_big[num]+=1
			if num in  cnt_small and cnt_big[num]==1:
				less-=1
			while not less:
				if r-l<ansr-ansl:
					ansr,ansl=r,l
				cnt_big[big[l]]-=1
				if cnt_big[big[l]]==0 and big[l] in small:
					less+=1
				l+=1
		return [] if ansl==-1 else [ansl,ansr]