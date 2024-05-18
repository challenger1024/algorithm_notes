# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
		def dfs(root):
			if root.left:
				root.left=dfs(root.left)
			if root.right:
				root.right=dfs(root.right)
			if root.left==None and root.right==None and root.val==target:
				return None
			return root
		return dfs(root)