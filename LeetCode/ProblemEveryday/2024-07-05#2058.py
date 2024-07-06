# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
		idx=[]
		front=head.next
		back=head
		i=0
		while front.next:
			i+=1
			if (back.val>front.val and front.next.val>front.val) or (back.val<front.val and front.next.val<front.val):
				idx.append(i)
			front=front.next
			back=back.next
		if len(idx)<2:
			return [-1,-1]
		m=inf
		for i in range(len(idx)-1):
			m=min(m,idx[i+1]-idx[i])
		return [m,idx[-1]-idx[0]]