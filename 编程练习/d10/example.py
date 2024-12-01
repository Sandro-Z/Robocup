import random
import sys
import time
import os


class Universe:
	def __init__(self,height=30,width=100):
		self.height=height
		self.width=width
		# 初始化两个矩阵，一个保存当前状态，一个保存前一状态
		self.current_grid=[[' ' for _ in range(self.width)] for _ in range(self.height)]
		self.previous_grid=[[' ' for _ in range(self.width)] for _ in range(self.height)]

	def show(self):
		"""在屏幕上打印当前世界的状态，并使用转义字符实现原地刷新"""
		# 使用转义序列清空屏幕并将光标移到左上角
		os.system('cls')
		sys.stdout.write("\033[2J")
		for row in self.current_grid:
			sys.stdout.write(''.join(row)+"\n")
		sys.stdout.flush()  # 确保立即显示

	def seed(self,fill_ratio=0.25):
		"""随机激活约25%的细胞"""
		for i in range(self.height):
			for j in range(self.width):
				if random.random()<fill_ratio:
					self.current_grid[i][j]='*'

	def alive(self,x,y):
		"""判断坐标 (x, y) 的细胞是否存活"""
		if 0<=x<self.height and 0<=y<self.width:
			return self.previous_grid[x][y]=='*'
		return False

	def neighbors(self,x,y):
		"""统计 (x, y) 邻近存活细胞数量"""
		count=0
		for i in range(-1,2):
			for j in range(-1,2):
				if not (i==0 and j==0):  # 跳过自身
					if self.alive(x+i,y+j):
						count+=1
		return count

	def next_state(self,x,y):
		"""判断 (x, y) 在下一代中的状态"""
		alive_neighbors=self.neighbors(x,y)
		if self.alive(x,y):
			# 规则 1 & 3：少于2个或多于3个邻居 -> 死亡；否则存活
			return alive_neighbors==2 or alive_neighbors==3
		else:
			# 规则 4：正好有3个邻居 -> 存活
			return alive_neighbors==3

	def step(self):
		"""执行一步模拟，并更新世界状态"""
		# 将当前状态保存为previous_grid
		self.previous_grid=[row[:] for row in self.current_grid]

		# 更新current_grid
		for i in range(self.height):
			for j in range(self.width):
				if self.next_state(i,j):
					self.current_grid[i][j]='*'
				else:
					self.current_grid[i][j]=' '

	def run(self,delay=0.2):
		"""运行模拟指定步数"""
		while True:
			self.show()  # 显示当前世界状态
			self.step()  # 更新到下一代
			time.sleep(delay)  # 控制每代间隔时间

if __name__=="__main__":
	universe=Universe()
	universe.seed()
	universe.run(delay=0.05)
