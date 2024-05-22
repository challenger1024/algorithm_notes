class Solution:
	def extend(self,s,left,right):
		n=len(s)
		while left>=0 and right <n and s[left]==s[right]:
			left-=1
			right+=1
		return (right-left-2)//2
	def longestPalindrome(self, s: str) -> str:
		s='#'+'#'.join(s)+'#'
		arms=[]
		start,end=0,-1
		right=-1
		j=-1
		for i in range(len(s)):
			if right>=i:
				a=2*j-i
				min_a=min(arms[a],right-i)
				arm=self.extend(s,i-min_a,i+min_a)
			else:
				arm=self.extend(s,i,i)
			arms.append(arm)
			if i+arm>right:
				right=i+arm
				j=i
			if arm>(end-start-1)//2:
				start=i-arm
				end=i+arm
		return s[start+1:end+1:2]

#solution
'''
使用Manacher算法找最长的回文字符串
拿到一个字符串
1. 将字符串长度改成奇数，具体操作是在字符串的每两个字母之间和字符串两端加上一个字符，这里我用'#';
s='#'+'#'.join(s)+'#'
2. 设一个数组arm,arm[i]表示以s[i]为中心，长度为2*length+1的回文字符串的length值;

'''