
from  pygame import *
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

###Definir la pantalla
width, height=500, 500
tile=50
color_snake="green"
color_food="red"
var=True
font.init()
white = Color(255, 255, 255)
pos_food=(random.randint(1,width/tile),random.randint(1,height/tile))
def show_score(choice, color, fuente, size, score, screen):
	score_font=font.SysFont(fuente,size)
	string_count='Count:{}'.format(str(score))
	score_surface = score_font.render(string_count, True, color)
	score_rect = score_surface.get_rect()
	screen.blit(score_surface, score_rect)

def game(width, heigh,color_snake,tile,pos_food, color_food):
	posx=[0]
	posy=[0]
	dir=0
	var=True
	count=0
	posx.append(0)
	posy.append(0)
	sn=Rect(posx[0]*tile,posy[0]*tile, tile, tile)
	fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
	while var:
		screen=display.set_mode((heigh,width))
		display.set_caption('Snake v.2')
		show_score(1, white, 'times new roman', 20, count,screen)
		###draw the snake
		draw.rect(screen,color_snake,sn)
		#draw the food
		draw.rect(screen, color_food,fd)

		for i in posx:
			for j in posy:
				if i<0 or i>width:
					var=False
				elif j<0 or j>height:
					var=False

		

		for e in event.get():
			if e.type == QUIT:
				var=False

		#left movement
			if e.type==KEYDOWN:
				if e.key==K_LEFT:
					dir=1
					if len(posy)<2:
						for i in range(len(posx)):
							posx[i]-=1
							if sn==fd:
								count+=1
								fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(heigh/tile)-1)*tile, tile, tile)
								draw.rect(screen, color_food,fd)
								posx.append((posx[0]+1))
					if len(posy)>2:
							for i in range(len(posy)):
								posx.append((posx[0]-1))
								if sn==fd:
									count+=1
									fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
									draw.rect(screen, color_food,fd)
									posx.append((posx[0]+1))
							if dir==3:
								newy=posy[0]
							else:
								newy=posy[-1]
								
							posy.clear()
							posy.append(newy)
					else:
						for i in range(len(posx)):
							posx[i]-=1
							if sn==fd:
									count+=1
									fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
									draw.rect(screen, color_food,fd)
									posx.append((posx[0]+1))



				
				#right movement	
				if e.key==K_RIGHT:
					dir=2
					if len(posy)<2:
							for i in range(len(posx)):
								posx[i]+=1
								if sn==fd:
									count+=1
									fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
									draw.rect(screen, color_food,fd)
									posx.append((posx[0]-1))

					if len(posy)>2:
							for i in range(len(posy)):
								posx.append((posx[0]+1))
								if sn==fd:
									count+=1
									fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
									draw.rect(screen, color_food,fd)
									posx.append((posx[0]-1))
							if dir==3:
								newy=posy[0]
							else:
								newy=posy[-1]		
							posy.clear()
							posy.append(newy)
					else:
						for i in range(len(posx)):
							
							posx[i]+=1
							if sn==fd:
								count+=1
								fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
								draw.rect(screen, color_food,fd)
								posx.append((posx[0]-1))




				#up movement				
				if e.key==K_UP:
					dir=3
					if len(posx)<2:
						for i in range(len(posy)):
							posy[i]-=1
							if sn==fd:
								count+=1
								fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
								draw.rect(screen, color_food,fd)
								posy.append(posy[0]-1)
					if len(posx)>2:
						for i in range(len(posx)):
							posy.append((posy[0]-1))
							if sn==fd:
								count+=1
								fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
								draw.rect(screen, color_food,fd)
								posy.append(posy[0]-1)
							if dir==1:
								newx=posx[0]
							else:
								newx=posx[-1]
	
						posx.clear()
						posx.append(newx)
					else:
						for i in range(len(posy)):
							posy[i]-=1
							if sn==fd:
								count+=1
								fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
								draw.rect(screen, color_food,fd)
								posy.append(posy[0]-1)

						
				#down movement
				if e.key==K_DOWN:
					dir=4
					if len(posx)<2:
						for i in range(len(posy)):
							posy[i]+=1
							if sn==fd:
								count+=1
								fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
								draw.rect(screen, color_food,fd)
								posy.append(posy[0]+1)
					if len(posx)>2:
						for i in range(len(posx)):
							posy.append((posy[0]+1))
							if sn==fd:
								count+=1
								fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
								draw.rect(screen, color_food,fd)
								posy.append(posy[0]+1)
						if dir==1:
							newx=posx[0]
						else:
							newx=posx[-1]
						posx.clear()
						posx.append(newx)
					else:
						for i in range(len(posy)):
							posy[i]+=1
							if sn==fd:
								count+=1
								fd=Rect(random.randint(1,(width/tile)-1)*tile,random.randint(1,(height/tile)-1)*tile, tile, tile)
								draw.rect(screen, color_food,fd)
								posy.append(posy[0]+1)
					




		if dir==1 or 2:
			for i in range(len(posx)):
				sn=Rect(posx[i]*tile,posy[0]*tile, tile, tile)
				draw.rect(screen,color_snake,sn)

			
		if dir==3 or 4:
			for j in range(len(posy)):
				sn=Rect(posx[0]*tile,posy[j]*tile, tile, tile)
				draw.rect(screen,color_snake,sn)	
			

			
		display.update()



game(width, height, color_snake,tile,pos_food,color_food)