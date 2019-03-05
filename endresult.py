#进行结果判定
import pygame
import choose
import sys
import record
from pygame.locals import *


win_sound = pygame.mixer.Sound('material/sound/win.wav')
win_sound.set_volume(0.2)

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


def  result_screen(result,sound,process_time,level):

	#游戏战绩记录
	record.record(level,result,process_time)
	#提取记录
	time,times,odds = record.get_record(level)
	#建立界面
	bg_size = width,height = 450,700
	r_screen = pygame.display.set_mode(bg_size)
	r_screen.fill((237,237,237))

	r_font1 = pygame.font.Font('material/benmoyouyuan.ttf',67)
	r_font2 = pygame.font.Font('material/benmoyouyuan.ttf',50)
	r_font3 = pygame.font.Font('material/benmoyouyuan.ttf',30)
	r_font4 = pygame.font.Font('material/benmoyouyuan.ttf',20)

	pygame.draw.rect(r_screen,(0,0,0),[100,450,250,100],5)

	process_time = str(process_time)
	r_text1 = r_font1.render(result,True,(0,0,0))
	r_text2 = r_font2.render("继续游戏",True,(0,0,0))
	r_text3 = r_font3.render('游戏时间：'+process_time+'秒',True,(0,0,0))
	r_text4 = r_font4.render('游戏记录：'+time+'秒',True,(0,0,0))
	r_text5 = r_font4.render('游戏次数：'+times+'次',True,(0,0,0))
	r_text6 = r_font4.render('游戏胜率：'+odds,True,(0,0,0))

	r_screen.blit(r_text1,(90,100))
	r_screen.blit(r_text2,(120,470))
	r_screen.blit(r_text3,(120,200))
	r_screen.blit(r_text4,(120,250))
	r_screen.blit(r_text5,(120,300))
	r_screen.blit(r_text6,(120,350))


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
