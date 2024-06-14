class Solution:
	def smallestSubarrays(self, nums: List[int]) -> List[int]:
		n=len(nums)
		ans=[0]*n
		for i,a in enumerate(nums):
			ans[i]=1
			for j in range(i-1,-1,-1):
				if nums[j]|a!=nums[j]:
					nums[j]|=a
					ans[j]=i-j+1
				else:
					break
		return ans

#solution
'''
利用前缀和+数字和集合的关系的思路求解
两重循环
外层循环便利nums中的每个元素a
对于每一个a=nums[i],进行内层循环
倒序便利a左侧的每个nums[j]
如果nums[j]|a>nums[j],说明a必须加入到nums[j]为开头的子数组的后面才能保证这个子数组或值最大
因此更新ans[j]
如果nums[j]|a==nums[j],说明不需要将a添加到nums[j]为开头的子数组中，且nums[j]左侧开头的那些数组也不需要考虑是否添加a到末尾
这是因为每个nums[j]都是nums[j-1]的子集，a|nums[j]=nums[j]说明nums[j]这个集合中已经存在a,所以无需添加a进去。

'''