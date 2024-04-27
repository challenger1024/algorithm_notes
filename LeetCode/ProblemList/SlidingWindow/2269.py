class Solution:
	def divisorSubstrings(self, num: int, k: int) -> int:
		s=str(num)
		n=len(s)
		if n<k:
			return 0
		l,r=0,k
		ans=0
		while r<=n:
			temp=int(s[l:r])
			if temp!=0 and num%temp==0:
				ans+=1
			l+=1
			r+=1
		return ans