class Solution:
	def hasTrailingZeros(self, nums: List[int]) -> bool:
		if len(nums)<2:
			return False
		ans=0
		for a in nums:
			ans+=1 if a&1==0 else 0
			if ans>=2:
				return True
		return False

#solution
'''
要想or值中有尾随0，nums中至少要有两个元素的二进制表示中有尾随0，据此便利nums即可。
'''