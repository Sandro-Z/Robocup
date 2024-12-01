a=input()
times=eval(input())
ls=[]
for i in range(1,times+1):
	ls.append(a*i)
for i in range(len(ls)):
	ls[i]=eval(ls[i])
print(sum(ls))