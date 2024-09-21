# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def spiralMatrix(self, m: int, n: int, head):# -> List[List[int]]:
		matrix=[[-1]*n for _ in range(m)]
		dirs=[[0,1],[-1,0],[0,-1],[1,0]]
		i,j=0,0
		d=0
		while head:
			matrix[i][j]=head.val
			head=head.next
			while head and (not 0<=i+dirs[d][0]<m or not 0<=j+dirs[d][1]<n or matrix[i+dirs[d][0]][j+dirs[d][1]]!=-1):
				d+=1
				d%=4
			i,j=i+dirs[d][0],j+dirs[d][1]
#			print(f'i={i},j={j}')
		return matrix

s=Solution()
m=3
n=5
nums=[3,0,2,6,8,1,7,9,4,2,5,5,0]
dummy=ListNode(0,None)
head=dummy
for x in nums:
	head.next=ListNode(x,None)
	head=head.next
print(s.spiralMatrix(m,n,dummy.next))