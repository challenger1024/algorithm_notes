class Solution:
	def maximumEnergy(self, energy, k: int) -> int:
		n=len(energy)
		for i in range(k,n):
			energy[i]=max(energy[i-k]+energy[i],energy[i])
		return max(energy[n-1:n-k-1:-1])

#test entry
s=Solution()
energy = [5,2,-10,-5,1]
k = 3
#energy = [-2,-3,-1]k = 2
print(s.maximumEnergy(energy,k))