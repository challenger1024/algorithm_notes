class Solution:
	def binaryGap(self, n: int) -> int:
		if n&(n-1)==0:
			return 0
		pre,now=0,0
		i=0
		ans=0
		flag=False
		while n:
			if  n&1==1:
				now=i
				if flag==False:
					pre=now
					flag=True
			ans=max(ans,now-pre)
			pre=now
			i+=1
			n>>=1
		return ans
