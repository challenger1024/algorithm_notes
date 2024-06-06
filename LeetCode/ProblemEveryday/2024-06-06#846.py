class Solution:
	def isNStraightHand(self, hand, gs: int) -> bool:
		n=len(hand)
		if n%gs!=0:
			return False
		cnt=Counter(hand)
		hand.sort()
		for x in hand:
			if cnt[x]==0:
				continue
			for num in range(x,x+gs):
				if cnt[num]==0:
					return False
				cnt[num]-=1
		return True

