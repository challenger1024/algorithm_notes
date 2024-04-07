class Solution:
	def maximumCostSubstring(self, s: str, chars: str, vals) -> int:
		pre=0
		ans=pre
		for i,c in enumerate(s):
			val=0
			if c in chars:val=vals[chars.find(c)]
			else: val=ord(c)-ord('a')+1
			pre=max(pre+val,val)
			ans=max(ans,pre)
		return ans

#test entry

