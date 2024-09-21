                                                                                                                                                                                                                                                                                                                        # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def insertGreatestCommonDivisors(self, head):# -> Optional[ListNode]:
		def calc(x,y):
			if x>y:
				x,y=y,x
			while x>0:
				temp=x
				x=y%x
				y=temp
			return y
		now=head
		while now.next:
			new=ListNode(calc(now.val,now.next.val),now.next)
			now.next=new
			now=now.next.next
		return head