import os,random

def genfile():
	os.mkdir('img')
	os.chdir('img')
	for i in range(100):
		f=open(str(random.randint(1,9999)),'w');f.close
genfile()