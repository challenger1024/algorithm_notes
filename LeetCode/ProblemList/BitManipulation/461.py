class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=0
        s=x^y
        while s:
            s&=s-1
            ans+=1
        return ans