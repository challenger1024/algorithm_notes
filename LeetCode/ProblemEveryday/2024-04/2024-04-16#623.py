from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
		if depth==1:
			now=TreeNode(val,root,None)
			return now
		q=deque()
		q.append(root)
		d=0
		while q:
			d+=1
			n=len(q)
			for i in range(n):
				now=q.popleft()
				if d==depth-1:
					templeft=TreeNode(val,now.left,None)
					tempright=TreeNode(val,None,now.right)
					now.left=templeft
					now.right=tempright
				else:
					if now.left:
						q.append(now.left)
					if now.right:
						q.append(now.right)
			if d==depth-1:
				break
		return root