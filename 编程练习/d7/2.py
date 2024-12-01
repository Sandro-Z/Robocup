import string,random
all_chars=list(string.printable[:-5])
output=open('test.txt', 'w')
i=eval(input('输入整数'))
try:
	for j in range(i):
		for k in range(10):#默认每行10个字符
			output.write(random.choice(all_chars))
		output.write('\n')
	output.close()
except TypeError:
	print('指定的行数必须是正整数')

def copy():
	f=open('copy_test.txt','w')
	i=open('test.txt','r')
	for line in i:
		f.write(line)
	f.close()
copy()