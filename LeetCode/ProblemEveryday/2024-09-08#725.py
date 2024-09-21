import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def splitListToParts(self, head, k: int):# -> List[Optional[ListNode]]:
		n=0
		ans=[None for _ in range(k)]
		hand=head
		while hand:
			n+=1
			hand=hand.next
		i=0
		now=head
		q,remainder=n//k,n%k
		while i<k and now:
			ans[i]=now
			l=q+(1 if i<remainder else 0)
			for _ in range(l-1):
				now=now.next
			temp=now
			now=now.next
			temp.next=None
			i+=1
		return ans