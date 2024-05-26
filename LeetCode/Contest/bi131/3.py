from collections import Counter
class Solution:
	def queryResults(self, limit, queries):# -> List[int]:
		cnt=Counter()
		ball=Counter()
		ans=[]
		for (x,y) in queries:
			cnt[y]+=1
			temp=ball[x]
			if temp in cnt:
				cnt[temp]-=1
				if cnt[temp]==0:del(cnt[temp])
			ball[x]=y
			ans.append(len(cnt))
		return ans

#test entry
s=Solution()
#limit = 4queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]
print(s.queryResults(limit, queries))