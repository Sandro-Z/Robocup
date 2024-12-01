if __name__ == "__main__":
#最好不要将自定义标识符和内置标识符重名
	lst = list(range(1000))

	for item in lst:
		if item%2==1:
			lst.remove(item)
	print(lst)
#使用索引值删除的话，剩余项索引值会改变，导致混乱，因此列表删除内容操作出现时遍历不应使用索引值而要直接遍历元素