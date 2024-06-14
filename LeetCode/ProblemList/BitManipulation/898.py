class Solution:
	def subarrayBitwiseORs(self, arr: List[int]) -> int:
		n=len(arr)
		s=set()
		for i,a in enumerate(arr):
			s.add(a)
			for j in range(i-1,-1,-1):
				if arr[j]|a==arr[j]:
					break
				arr[j]|=a
				if arr[j] not in s:
					s.add(arr[j])
		return len(s)

#solution
'''
和#2411类似利用子数组和数字代表集合的关系
'''