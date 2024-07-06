#广度优先搜索
from collections import deque
class Solution:
	def openLock(self, deadends: List[str], target: str) -> int:
		dead=set(deadends)
		vis=set()
		if target =='0000':
			return 0
		if '0000' in dead:
			return -1
		def num_pre(x):
			return '9' if x=='0' else str(int(x)-1)
		def num_next(x):
			return '0' if x=='9' else str(int(x)+1)
		def get(status):#生成一个可能是下一个密码字符串的列表，是由yield字段生成的
			s=list(status)
			for i in range(4):
				num=s[i]
				s[i]=num_pre(num)
				yield ''.join(s)
				s[i]=num_next(num)
				yield ''.join(s)
				s[i]=num
		q=deque([('0000',0)])
		vis.add('0000')
		while q:
			status,step=q.popleft()
			for next_status in get(status):
				if  next_status not in vis and next_status not in dead:
					if next_status==target:
						return step+1
					q.append((next_status,step+1))
					vis.add(next_status)
		return -1