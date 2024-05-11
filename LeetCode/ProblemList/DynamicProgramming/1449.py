class Solution:
	def largestNumber(self, cost, target: int) -> str:
		def make(s,ch):
			ch=str(ch)
			s=str(s)
			for i,c in enumerate(s):
				if ch>=c:
					return int(s[:i]+ch+s[i:])
			return int(s+ch)
		dp=[float('-inf')]*(target+1)
		dp[0]=0
		for i ,c in enumerate(cost):
			for j in range(c,target+1):
				dp[j]=max(dp[j],dp[j-c]+1)
		if dp[target]<0:
			return '0'
		ans=[]
		g=target
		for i in range(8,-1,-1):
			c=cost[i]
			while j>=c and dp[j]==dp[j-c]+1:
				ans.append(str(i+1))
				j-=c
		return ''.join(ans)

#test entry
s=Solution()
cost = [4,3,2,5,6,7,2,5,5]
target = 9
print(s.largestNumber(cost,target))
#solution
'''
直接造字符串比较大小很容易出错，所以先统计出来能造出来的最大数字的长度，在去构造字符串
想成一个背包：
cost[i]是物品的体积，target是背包的体积，物品的价值=1
设数组dp,dp[i]为选用的数字消耗价值i时构成数字的长度,
初始时，dp[i]=-无穷大
但dp[0]=0,意味着选0个数位，构成的数字长度为0
dp[target]为数字的长度，dp[target]<0的话说明无法求初满足要求的数字，返回'0',否则构造字符串。
先说如何求初dp[target]
1. 便利cost数组中的每一个c;
2. 因为每个c可以使用多次，所以便利j [c,target]
分成两种情况，选还是不选当前价值为c的数位
选的话：dp[j]=dp[j-c]+1
不选的话:dp[j]=dp[j]
动态规划方程为:
dp[j]=max(dp[j],dp[j-c]+1)
求出数字的长度之后就开始构造这个数字吧
其实就是一个反向走回去的过程
还是便利cost中的每一个c
设j=target
循环从target网前便利，直到j=0
'''