class Solution:
	def maxPossibleScore(self, start, d: int) -> int:
		start.sort()
		def judge(x):
			prev=start[0]
			i=1
			while i<len(start):
				if start[i]<=prev+x<=start[i]+d:
					prev=prev+x
				elif prev+x<start[i]:
					prev=start[i]
				else:
					return False
				i+=1
			return True
		left,right=0,d+start[-1]
		while left<=right:
			mid=(left+right)//2
			if judge(mid) :
				left=mid+1
			else:
				right=mid-1
		return left-1

s=Solution()
start=[1000000000,0]
d=1000000000
print(s.maxPossibleScore(start,d))