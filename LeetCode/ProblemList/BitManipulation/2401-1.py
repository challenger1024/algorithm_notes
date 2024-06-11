#枚举
class Solution:
	def longestNiceSubarray(self, nums: List[int]) -> int:
		ans=0
		for i,sub in enumerate(nums):
			j=i-1
			while j>=0 and (nums[j]&sub)==0:
				sub|=nums[j]#将nums[j]并入集合sub,后面进行与运算也不会受到影响，因为每个数字设置位都不同
				j-=1
			ans=max(ans,i-j)
		return ans

#solution
'''
要使两个数字与运算=0，就要使这两个数字a和b中设置位的位置不同。
设置位是数字二进制表示中1的位置；
因为nums[i]的范围在10**9之内，最大只有2**29,所以子数组长度最多只有30；
据此，外层循环枚举右端点，
内层循环枚举左端点，内层循环成立条件为:sub&nums[j]=0
sub每次遇到可延加入到尾部的nums[j],就将nums[j]或运算到sub中，这是因为因为设置位不同，将每一个子数组中二进制表示中1的位置都并入集合中，方便后面的与运算判断是否有1的位置重复。
每次内层循环结束时更新答案。

'''