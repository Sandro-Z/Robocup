def decide_is_run_year(year):
	if (year%4==0 and year%100!=0) or year%400==0:return True
	else: return False
print(decide_is_run_year(eval(input())))