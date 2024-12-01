num_list=list(range(10))
print(num_list)
for i in range(4):
	num_list.append(num_list.pop(0))
	print(num_list)