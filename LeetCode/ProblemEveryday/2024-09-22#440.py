class Solution:
	def findKthNumber(self, n: int, k: int) -> int:
		def getNum(cur):
			ret,first,last=0,cur,cur
			while first<=n:
				ret+=min(last,n)-first+1
				first*=10
				last=last*10+9
			return ret
		k-=1
		cur =1
		while k:
			num=getNum(cur)
			if num<=k:
				cur+=1
				k-=num
			else:
				cur*=10
				k-=1
		return cur