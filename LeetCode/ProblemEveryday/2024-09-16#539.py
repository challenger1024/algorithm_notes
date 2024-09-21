class Solution:
	def findMinDifference(self, timePoints) -> int:
		def getMinutes(t):
			return 60*((ord(t[0])-ord('0'))*10+ord(t[1])-ord('0'))+10*(ord(t[3])-ord('0'))+ord(t[4])-ord('0')
		if len(timePoints)>=1440:
			return 0
		timePoints.sort()
		ans=float('inf')
		t0=getMinutes(timePoints[0])
		pre=t0
		for i in range(1,len(timePoints)):
			now=getMinutes(timePoints[i])
			ans=min(ans,now-pre)
			ans=min(ans,t0+1440-now)
			pre=now
		return ans