#滑动窗口
class Solution:
	def longestNiceSubarray(self, nums: List[int]) -> int:
		ans=0
		l=0
		sub=0#子数组
		for r,a in enumerate(nums):
			while sub&a:#如果sub&a!=0,说明此时a不能加入到子数组中，窗口左边界右移
				sub^=nums[l]#将nums[l]从sub中取出来，抑或操作在集合中是获得差集
				l+=1
			sub|=a#将窗口右边界向右扩展
			ans=max(ans,r-l+1)
		return ans