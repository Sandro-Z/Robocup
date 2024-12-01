import os
import random
def main():
	os.chdir('img')
	ls=os.listdir()
	print(len(ls))
	new_ls=[]
	while len(new_ls)<50:
		x=random.choice(ls)
		if x not in new_ls:
			new_ls.append(x)
	print(len(new_ls))
	for i in new_ls:
		os.rename(i,i+'.jpg')
main()