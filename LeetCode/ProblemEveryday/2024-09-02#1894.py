class Solution:
	def chalkReplacer(self, chalk, k: int) -> int:
		n=len(chalk)
		s=sum(chalk)
		k%=s
#		print(k)
		i=0
		while k>0 and i<n:
			k-=chalk[i]
			i+=1
		return i%n if k==0 else i-1

#test entry
s=Solution()
chalk=[3,4,1,2]
k=25
print(s.chalkReplacer(chalk,k))