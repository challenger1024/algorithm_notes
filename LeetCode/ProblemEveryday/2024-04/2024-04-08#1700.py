from collections import Counter
class Solution:
	def countStudents(self, students, sandwiches) -> int:
		n=len(students)
		cnt=Counter(students)
		for s in sandwiches:
			if cnt[s]>0:
				cnt[s]-=1
			else: break
		return cnt[0]+cnt[1]

#test entry
s=Solution()
#students = [1,1,0,0]
#sandwiches = [0,1,0,1]
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(s.countStudents(students,sandwiches))