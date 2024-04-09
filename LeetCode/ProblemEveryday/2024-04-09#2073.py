class Solution:
	def timeRequiredToBuy(self, tickets, k: int) -> int:
		ans=0
		num=tickets[k]#第k个人要买的票数
		for i,t in enumerate(tickets):
			if i<=k:
				ans+=min(t,num)#在第k个人前面，要买num张票的就加上num秒时间，少于num张票的就加上t秒时间
			else:
				ans+=min(t,num-1)#在第k个人后面的人，需要num-1秒时间或者t秒时间
		return ans