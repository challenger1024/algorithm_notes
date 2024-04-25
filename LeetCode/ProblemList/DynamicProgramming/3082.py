mod=10**9+7
class Solution:
	def sumOfPower(self, nums, k: int) -> int:
		n=len(nums)
		dp=[[0]*(n+1) for _ in range(k+1)]
		dp[0][0]=1
		for i in range(1,n+1):
			num=nums[i-1]
			for x in range(k,num-1,-1):
				for j in range(1,i+1):
					dp[x][j]+=dp[x-num][j-1]
#		print(dp)
		ans=0
		p=1
		for j in range(n,0,-1):
			ans=(ans+dp[k][j]*p)%mod
			p*=2
		return ans

#test entry
s=Solution()
nums=[1,2,3]
k=3
print(s.sumOfPower(nums,k))

#solution
'''
设子序列为subse,对于数组中的nums[i],可以有两种选择：
1.选nums[i]构成子序列
2.不选nums[i]构成子序列
对于每一个子序列subse，又有，是否选择subse[j]构成和为k的更小子序列subsubse。
设状态dp[i][k][j]为第i个数字，和为k时长度为j的序列的长度，
那么，长度为j的序列能为答案做出的贡献为:2**(len(nums)-dp[i][k][j])

'''