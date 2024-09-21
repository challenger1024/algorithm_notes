#埃氏筛
import time
import sys
import os

class solution:
	def main(self):
		n=10**7
		k=0
		ori=[True]*(n+1)
		i=2
#		for i in range(2,n+1):
		while i<n+1:
			if ori[i]:
				k+=1
				j=i*i
				#for j in range(i+i,n+1,i):
				while j<n+1:
					ori[j]=False
					j+=i
			i+=1
		print(k)

s=solution()
start=time.time()
s.main()
end=time.time()
print(end-start)