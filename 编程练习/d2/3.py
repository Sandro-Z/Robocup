after=10/(2**10)
all_length=0
for i in range(9):
	length=10/2**(i+1)
	all_length+=length*2
all_length+=after
print(all_length)
print(after)