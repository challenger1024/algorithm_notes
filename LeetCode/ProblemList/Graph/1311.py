from collections import Counter,deque
class Solution:
	def watchedVideosByFriends(self, watchedVideos, friends, id: int, level: int):# -> List[str]:
		n=len(friends)
		q=deque([id])
		cnt=Counter()
		i=0
		vis=[False]*n
		vis[id]=True
		while q:
			t=len(q)
			for j in range(t):
				now=q.popleft()
				if i==level:
					for video in watchedVideos[now]:
						cnt[video]+=1
					continue
				for next in friends[now]:
					if not vis[next]:
						vis[next]=True
						q.append(next)
			i+=1
		ans=list(cnt.keys())
		ans.sort(key=lambda x:(cnt[x],x))
		return ans

#test entry
s=Solution()
#watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
#friends = [[1,2],[0,3],[0,3],[1,2]]
#id = 0
#level = 2
watchedVideos=[["xk","qvgjjsp","sbphxzm"],["rwyvxl","ov"]]
friends=[[1],[0]]
id=0
level=1
print(s.watchedVideosByFriends(watchedVideos,friends,id,level))