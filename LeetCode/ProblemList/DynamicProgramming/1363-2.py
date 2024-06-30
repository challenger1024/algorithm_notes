#腧穴
class Solution:
	def largestMultipleOfThree(self, nums: List[int]) -> str:
		f=[0]*10
		mod=[0]*3
		s=0
		for a in nums:
			f[a]+=1
			mod[a%3]+=1
			s+=a
		rmv,rest=0,0
		if s%3==1:
			rmv,rest=(1,1) if mod[1]>=1 else (2,2)
		elif s%3==2:
			rmv,rest=(2,1) if mod[2]>=1 else (1,2)
		ans=''
		for i in range(10):
			for j in range(f[i]):
				if rest>0 and rmv==i%3:
					rest-=1
				else:
					ans+=str(i)
		if len(ans)>0 and ans[-1]=='0':
			ans='0'
		return ans[::-1]