# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	m=0
	def distributeCoins(self, root: Optional[TreeNode]) -> int:
		m=0
		def dfs(root):
			if  root is None:
				return 0
			l,r=0,0
			if root.left is not None:
				l=dfs(root.left)
			if root.right is not None:
				r=dfs(root.right)
			self.m+=abs(l)+abs(r)
			return l+r+root.val-1
		dfs(root)
		return self.m

