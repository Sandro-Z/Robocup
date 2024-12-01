import random
def gen_file():
	f=open('data.txt','w')
	for i in range(10):
		ls=[]
		for j in range(3):
			ls.append(str(random.randint(1,100)))
		f.write(','.join(ls)+'\n')
	f.close()
def read_file():
	g=open('data.txt','r').readlines()
	ls=g[2].strip().split(',')
	for i in range(len(ls)):
		ls[i]=eval(ls[i])
	print(max(ls),min(ls),sum(ls)/len(ls),ls[1])

if __name__ == '__main__':
	gen_file()
	read_file()