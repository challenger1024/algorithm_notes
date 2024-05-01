class Solution:
	def evenOddBit(self, n: int) -> List[int]:
		even,odd=0,0
		i=0
		while (1<<i)<=n:
			if ((1<<i)^n)!=n:
				if i%2:
					odd+=1
				else:
					even+=1
			i+=1
		return [even,odd]