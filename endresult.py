#进行结果判定
import pygame
import choose
import sys
from pygame.locals import *

#判定结果
def result_judge(map1,map2,sound):
	
	mine = []
	flag = []

	for x in range(len(map1)):
		for y in range(len(map1[0])):
			if map1[x][y] == '9':
				mine.append((x,y))
			if map2[x][y] == '10':
				flag.append((x,y))
	if mine == flag:
		result = '游戏胜利'
		if sound:
			win_sound.play()
	else:
		result = '游戏失败'

	return result


def  result_screen(result,sound):


	#建立界面
	bg_size = width,height = 450,700
	r_screen = pygame.display.set_mode(bg_size)
	r_screen.fill((237,237,237))

	r_font1 = pygame.font.Font('material/benmoyouyuan.ttf',67)
	r_font2 = pygame.font.Font('material/benmoyouyuan.ttf',50)

	pygame.draw.rect(r_screen,(0,0,0),[100,450,250,100],5)

	r_text1 = r_font1.render(result,True,(0,0,0))
	r_text2 = r_font2.render("继续游戏",True,(0,0,0))

	r_screen.blit(r_text1,(90,100))
	r_screen.blit(r_text2,(120,470))

	pygame.display.set_caption('游戏结束')

	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if 100<event.pos[0]<350 and 450<event.pos[1]<550:
						pygame.display.quit()
						choose._interface(sound)
