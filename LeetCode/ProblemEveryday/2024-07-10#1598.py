class Solution:
	def minOperations(self, logs: List[str]) -> int:
		step=0
		for l in logs:
			flag=l.count('.')
			if flag==0:
				step+=1
			elif flag==2 and step!=0:
				step-=1
		return step