runyearmonthdaysls=[31,29,31,30,31,30,31,31,30,31,30,31]
notrunyearmonthdaysls=[31,28,31,30,31,30,31,31,30,31,30,31]

def decide_is_run_year(year):
	if (year%4==0 and year%100!=0) or year%400==0:return True
	else: return False

#输入格式：YYYY-M-D
date=input()
ls=date.split('-')
if decide_is_run_year(eval(ls[0])):
	print(sum(runyearmonthdaysls[:eval(ls[1])-1])+eval(ls[2]))
else:
	print(sum(notrunyearmonthdaysls[:eval(ls[1])-1])+eval(ls[2]))