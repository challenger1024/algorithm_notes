#枚举中间点
class Solution:
	def numTeams(self, rating: List[int]) -> int:
		ans=0
		n=len(rating)
		for i in range(1,n-1):
			smalll=smallr=bigl=bigr=0
			for j in range(i):
				if rating[j]<rating[i]:
					smalll+=1
				if rating[j]>rating[i]:
					bigl+=1
			for j in range(i+1,n):
				if rating[j]<rating[i]:
					smallr+=1
				if rating[j]>rating[i]:
					bigr+=1
			ans+=smalll*bigr+bigl*smallr
		return ans

#solution
'''
枚举中间点，对于每个撞见点，计算其左右两侧满足条件的点的数量。
'''