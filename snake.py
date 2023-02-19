import pygame
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox


size = width, height = 200, 200
block_size=10
start=(0,0)
color=(255, 255, 255, 255)
game_speed=1.5
radius=7.5
width_rect=block_size
height_rect=block_size
white = pygame.Color(255, 255, 255)


pygame.font.init()

def main_screen(size):
	screen = pygame.Surface(size)
	return screen

def create_grid(size, block_size):
	pos=[]
	for i in range(0,int(width/block_size)):
		for j in range(0,int(height/block_size)):
			pos.append([i,j])
	return pos
def snake(posx,posy,color,screen,width_rect,height_rect):
	rect=pygame.draw.rect(screen,color,[posx,posy,width_rect,height_rect],block_size)
	return rect
	

	


def apples(screen,color,pos_circlex, pos_circley, block_size):
	apple=pygame.draw.rect(screen,color,[pos_circlex*block_size,pos_circley*block_size,block_size,block_size],block_size)
	
	return apple


#def loose():
	#messagebox.showinfo('Continue','OK')

def show_score(choice, color, font, size, score, screen):
	score_font=pygame.font.SysFont(font,size)
	string_count='Count:{}'.format(str(score))
	score_surface = score_font.render(string_count, True, color)
	score_rect = score_surface.get_rect()
	screen.blit(score_surface, score_rect)

	





                    
var=True


def main(var,game_speed,width_rect,height_rect):
	pos=create_grid(size,block_size)
	posx=[]
	posy=[]
	posx.append(1)
	posy.append(1)
	pos_circlex=random.randint(0,20)
	pos_circley=random.randint(0,20)
	count=0
	dir=int()

	while var:
		screen=pygame.display.set_mode(size)
		pygame.display.set_caption('Snake')
		apples(screen,color,pos_circlex, pos_circley, block_size)
		show_score(1, white, 'times new roman', 20, count,screen)
		pygame.display.update()


		for i in posx:
			for j in posy:
				if i<0 or i>width:
					var=False
				elif j<0 or j>height:
					var=False

		
		
				
			
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				var=False

			if event.type==pygame.KEYDOWN:
		
				if event.key==pygame.K_LEFT:
					dir=0
					if len(posy)==1:
						posx.append(posx[0]-1)
						del posx[0]
					else:
						for i in range(len(posy)):
							posx.append(posx[0]-1)
							del posy[-1]
							
					for i in range(len(posx)):
						for j in range(len(posy)):
						
							if 	posx[i]== pos_circlex and posy[j]== pos_circley:
								posx.append(posx[0]-1)
								pos_circlex=random.randint(0,20)
								pos_circley=random.randint(0,20)
								apples(screen,color,pos_circlex, pos_circley, block_size)
								count+=1



		                    
				elif event.key==pygame.K_RIGHT:
					dir=0

					if len(posy)==1:
						posx.append(posx[-1]+1)
						del posx[0]
					else:
						for i in range(len(posy)):
							posx.append(posx[-1]+1)
							del posy[0]
							


					for i in range(len(posx)):
						for j in range(len(posy)):
							
							if 	posx[i] == pos_circlex and posy[j] == pos_circley:
								posx.append(posx[-1]+1)
								pos_circlex=random.randint(0,20) 
								pos_circley=random.randint(0,20) 
								apples(screen,color,pos_circlex, pos_circley, block_size)
								count+=1

			
								

				elif event.key==pygame.K_DOWN:
					dir=1

					if len(posx)==1:
						posy.append(posy[-1]+1)
						del posy[0]
					if len(posx)>1:
						for i in range(len(posx)):
							posy.append(posy[-1]+1)
							del posx[0]

					for i in range(len(posx)):
						for j in range(len(posy)):
							if 	posx[i] == pos_circlex and posy[j] == pos_circley:
								posy.append(posy[-1]+1)
								pos_circlex=random.randint(0,20) 
								pos_circley=random.randint(0,20)
								apples(screen,color,pos_circlex, pos_circley, block_size)
								count+=1
					


						

				elif event.key==pygame.K_UP:
					dir=1

					if len(posx)==1:
						posy.append(posy[0]-1)
						del posy[0]
					else:
						for i in range(len(posx)):
							posy.append(posy[0]-1)
							del posx[-1]

					
					

					for i in range(len(posx)):
						
						for j in range(len(posy)):
							
							if 	posx[i] == pos_circlex and posy[j] == pos_circley:
								posy.append(posy[0]-1)
								pos_circlex=random.randint(0,20) 
								pos_circley=random.randint(0,20)
								apples(screen,color,pos_circlex, pos_circley, block_size)
								count+=1

		
	"""		
		if  dir==0:	
			if len(posy)>1:
				posj=posy[-1]*block_size
			else:
				posj=posy[0]*block_size
			for i in range(len(posx)):
				posi=posx[i]*block_size
				snake(posi,posj,color,screen,width_rect,height_rect)
				

		elif  dir==1:
			posi=posx[-1]*block_size
			for j in range(len(posx)):
				posj=posy[j]*block_size
				snake(posi,posj,color,screen,width_rect,height_rect) 
		else:"""
		for i in range(len(posx)):
			for j in range(len(posy)):
				posi=posx[i]*block_size
				posj=posy[j]*block_size
				snake(posi,posj,color,screen,width_rect,height_rect)
	




			

						
		pygame.display.update()					
								

		
			
				
				
	
			

		


				

				
																																	            
           		
 
main(var,game_speed,width_rect,height_rect)



