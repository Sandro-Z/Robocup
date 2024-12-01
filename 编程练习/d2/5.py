def is_prime(n:int):
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True
for i in range(101,201):
	if is_prime(i):
		print(i, end=" ")