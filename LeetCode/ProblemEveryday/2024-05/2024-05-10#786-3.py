class Solution:
	def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
		n=len(arr)
		left,right=0.0,1.0
		while True:
			mid=(left+right)/2
			i,count=-1,0
			x,y=0,1
			for j in range(1,n):
				while arr[i+1]/arr[j] < mid:
					i+=1
					if arr[i]*y>arr[j]*x:
						x,y=arr[i],arr[j]
				count+=i+1
			if count==k:
				return [x,y]
			if count<k:
				left=mid
			else:
				right=mid

#solution
'''
二分查找
设第k个分数小于某个0到1之间的实数mid.
用count记录小于mid的分数的数量
如果count==k,那么当前的这个分数就是答案
如果count<k,说明mid选小了，则令left=mid,重新找一遍
如果count>k,说明mid找大了，令right=mid,再找一遍
'''