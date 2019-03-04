#布雷部分

import random

def lay_mines(level,map1):
	if level == '低':
		a = 0
		while a<10:
			x = random.randint(0,9)
			y = random.randint(0,9)
			map1[x][y] = '9'
			print('布雷功能运行正常')
			a = 0
			for i in range(10):
				for j in range(10):
					if map1[i][j] == '9':
						a += 1
						print(a)
	elif level == '中':
		a = 0
		while a<40:
			x = random.randint(0,15)
			y = random.randint(0,15)
			map1[x][y] = '9'
			print('布雷功能运行正常')
			a = 0
			for i in range(16):
				for j in range(16):
					if map1[i][j] == '9':
						a += 1
						print(a)
	elif level == '高':
		a = 0
		while a<99:
			x = random.randint(0,31)
			y = random.randint(0,15)
			map1[x][y] = '9'
			print('布雷功能运行正常')
			a = 0
			for i in range(32):
				for j in range(16):
					if map1[i][j] == '9':
						a += 1
						print(a)

