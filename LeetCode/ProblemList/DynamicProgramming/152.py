class Solution:
	def maxProduct(self, nums) -> int:
		n=len(nums)
		mi,ma=nums[0],nums[0]
		ans=max(mi,ma)
		for num in nums[1:n]:
			temp=ma
			ma=max(num,ma*num,mi*num)#最大值可能的三种情况，当前num,ma*num,min*num
			mi=min(mi*num,num,temp*num)#最小值也有三种情况当前的num,ma*num,mi*num
			ans=max(ans,ma,mi)#答案取最大值
		return ans

#test entry
s=Solution()
nums=[-1,-2,-9,-6]
#nums = [-2,0,-1]
#nums = [2,3,-2,4]
print(s.maxProduct(nums))
#Solution
'''因为数组中有正数和复数，数组的最大乘机可能是有两个复数相乘得到的，所以要记录乘机的最小值。
'''