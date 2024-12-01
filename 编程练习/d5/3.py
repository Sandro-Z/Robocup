import random


def gen_random_file(filename):
	f=open(filename,'w')
	for i in range(100000):
		f.write(str(random.randint(1,100))+'\n')
	f.close()

gen_random_file('data.txt')
