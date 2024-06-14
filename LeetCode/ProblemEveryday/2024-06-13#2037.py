class Solution:
	def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
		seats.sort()
		students.sort()
		ans=0
		for (student,seat) in zip(students,seats):
			ans+=abs(student-seat)
		return ans
