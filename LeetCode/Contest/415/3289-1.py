#解法1：哈希集合
class Solution:
	def getSneakyNumbers(self, nums: List[int]) -> List[int]:
		cnt=Counter(nums)
		ret=[]
		for a in nums:
			if cnt[a]==2:
				ret.append(a)
		ret=list(set(ret))
		return ret