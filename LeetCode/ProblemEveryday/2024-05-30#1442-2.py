class Solution:
	def countTriplets(self, arr) -> int:
		n=len(arr)
		ans=0
		subs=[0]*(n+1)
		for i,a in enumerate(arr):
			subs[i+1]^=a
			subs[i+1]^=subs[i]
		for i in range(1,n+1):
			for k in range(i+1,n+1):
				if subs[i-1]==subs[k]:
					ans+=k-i
		return ans

#test entry
s=Solution()
arr=[2,3,1,6,7]
print(s.countTriplets(arr))