MOD=10**9+7
class Solution:
	def numDecodings(self, s: str) -> int:
		def num1(c):
			if c=='0':
				return 0
			return 9 if c=='*' else 1
		def num2(c1,c2):
			if c1==c2=='*':
				return 15
			if c1=='*':
				return 2 if c2<='6' else 1
			if c2=='*':
				return 9 if c1=='1' else (6 if c1=='2' else 0)
			return int(c1!='0' and (int(c1)*10+int(c2)<=26))
		n=len(s)
		a,b,c=0,1,0#b目前是前0 个字符的解码方案数
#后面a是dp[i-2],b是dp[i-1],c是dp[i]
		for i in range(1,n+1):
			c=b*(0 if s[i-1]=='0' else (9 if s[i-1]=='*' else 1))#也可以换成调用num1()函数传入s[i-1]
			if i>1:
				c+=a*(num2(s[i-2],s[i-1]))
			c%=MOD
			a=b
			b=c
		return c