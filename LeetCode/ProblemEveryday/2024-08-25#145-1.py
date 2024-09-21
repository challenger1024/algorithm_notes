#方法1：递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def postorderTraversal(self, root) :
		ans=[]
		def get(root):
			if root==None:
				return
			if root.left:
				get(root.left)
			if root.right:
				get(root.right)
			ans.append(root.val)
		get(root)
		return ans