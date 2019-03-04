#翻开功能部分

import pygame
import main_game
import endresult
from pygame.locals import *

pygame.mixer.init()
boom_sound = pygame.mixer.Sound('material/sound/BOOM.wav')
boom_sound.set_volume(0.2)


#比较得出雷数
def mine_digital(i,j,map1):
	count = 0
	if i-1>=0 and j-1>=0 and map1[i-1][j-1] == '9':
		count += 1
	if i-1>=0 and map1[i-1][j] == '9':
		count += 1
	if i-1>=0 and j+1<len(map1[0]) and map1[i-1][j+1] == '9':
		count += 1
	if j-1>=0 and map1[i][j-1] == '9':
		count += 1
	if j+1<len(map1[0]) and map1[i][j+1] == '9':
		count += 1
	if i+1<len(map1) and j-1>=0 and map1[i+1][j-1] == '9':
		count += 1
	if i+1<len(map1) and map1[i+1][j] == '9':
		count += 1
	if i+1<len(map1) and j+1<len(map1[0]) and map1[i+1][j+1] == '9':
		count += 1
	return count


def flag_digital(i,j,map1):
	count = 0
	if i-1>=0 and j-1>=0 and map1[i-1][j-1] == '10':
		count += 1
	if i-1>=0 and map1[i-1][j] == '10':
		count += 1
	if i-1>=0 and j+1<len(map1[0]) and map1[i-1][j+1] == '10':
		count += 1
	if j-1>=0 and map1[i][j-1] == '10':
		count += 1
	if j+1<len(map1[0]) and map1[i][j+1] == '10':
		count += 1
	if i+1<len(map1) and j-1>=0 and map1[i+1][j-1] == '10':
		count += 1
	if i+1<len(map1) and map1[i+1][j] == '10':
		count += 1
	if i+1<len(map1) and j+1<len(map1[0]) and map1[i+1][j+1] == '10':
		count += 1
	return count



#周围判断
def arround(screen,i,j,map1,map2,sound):
	if map1[i][j] == '9':
		omine_image = pygame.image.load('material/picture/mine.gif').convert()
		mine_image = pygame.transform.scale(omine_image,(22,22))
		screen.blit(mine_image,(i*30+3,j*30+3))
		if sound:
			boom_sound.play()
		pygame.display.flip()
		for x in range(len(map1)):
			for y in range(len(map1[0])):
				if map1[x][y] == '9':
					screen.blit(mine_image,(x*30+3,y*30+3))
					pygame.display.flip()
					pygame.time.delay(100)
		result = '游戏失败'
		pygame.time.delay(1000)
		endresult.result_screen(result,sound)



		#显示lose
	else:
		digital = mine_digital(i,j,map1)
		map1[i][j] = str(digital)
		print('内容填写部分正常')
		if map1[i][j] == '0':
			print('判断成功')
			map1[i][j] = ' '

			if i-1>=0 and j-1>=0 and len(map1[i-1][j-1]) == 0 and map2[i-1][j-1] == '':
				arround(screen,i-1,j-1,map1,map2,sound)
			if i-1>=0 and len(map1[i-1][j]) == 0 and map2[i-1][j] == '':
				arround(screen,i-1,j,map1,map2,sound)
			if i-1>=0 and j+1<len(map1[0]) and len(map1[i-1][j+1]) == 0 and map2[i-1][j+1] == '':
				arround(screen,i-1,j+1,map1,map2,sound)
			if j-1>=0 and len(map1[i][j-1]) == 0 and map2[i][j-1] == '':
				arround(screen,i,j-1,map1,map2,sound)
			if j+1<len(map1[0]) and len(map1[i][j+1]) == 0 and map2[i][j+1] == '':
				arround(screen,i,j+1,map1,map2,sound)
			if i+1<len(map1) and j-1>=0 and len(map1[i+1][j-1]) == 0 and map2[i+1][j-1] == '':
				arround(screen,i+1,j-1,map1,map2,sound)
			if i+1<len(map1) and len(map1[i+1][j]) == 0 and map2[i+1][j] == '':
				arround(screen,i+1,j,map1,map2,sound)
			if i+1<len(map1) and j+1<len(map1[0]) and len(map1[i+1][j+1]) == 0 and map2[i+1][j+1] == '':
				arround(screen,i+1,j+1,map1,map2,sound)
		s_font = pygame.font.Font('material/benmoyouyuan.ttf',19)
		if map1[i][j] == '1':
			color = (86,98,166)
		elif map1[i][j] == '2':
			color = (67,106,62)
		elif map1[i][j] == '3':
			color = (15,170,209)
		else:
			color = (222,29,90)
		s_text = s_font.render(str(map1[i][j]),True,color)
		#将字放在窗口指定位置
		screen.blit(s_text,(i*30+9,j*30+3))
		#将为零的格子填充为新颜色
		for i in range(len(map1)):
			for j in range(len(map1[0])):
				if map1[i][j] == ' ':
					pygame.draw.rect(screen,(200,200,200),[i*30,j*30,29,29])

