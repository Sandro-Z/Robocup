s=''
ls=[]
for a in range(1,5):
	for b in range(1,5):
		for c in range(1,5):
			for d in range(1,5):
				s+=str(a)
				s+=str(b)
				s+=str(c)
				s+=str(d)
				if s not in ls:
					ls.append(s)
				s=''
def decide_if_not_unique(s:str):
	for i in s:
		if s.count(i)>1:
			return False
	return True
new_ls=[]
for item in ls:
	if decide_if_not_unique(item):
		new_ls.append(item)
print(new_ls)
print(len(new_ls))