class Solution:
	def totalFruit(self, fruits: List[int]) -> int:
		n=len(fruits)
		cnt=Counter()
		l,r=0,0
		ans=0
		while r<n:
			cnt[fruits[r]]+=1
			while l<n and len(cnt)>2:
				cnt[fruits[l]]-=1
				if cnt[fruits[l]]==0:del(cnt[fruits[l]])
				l+=1
			ans=max(ans,r-l+1)
			r+=1
		return ans