from heapq import *
class Solution:
	def getResults(self, queries):# -> List[bool]:
		n=len(queries)
#		axis=[0]+[0]*(min(10**4,3*n))
		h=[]
		ans=[]
#		@lru_cache
		def search(last,end,l):
			if not h or end-last<l:
				return end-last>=l
			now=heappop(h)
			if  now-last>=l and end-last>=l:
				heappush(h,now)
				return True
			ret=search(now,end,l)
			heappush(h,now)
			return ret
		for q in queries:
			if q[0]==1:
#				axis[q[1]]=1
				heappush(h,q[1])
			else:
#				print(h)
#				if not h:
#				print('准备调用')
				ans.append(search(0,q[1],q[2]))
		return ans

#test entry
s=Solution()
#queries =[[1,5],[2,2,1]]
queries=[[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
print(s.getResults(queries))