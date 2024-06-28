
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            ans+=num%3 if num%3<=1 else 1
        return ans