import numpy
WIDTH=80
HEIGHT=15
class Universe:
	def __init__(self):
		self.status_array=numpy.array([0]*(WIDTH*HEIGHT),dtype=int).reshape(HEIGHT,WIDTH)
	def show(self):
		print('\r{}'.format(self.status_array),end='')

a=Universe()
a.show()