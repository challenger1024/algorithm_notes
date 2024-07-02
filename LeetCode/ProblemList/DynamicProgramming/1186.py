class Solution:
	def maximumSum(self, arr: List[int]) -> int:
		x=float('-inf')#上一个没删除元素的子数组和
		y=float('-inf')#上一个删除了一个元素的子数组和
		ans=float('-inf')
		for a in arr:
			y=x if x>y+a else y+a
			x=a+(x if x>0 else 0)
			ans=max(ans,x,y)
		return ans