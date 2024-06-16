class Solution:
	def longestString(self, x: int, y: int, z: int) -> int:
		@cache
		def dfs(x,y,z,k):
			if k==0:
				return dfs(x,y-1,z,1)+2 if y else 0
			res1=dfs(x-1,y,z,0)+2 if x else 0
			res2=dfs(x,y,z-1,2)+2 if z else 0
			return max(res1,res2)
		return max(dfs(x,y,z,0),dfs(x,y,z,1))

#solution
'''
记忆化搜索
`dfs(x,y,z,k)`其中k代表当前的结尾是0:aa,1:bb,2:ab
aa后面只能街bb
bb后面可以接aa和ab
ab后面只能接aa
'''