def calculate(*args):
	ls=[]
	for i in range(len(args)):
		if i>sum(args)/len(args):
			ls.append(args[i])
	return sum(args)/len(args),ls