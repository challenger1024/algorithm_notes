# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
		stack=[]
		while head:
			head.val*=2
			stack.append(head)
			head=head.next
		x=0
		while stack:
			if head :
				x=head.val//10
				head.val%=10
			stack[-1].next=head
			head=stack[-1]
			head.val+=x
			stack.pop()
		dummy=ListNode(0,head)
		if head.val>=10:
			dummy.val+=head.val//10
			head.val%=10
			return dummy

		return head