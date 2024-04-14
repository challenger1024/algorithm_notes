from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
		q=deque()
		q.append(root)
		ans=0
		while q:
			n=len(q)
			for i in range(n):
				now=q.popleft()
				if now.left :
					if not now.left.left and not now.left.right:
						ans+=now.left.val
					else:
						q.append(now.left)
				if now.right:
					q.append(now.right)
		return ans