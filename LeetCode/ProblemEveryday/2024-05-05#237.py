# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def deleteNode(self, node):
		hand=node
		hand.val=hand.next.val
		hand.next=hand.next.next

#solution
'''
交换当前节点和下一个节点的值，删除掉下一个节点
因为无法访问node的上一个节点，所以不能直接删除node
'''