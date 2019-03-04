#难度选择部分

import pygame
import sys
import main_game
from pygame.locals import *

#初始化模块
pygame.init()
pygame.mixer.init()

#音效加载
button_sound = pygame.mixer.Sound('material/sound/button.wav')
button_sound.set_volume(0.2)
background_sound = pygame.mixer.music.load('material/sound/background.ogg')
pygame.mixer.music.set_volume(0.3)

sys.setrecursionlimit(2000)

	#画出主界面
def draw_choose_interface(level):
		
	#level为难度等级，prompt为显示界面所显示的文字

	bg_size = width,height = 450,700
	screen = pygame.display.set_mode(bg_size)
	screen.fill((237,237,237))
	#画出选择框
	pygame.draw.rect(screen,(0,0,0),[175,100,100,300],5)
	#分割出三部分存放+，-和等级的位置
	pygame.draw.line(screen,(0,0,0),(175,200),(275,200),5)
	pygame.draw.line(screen,(0,0,0),(175,300),(275,300),5)
	#画出+的横线以及-
	pygame.draw.line(screen,(0,0,0),(195,150),(255,150),20)
	pygame.draw.line(screen,(0,0,0),(195,350),(255,350),20)
	#画出+的竖线
	pygame.draw.line(screen,(0,0,0),(225,120),(225,180),20)
	#开始游戏的选择框
	pygame.draw.rect(screen,(0,0,0),[100,450,250,100],5)
	#定义字体跟大小
	s_font1=pygame.font.Font('material/benmoyouyuan.ttf',50)
	s_font2=pygame.font.Font('material/benmoyouyuan.ttf',16)
	s_font3=pygame.font.Font('material/benmoyouyuan.ttf',34)
	#文本确定
	s_text1=s_font1.render(str(level),True,(0,0,0))
	s_text2=s_font1.render("开始游戏",True,(0,0,0))
	s_text3=s_font2.render('Listening_Rift',True,(0,0,0))
	s_text4=s_font3.render('难度选择：',True,(255,0,0))
	#将字放在窗口指定位置
	screen.blit(s_text1,(200,220))
	screen.blit(s_text2,(120,470))
	screen.blit(s_text3,(22,650))
	screen.blit(s_text4,(100,50))

	o_sound_go = pygame.image.load('material/picture/go.gif').convert_alpha()
	o_sound_pause = pygame.image.load('material/picture/pause.gif').convert_alpha()
	sound_go = pygame.transform.scale(o_sound_go,(50,50))
	sound_pause = pygame.transform.scale(o_sound_pause,(50,50))
	screen.blit(sound_go,(310,630))
	screen.blit(sound_pause,(380,630))
	


	pygame.display.set_caption('难度选择')
	pygame.display.flip()

def _interface(sound = 1):
	level = '低'
	if sound:
		pygame.mixer.music.play(-1)
	draw_choose_interface(level)
	

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					print(sound)
					if 175<event.pos[0]<275 and 100<event.pos[1]<200:
						if level == '低':
							level = '中'
							if sound:
								button_sound.play()
							draw_choose_interface(level)
						elif level == '中':
							level = '高'
							if sound:
								button_sound.play()
							draw_choose_interface(level)
						elif level == '高':
							level = '低'
							if sound:
								button_sound.play()
							draw_choose_interface(level)
					elif 175<event.pos[0]<275 and 300<event.pos[1]<400:
						if level == '高':
							level = '中'
							if sound:
								button_sound.play()
							draw_choose_interface(level)
						elif level == '中':
							level = '低'
							if sound:
								button_sound.play()
							draw_choose_interface(level)
						elif level == '低':
							level = '高'
							if sound:
								button_sound.play()
							draw_choose_interface(level)
					elif 310<event.pos[0]<360 and 630<event.pos[1]<680:
						pygame.mixer.music.unpause()
						sound = 1
					elif 380<event.pos[0]<430 and 630<event.pos[1]<680:
						pygame.mixer.music.pause()
						sound = 0
					elif 100<event.pos[0]<350 and 450<event.pos[1]<550:
						if sound:
							button_sound.play()
						print(sound)
						main_game.game_main(level,sound)


if __name__ == '__main__':
	_interface()