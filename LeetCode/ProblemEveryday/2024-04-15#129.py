from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def sumNumbers(self, root: Optional[TreeNode]) -> int:
		q=deque()
		q.append(root)
		ans=0
		while q:
			now=q.popleft()
			if not now.left and not now.right:
				ans+=now.val
				continue
			if now.left:
				now.left.val=10*now.val+now.left.val
				q.append(now.left)
			if now.right:
				now.right.val=10*now.val+now.right.val
				q.append(now.right)
		return ans