class Person:
	def __init__(self,name:str,age:int,gender:str):
		self.name=name
		self.age=age
		self.gender=gender
	def personinfo(self):
		print('姓名：{}，年龄：{}，性别：{}'.format(self.name,self.age,self.gender))

class Student(Person):
	def __init__(self,name:str,age:int,gender:str,college:str,class_:str):#class为关键字，不能用作变量名
		super().__init__(name,age,gender)
		self.college=college
		self.class_=class_
	def personinfo(self):
		super().personinfo()
		print('学院：{}，班级：{}'.format(self.college,self.class_))
	def __str__(self):
		return '姓名：{}，性别：{}，年龄：{}，学院：{}，班级：{}'.format(self.name,self.gender,self.age,self.college,self.class_)

student1=Student('Kobe',46,'Man!','Mamba college','Basketball 2301')
student1.personinfo()
print(student1)