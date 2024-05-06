# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
		stack=[]
		while head is not None:
			stack.append(head)
			head=head.next
		while stack:
			if head is None or stack[-1].val>=head.val:
				stack[-1].next=head
				head=stack[-1]
			stack.pop()
		return head