class Solution:
	def jump(self, nums) -> int:
		steps,dis,end=0,0,0
		n=len(nums)
		for i in range(n-1):
			if dis>=i:
				dis=max(dis,i+nums[i])
				if end==i:
					steps+=1
					end=dis
		return steps