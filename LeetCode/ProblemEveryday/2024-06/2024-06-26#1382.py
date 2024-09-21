class Solution:
	def balanceBST(self, root: TreeNode) -> TreeNode:
		data=[]
		def save(root):
			if  root.left:
				save(root.left)
			data.append(root.val)
			if root.right:
				save(root.right)
		save(root)
		def build(i,j):
			mid=(i+j)//2
			o=TreeNode(data[mid])
			if i<=mid-1:
				o.left=build(i,mid-1)
			if j>=mid+1:
				o.right=build(mid+1,j)
			return o
		return build(0,len(data)-1)
