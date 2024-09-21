class Solution:
	def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
		data=sorted(zip(difficulty,profit))
		worker.sort()
		n,m=len(data),len(worker)
		t=0
		best=0
		ans=0
		for w in worker:
			while t<n and w>=data[t][0]:
				best=max(best,data[t][1])
				t+=1
			ans+=best
		return ans