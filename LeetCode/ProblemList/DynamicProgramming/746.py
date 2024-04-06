class Solution:
	def minCostClimbingStairs(self, cost) -> int:
		cost.append(0)
		for i in range(2,len(cost)):
			cost[i]+=min(cost[i-1],cost[i-2])
		return cost[-1]

#test entry
s=Solution()
#cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
print(s.minCostClimbingStairs(cost))