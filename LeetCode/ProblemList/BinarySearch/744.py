class Solution:
	def nextGreatestLetter(self, letters: List[str], target: str) -> str:
		if letters[-1]<=target:
			return letters[0]
		l,r=0,len(letters)-1
		while l<=r:
			mid=(l+r)//2
			if ord(letters[mid])<ord(target)+1:
				l=mid+1
			else:
				r=mid-1
		return letters[l]