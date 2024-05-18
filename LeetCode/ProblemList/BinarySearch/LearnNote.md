最长严格递增子序列`biset_left(nums,x)`(不含等号)
最长递增子序列`bisect_right(nums,x)`(含等号)
二分查找代码模版
#在有序数组nums中，查找target
l,r=0,len(nums)-1
loc=r#target可能存在的位置
while l<=r:
	mid=(l+r)//2
	if nums[mid]<=target:#l需要右移
		l=mid+1
	else:#r需要左移
		r=mid-1
		loc=mid

