class Solution:
	def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
		def calc(ch):
			return ord(ch)-ord('a')+1
#			return ord(ch)&31
		n=len(s)
		hv=0
		tp=1
		for i in range(n-1,n-k-1,-1):
			hv=(hv*power+calc(s[i]))%modulo
			tp*=power
		ans=n-k if hv==hashValue else 0
		tp%modulo
#		tp=pow(power,k,modulo)
		for i in range(n-k-1,-1,-1):
			hv=(power*hv +calc(s[i])-tp*calc(s[i+k]))%modulo
			if hv==hashValue:
				ans=i
		return s[ans: ans+k]
#test entry
so=Solution()
s ="leetcode"
power =7
modulo =20
k =2
hashValue =0
print(so.subStrHash(s,power,modulo,k,hashValue))