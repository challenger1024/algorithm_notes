mod=10**9+7
class Solution:
	def kConcatenationMaxSum(self, arr, k: int) -> int:
		n=len(arr)
		pre=0
		maxSum=pre
		for num in arr*min(2,k):
			pre=max(pre+num,num)
			maxSum=max(maxSum,pre)
		if k<=2:return maxSum%mod
		else:return (maxSum+max(0,sum(arr))*(k-2))%mod



#test entry
s=Solution()
arr=[-5,-2,0,0,3,9,-2,-5,4]
k=5
#arr = [-1,-2]
#k = 7
#arr = [1,-2,1]
#k = 5
#arr = [1,2]
#k = 3
print(s.kConcatenationMaxSum(arr,k))