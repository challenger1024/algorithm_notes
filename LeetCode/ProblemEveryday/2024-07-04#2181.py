# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
		dummy=tail=ListNode()
		cur=head.next
		s=0
		while cur:
			if cur.val!=0:
				s+=cur.val
			else:
				node=ListNode(s)
				tail.next=node
				tail=tail.next
				s=0
			cur=cur.next
		return dummy.next