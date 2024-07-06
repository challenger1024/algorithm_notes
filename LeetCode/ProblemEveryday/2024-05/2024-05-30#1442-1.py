class Solution:
	def countTriplets(self, arr) -> int:
		n=len(arr)
		ans=0
		subs=[0]*(n+1)
		for i,a in enumerate(arr):
			subs[i+1]^=a
			subs[i+1]^=subs[i]
		for i in range(1,n+1):
			for j in range(i+1,n+1):
				a=subs[j-1]^subs[i-1]
				for k in range(j,n+1):
					b=subs[k]^subs[j-1]
					if a==b:
#						print(f'i={i-1},j={j-1},k={k-1},a={a},b={b}')
						ans+=1
		return ans

#test entry
s=Solution()
arr=[2,3,1,6,7]
print(s.countTriplets(arr))