#记忆化搜索
MOD=10**9+7
class Solution:
	def numberOfPermutations(self, n: int, req: List[List[int]]) -> int:
		q=[-1]*n
		q[0]=0
		for end,cnt in req:
			q[end]=cnt
		if q[0]:#只有一个元素的时候只能有0个逆序对，如果$q[0]!=0$,直接返回$0$
			return 0
		@cache
		def dfs(i,j):#状态:前i个元素有j个逆序对
			if i==0:#转移边界，当前面只有0个元素时，这个排列可以累加到答案中
				return 1
			r=q[i-1]
			if r>=0:
#如果r>j,说明前i-1个元素中恰好有r个逆序对，而前i个元素中有j<r个逆序对，相互矛盾，所以r必须<j
#如果j-i>r:前i 个元素有j个逆序对，前i-1个元素至少有j-i个逆序对，也是娶不到r的，所以也返回0
#如果上述条件都没有出现，则将r作为j传入到函数中继续记忆化搜索
				return dfs(i-1,r) if r<=j <=i+r else 0
			return sum(dfs(i-1,j-k) for k in range(min(i,j)+1))%MOD#如果q[i-1]=-1,那么当前索引位置没有逆序对数量要求，循环k带入其中求解,min(i,j)是因为第i个数字和前i-1个数字至多形成i个逆序对
		return dfs(n-1,q[-1])#答案是前n-1个数字有q[n-1]个逆序对