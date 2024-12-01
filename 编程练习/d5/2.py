def odd_index(ls):
	new_ls=[]
	for i in range(len(ls)):
		if i%2!=0:
			new_ls.append(ls[i])
	return new_ls