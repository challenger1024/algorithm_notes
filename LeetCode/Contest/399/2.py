class Solution:
	def compressedString(self, word: str) -> str:
		ans=''
		n=len(word)
		last=word[0]
		now,pre=1,0
		while now<n:
			if word[now]!=last or now-pre==9:
				ans+=str(now-pre)+last
				last=word[now]
				pre=now
			now+=1
		if now-pre>=1:
			ans+=str(now-pre)+last
		return ans

#test entry
s=Solution()
word='abcde'
#word = "aaaaaaaaaaaaaa"
print(s.compressedString(word))