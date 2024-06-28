
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        x=1
        flag=0
        for a in nums:
            if x!=a:
                ans+=1
                x=a
                flag^=1
        return ans