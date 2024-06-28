#morris 便利
class Solution:


    def bstToGst(self, root: TreeNode) -> TreeNode:


        def getSuccessor(node: TreeNode) -> TreeNode:


            succ = node.right

            while succ.left and succ.left != node:


                succ = succ.left

            return succ

        

        total = 0


        node = root



        while node:


            if not node.right:


                total += node.val

                node.val = total

                node = node.left

            else:


                succ = getSuccessor(node)


                if not succ.left:


                    succ.left = node

                    node = node.right

                else:


                    succ.left = None


                    total += node.val

                    node.val = total

                    node = node.left



        return root