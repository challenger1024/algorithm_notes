class Solution:
	def maximumLengthSubstring(self, s: str) -> int:
		def cal(c1,c2):
			return ord(c1)-ord(c2)
		cnt=[0]*26
		l=0
		ans=0
		for i,c in enumerate(s):
			cnt[cal(c,'a')]+=1
			if cnt[cal(c,'a')]<=2:
				ans=max(i-l+1,ans)
			while cnt[cal(c,'a')]>2:
				cnt[cal(s[l],'a')]-=1
				l+=1
		return ans

#test entry
so=Solution()
s = "aaaa"
#s = "bcbbbcba"
print(so.maximumLengthSubstring(s))
#solution
'''
滑动窗口
'''