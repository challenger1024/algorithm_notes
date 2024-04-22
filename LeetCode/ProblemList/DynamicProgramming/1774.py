class Solution:
	def closestCost(self, baseCosts, toppingCosts, target: int) -> int:
		x=min(baseCosts)
		if x>=target:
			return x
		dp=[False for _ in range(2*target-x+1)]
		for base in baseCosts:
			if base>2*target-x:continue
			dp[base]=True
		for topping in toppingCosts*2:
			for j in range(2*target-x,x-1,-1):
				if j>=topping:
					dp[j]=dp[j] or dp[j-topping]
#				if j>=2*topping:
#					dp[j]|=dp[j-2*topping]
		ans=target
#		print(dp)
		for i in range(target,-1,-1):
			if dp[i] :
				ans=i
				break
			if dp[2*target-i]:
				ans=2*target-i
				break
		return ans

#test entry
s=Solution()
#baseCosts = [2,3]
#toppingCosts = [4,5,100]
#target = 18
#baseCosts = [3,10]
#toppingCosts = [2,5]
#target = 9
baseCosts=[4,10,8,8]
toppingCosts=[10,6,10,9,9,6,5]
target=7
print(s.closestCost(baseCosts,toppingCosts,target))