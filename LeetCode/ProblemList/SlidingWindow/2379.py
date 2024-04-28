class Solution:
	def minimumRecolors(self, blocks: str, k: int) -> int:
		n=len(blocks)
		l,r=0,k-1
		ans=0
		for i in range(k):
			if blocks[i]=='W':
				ans+=1
		temp=ans
		while r<n-1:
			if blocks[l]=='W':
				temp-=1
			l+=1
			r+=1
			if blocks[r]=='W':
				temp+=1
			ans=min(temp,ans)
		return ans