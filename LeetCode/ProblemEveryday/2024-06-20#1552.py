class Solution:
	def maxDistance(self, pos: List[int], m: int) -> int:
		pos.sort()
		n=len(pos)
		def calc(x):
			num=1
			pre=pos[0]
			for i in range(1,n):
				if pos[i]-pre>=x:
					pre=pos[i]
					num+=1
				if num==m:
					break
			return num==m
		l,r=1,pos[-1]-pos[0]
		while l<=r:
			mid=(l+r)//2
			if calc(mid):
				l=mid+1
			else:
				r=mid-1
		return l-1