def fibonacci_repeat(n):
	if n<3:
		return 1
	res,pre,cur=0,1,1
	for _ in range(n-2):
		res=pre+cur
		pre=cur
		cur=res
	return res

for i in range(1,21):
	print(fibonacci_repeat(i),end=',')