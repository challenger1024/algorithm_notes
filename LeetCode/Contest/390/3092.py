from collections import Counter
from heapq import heappush,heappop
class Solution:
	def mostFrequentIDs(self, nums, freq):
		ans=[]
		cnt=Counter()
		heap=[]
		for num,f in zip(nums,freq):
			cnt[num]+=f
			heappush(heap,(-cnt[num],num))
			while -heap[0][0]!=cnt[heap[0][1]]:
				heappop(heap)
			ans.append(-heap[0][0])
		return ans

#test entry
s=Solution()
#nums = [5,5,3]
#freq = [2,-2,1]
nums = [2,3,2,1]
freq = [3,2,-3,1]
print(s.mostFrequentIDs(nums,freq))