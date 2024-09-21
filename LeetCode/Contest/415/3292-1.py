from random import randint

MOD = 1_070_777_777
BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE

class Solution:
	def minValidStrings(self, words, target: str) -> int:
		n=len(target)
		pow_base=[1]+[0]*n
		pre_hash=[0]*(n+1)#前缀哈希值
		for i,c in enumerate(target):
			pow_base[i+1]=pow_base[i]*BASE%MOD
			pre_hash[i+1]=(pre_hash[i]*BASE+ord(c))%MOD#计算多项式哈希
		def sub_hash(l,r):#计算子串[l,r)的]哈希值
			return (pre_hash[r]-pre_hash[l]*pow_base[r-l])%MOD
		max_len=max(map(len,words))
		sets=[set() for _ in range(max_len)]
		for w in words:
			h=0
			for j,c in enumerate(w):
				h=(h*BASE+ord(c))%MOD
				sets[j].add(h)
		ans=0
		cur_r=0
		next_r=0
		for i in range(n):
			