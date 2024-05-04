class Solution:
	def numRescueBoats(self, people, limit: int) -> int:
		n=len(people)
		people.sort()
		ans=0
		l,r=0,n-1
		while l<=r:
			if people[l]+people[r]<=limit:
				l+=1
			ans+=1
			r-=1
		return ans

#test entry
s=Solution()
people=[3,2,2,1]
limit=3
print(s.numRescueBoats(people,limit))