from collections import Counter
class Solution:
	def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
		letters_cnt=Counter(letters)
		score=dict(zip(ascii_lowercase,score))
		ans=0
		def dfs(i,total):
			if i<0:
				nonlocal ans
				ans=max(ans,total)
				return 
			dfs(i-1,total)
			w=0
			for j,c in enumerate(words[i]):
				if letters_cnt[c]==0:
					for h in words[i][:j]:
						letters_cnt[h]+=1
					return
				w+=score[c]
				letters_cnt[c]-=1
			dfs(i-1,total+w)
			for c in words[i]:
				letters_cnt[c]+=1
		dfs(len(words)-1,0)
		return ans