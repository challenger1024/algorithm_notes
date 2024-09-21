#马拉车算法找最长前缀回文串
class Solution:
	def shortestPalindrome(self, s: str) -> str:
		n=len(s)
		t='#'+'#'.join(s)+'#'
		m=len(t)
		def search_arm(l,r):#扩展臂长
			while l>=0 and r<m and t[l]==t[r]:
				l-=1
				r+=1
			return (r-l-2)//2
		right,centre,end=-1,0,0
		arms=[]
		for i in range(m):
			if right>=i:#此时可以利用已有的信息判断当前的回文串有多长
				a=2*centre-i
				min_a=min(arms[a],right-i)
				arm=search_arm(i-min_a,i+min_a)
			else:
				arm=search_arm(i,i)
			arms.append(arm)
			if i+arm>right:
				right=i+arm
				centre=i
				if right>=centre*2:
					end=(right-1)//2
#				else:
#					break
		#print(end)
		#print(s[:end+1])
		return s[-1:end-n:-1]+s

so=Solution()
s='aacecaaa'
#s="abcd"
print(so.shortestPalindrome(s))