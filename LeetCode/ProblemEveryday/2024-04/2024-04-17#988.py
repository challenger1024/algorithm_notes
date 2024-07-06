# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
		def get(num):
			return chr(97+num)
		self.ans='~'
		def dfs(root,ret):
			if not root.left and not root.right:
				res=get(root.val)+ret[::-1]
				if res<self.ans:self.ans=res
				return
			ret+=get(root.val)
			if root.left:dfs(root.left,ret)
			if root.right: dfs(root.right,ret)
			return
		dfs(root,'')
		return self.ans