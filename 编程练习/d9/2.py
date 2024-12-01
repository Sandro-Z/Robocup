class Point:
	def __init__(self,x,y,z=0):
		self.x=x
		self.y=y
		self.z=z
		print('创建了Point({},{},{})'.format(x,y,z))
	def __str__(self):
		return 'Point({}, {}, {})'.format(self.x,self.y,self.z)
	def __add__(self, other):
		if type(other)=='Vector':
			return Point(self.x+other.x,self.y+other.y,self.z+other.z)
		elif type(other)=='Point':
			raise TypeError
		else:raise TypeError
	def __sub__(self, other):
		return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
	def __del__(self):
		print('销毁了Point({}, {}, {})'.format(self.x,self.y,self.z))
	def __eq__(self, other):
		if type(self)!=type(other):return False
		if (self.x,self.y,self.z)==(other.x,other.y,other.z):return True
		else:return False
	def __lt__(self,other):
		if self.x**2+self.y**2+self.z**2<other.x**2+self.y**2+self.z**2:return True
		else: return False
	def __gt__(self, other):
		if self.x**2+self.y**2+self.z**2<other.x**2+self.y**2+self.z**2:return False
		else: return True

class Vector:
	def __init__(self,x,y,z=0):
		self.x=x
		self.y=y
		self.z=z
	def __str__(self):
		return 'Vector({}, {}, {})'.format(self.x,self.y,self.z)
	def __add__(self,other):
		return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
	def __sub__(self,other):
		return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
	def __eq__(self, other):
		if type(self)!=type(other): return False
		if (self.x,self.y,self.z)==(other.x,other.y,other.z):return True
		else:return False
	def __lt__(self,other):
		if self.x**2+self.y**2+self.z**2<other.x**2+self.y**2+self.z**2:return True
		else: return False
	def __gt__(self, other):
		if self.x**2+self.y**2+self.z**2<other.x**2+self.y**2+self.z**2:return False
		else: return True
	def __mul__(self,x):
		import math
		return Vector(self.x*math.cos(x/180*math.pi)-self.y*math.sin(x/180*math.pi),self.y*math.cos(x/180*math.pi)+self.x*math.sin(x/180*math.pi),self.z)
	def __truediv__(self, x):
		import math
		return Vector(self.x*math.cos(x/180*math.pi)+self.y*math.sin(x/180*math.pi),self.y*math.cos(x/180*math.pi)-self.x*math.sin(x/180*math.pi),self.z)

a=Point(1,2,3)
b=Point(4,5,6)
c=Point(1,2,3)
d=Vector(1,2,3)
e=Vector(4,5,6)
print(a==b,a>b,a<b,a==c,c==d,d<e,c==e)
print(a+b,a-b)
vec=Vector(3,4,0)
print(vec*90,vec/90)