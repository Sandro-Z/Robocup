a=open('copy_test.txt','r').readlines()
b=open('test.txt','r').readlines()
for i in range(len(a)):
	if b[i]!=a[i]:
		print(f'Line {i+1} is different.')
		print(f'Original: {a[i].strip()}')
		print(f'Modified: {b[i].strip()}')
	else:
		print(f'Line {i+1} is the same.')
print('test.txt 比copy_test.txt多一行"python"')