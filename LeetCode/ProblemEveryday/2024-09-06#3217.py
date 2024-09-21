#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
	def modifiedList(self, nums, head):# -> Optional[ListNode]:
		rm=set(nums)
		dummy=ListNode(0,head)
		hand=dummy
		while hand.next:
			if hand.next.val in rm:
				hand.next=hand.next.next
			else:
				hand=hand.next
		return dummy.next