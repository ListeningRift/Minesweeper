#主题游戏部分实现
import endresult
import pygame
import traceback
import sys
import random
import choose
import lay_mines
import open_event
from pygame.locals import *


#9代表雷
#10代表旗帜

sys.setrecursionlimit(1000)
#板块初始化
pygame.init()

#音效载入，背景音乐，点击音效，爆炸音效，音量均为0.2
pygame.mixer.init()
button_sound = pygame.mixer.Sound('material/sound/button.wav')
button_sound.set_volume(0.2)
boom_sound = pygame.mixer.Sound('material/sound/BOOM.wav')
boom_sound.set_volume(0.2)
background_sound = pygame.mixer.music.load('material/sound/background.ogg')
pygame.mixer.music.set_volume(0.2)
win_sound = pygame.mixer.Sound('material/sound/win.wav')
win_sound.set_volume(0.2)






def game_main(level,sound):
	#生成主界面
	if level == '低':
		bg_size = width,height = 300,300
	elif level == '中':
		bg_size = width,height = 480,480
	elif level == '高':
		bg_size = width,height = 960,480
	screen_main = pygame.display.set_mode(bg_size)
	screen_main.fill((237,237,237))
	pygame.display.set_caption('L_R扫雷:%s级模式'%level)

	if sound == 1:
		pygame.mixer.music.play(-1)

	#画格子?
	for x in range(width//30):
		for y in range(height//30):
			pygame.draw.rect(screen_main,(0,0,0),[x*30,y*30,29,29],1)

	pygame.display.flip()


	#初始化地图二维列表
	if level == '低':
		map1 = [[0 for col in range(10)] for row in range(10)]
		map2 = [[0 for col in range(10)] for row in range(10)]
		for i in range(10):
			for j in range(10):
				map1[i][j] = ''
				map2[i][j] = ''
	elif level == '中':
		map1 = [[0 for col in range(16)] for row in range(16)]
		map2 = [[0 for col in range(16)] for row in range(16)]
		for i in range(16):
			for j in range(16):
				map1[i][j] = ''
				map2[i][j] = ''
	elif level == '高':
		map1 = [[0 for col in range(16)] for row in range(32)]
		map2 = [[0 for col in range(16)] for row in range(32)]
		for i in range(32):
			for j in range(16):
				map1[i][j] = ''
				map2[i][j] = ''


	#布雷
	lay_mines.lay_mines(level,map1)

	#确定双击事件所需的列表
	location = [(0,0)]

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if sound:
						button_sound.play()
					i = event.pos[0]//30
					j = event.pos[1]//30
					if (map1[i][j] == '' or map1[i][j] == '9') and map2[i][j] == '':			
						open_event.arround(screen_main,i,j,map1,map2,sound)
						print('翻开成功')
						pygame.display.flip()
					if map1[i][j] != '' and map1[i][j] != '9' and map2[i][j] == '':
						location.append((event.pos[0],event.pos[1]))
						last = location.pop(0)
						flag_num = str(open_event.flag_digital(i,j,map2))
						if last == (event.pos[0],event.pos[1]) and flag_num == map1[i][j]:
							if i-1>=0 and j-1>=0 and (map1[i-1][j-1] == '' or map1[i-1][j-1] == '9') and map2[i-1][j-1] == '':
								open_event.arround(screen_main,i-1,j-1,map1,map2,sound)
							if i-1>=0 and (map1[i-1][j] == '' or map1[i-1][j] == '9') and map2[i-1][j] == '':
								open_event.arround(screen_main,i-1,j,map1,map2,sound)
							if i-1>=0 and j+1<len(map1[0]) and (map1[i-1][j+1] == '' or map1[i-1][j+1] == '9') and map2[i-1][j+1] == '':
								open_event.arround(screen_main,i-1,j+1,map1,map2,sound)
							if j-1>=0 and (map1[i][j-1] == '' or map1[i][j-1] == '9') and map2[i][j-1] == '':
								open_event.arround(screen_main,i,j-1,map1,map2,sound)
							if j+1<len(map1[0]) and map1[i][j+1] == '' and map2[i][j+1] == '':
								open_event.arround(screen_main,i,j+1,map1,map2,sound)
							if i+1<len(map1) and j-1>=0 and map1[i+1][j-1] == '' and map2[i+1][j-1] == '':
								open_event.arround(screen_main,i+1,j-1,map1,map2,sound)
							if i+1<len(map1) and map1[i+1][j] == '' and map2[i+1][j] == '':
								open_event.arround(screen_main,i+1,j,map1,map2,sound)
							if i+1<len(map1) and j+1<len(map1[0]) and map1[i+1][j+1] == '' and map2[i+1][j+1] == '':
								open_event.arround(screen_main,i+1,j+1,map1,map2,sound)
							pygame.display.flip()
							


				elif event.button == 3:
					if sound:
						button_sound.play()
					i = event.pos[0]//30
					j = event.pos[1]//30
					if (map1[i][j] == '' or map1[i][j] == '9') and map2[i][j] == '':
						map2[i][j] = '10'
						oflag = pygame.image.load('material/picture/flag.gif')
						flag = pygame.transform.scale(oflag,(22,22))
						screen_main.blit(flag,(i*30+3,j*30+3))
						print('标记成功')
						pygame.display.flip()
					elif (map1[i][j] == '' or map1[i][j] == '9') and map2[i][j] == '10':
						map2[i][j] = ''
						print('取消标记')
						oblank = pygame.image.load('material/picture/blank.gif')
						flag = pygame.transform.scale(oblank,(22,22))
						screen_main.blit(flag,(i*30+3,j*30+3))
						pygame.display.flip()
					
					if level == '低':
						mines = 10
					elif level == '中':
						mines = 40
					elif level == '高':
						mines = 99

					flags = 0
					for x in range(len(map2)):
						for y in range(len(map2[0])):
							if map2[x][y] == '10':
								flags += 1
					if flags == mines:
						result = endresult.result_judge(map1,map2,sound)
						pygame.time.delay(1000)
						endresult.result_screen(result,sound)
