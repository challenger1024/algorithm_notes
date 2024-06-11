class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=0
        s=x^y
        while s:
            s&=s-1
            ans+=1
        return ans

#solution
'''
x^y的二进制表示中，1代表x和y相应位置数字相同,0表示x和y相应位置数字不同，
所以，x^y的二进制表示中，1的个数及为x何y的汉明距离。
'''