class Solution:
	def numberOfSubarrays(self, nums: List[int], k: int) -> int:
		odd=[-1]
		for i,num in enumerate(nums):
			if num%2==1:
				odd.append(i)
		odd.append(len(nums))
		ans=0
		for i in range(1,len(odd)-k):
			ans+=(odd[i]-odd[i-1])*(odd[i+k]-odd[i+k-1])
		return ans