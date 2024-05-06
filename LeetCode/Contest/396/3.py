from collections import Counter
class Solution:
	def minAnagramLength(self, s: str) -> int:
		n=len(s)
		cnt=Counter(s)
		k=len(cnt.keys())
		idx=0
		while idx+k<=n:
			rtemp=Counter(s[idx:idx+k])
			ltemp=Counter(s[idx:idx+k])
			i,j=idx-1,idx+k
			while i>=0 and len(ltemp.keys()) < k:
				ltemp[s[i]]+=1
				i-=1
			while j<n and len(rtemp.keys()) < k:
				rtemp[s[j]]+=1
				j+=1
			ans=float('inf')
			if len(ltemp.keys())==k :
				ans=min(ans,min(idx+k,n)-max(0,i))
			if len(rtemp.keys())==k:
				ans=min(ans,j-idx)
			return ans
			idx+=k
		return k

#test entry
s=Solution()
w="twpezw"
w='jjj'
print(s.minAnagramLength(w))