MOD = 10 ** 9 + 7
f = [1, 1, 2, 4]
g = [1, 1, 2, 4]
for _ in range(10 ** 5 - 3):
	f.append((f[-1] + f[-2] + f[-3]) % MOD)
	g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)
class Solution:
	def countTexts(self, pressedKeys: str) -> int:
		n=len(pressedKeys)
		ans = 1
		i=0
		while i < n:
			j=i
			while j<n and pressedKeys[i]==pressedKeys[j]:
				j+=1
			ans = ans * (g[j-i] if pressedKeys[i] in "79" else f[j-i]) % MOD
			i=j
		return ans

#test entry
s=Solution()
pressedKeys = "222222222222222222222222222222222222"
#pressedKeys = "22233"
print(s.countTexts(pressedKeys))