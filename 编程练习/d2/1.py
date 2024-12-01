s=input()
alphas=[]
digits=[]
chinese_chars=[]
space_count=0
others=[]
for i in s:
	if i.isalpha():
		alphas.append(i)
	elif i.isdigit():
		digits.append(i)
	elif i.isspace():
		space_count+=1
	elif '\u4e00'<=i<='\u9fff':
		chinese_chars.append(i)
	else:
		others.append(i)
print('中文字符{}个，英文字母{}个，数字{}个，空格{}个，其他字符{}个'.format(len(chinese_chars),len(alphas),len(digits),space_count,len(others)))