#解法3：腧穴
#出现两次的两个数字a,b的和a+b=sum(nums)-n*(n-1)/2
#a^2+b^2=nums中的每一项的平方和-数列(0到n-1)的 每一项的平方和
#题目变成解二元二次方程组，求直线和圆的一个焦点
class Solution:
	def getSneakyNumbers(self, nums: List[int]) -> List[int]:
		a,b=0,0
		n=len(nums)-2
		for i,x in enumerate(nums):
			if i<n:
				a-=i
				b-=i*i
			a+=x
			b+=x*x
		x=int((a+sqrt(2*b-a*a))/2)
		return [x,a-x]