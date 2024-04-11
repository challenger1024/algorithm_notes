from collections import deque
class Solution:
	def deckRevealedIncreasing(self, deck):# -> List[int]:
		n=len(deck)
		index=deque(range(n))
		ans=[None]*n
		for card in sorted(deck):
			ans[index.popleft()]=card
			if index:
				index.append(index.popleft())
		return ans

#test entry
s=Solution()
deck = [17,13,11,2,3,5,7]
print(s.deckRevealedIncreasing(deck))