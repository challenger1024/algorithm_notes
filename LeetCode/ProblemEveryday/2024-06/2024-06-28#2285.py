class Solution:
	def maximumImportance(self, n: int, roads) -> int:
		ins=[0]*n
		for (a,b) in roads:
			ins[a]+=1
			ins[b]+=1
		ins.sort()
		ans=0
		for i in range(1,n+1):
			ans+=i*ins[i-1]
		return ans