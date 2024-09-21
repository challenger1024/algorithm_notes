class Solution:
	def maxSatisfied(self, customers, grumpy, minutes: int) -> int:
		n=len(customers)
		l,r,temp=0,0,0
		ans=0
		i,j=0,minutes-1
		for i,c in enumerate(customers):
			if grumpy[i]==1:
				temp+=c
			if i>=minutes and grumpy[i-minutes]==1:
				temp-=customers[i-minutes]
#			if i==minutes-1:
#				ans=temp
			if i>=minutes-1 and temp>ans:
				ans=temp
				r=i
				l=i-minutes+1
		ans=sum(customers[max(l,0):r+1])
#		print(r)
		for i,c in enumerate(customers):
			if l<=i<=r or grumpy[i]==1:
				continue
			ans+=c
		return ans

#test entry
s=Solution()
customers=[2,6,6,9]
grumpy=[0,0,1,1]
minutes=1
#customers=[10,4]
#grumpy=[0,1]
#minutes=2
print(s.maxSatisfied(customers,grumpy,minutes))