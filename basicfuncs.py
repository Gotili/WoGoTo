from __future__ import absolute_import, division, print_function
import pygame
import random
import numpy as np
from PIL import Image

def initfield(Display, field, specialpos, black, gray, display_width):
	global position
	Display.fill((225,225,250))
	textmaker(Display, display_width/2, 10, 30, 30, 'WoGoTo', (0,0,0), 30, 0)	
	positions = []
	#make field
	for k in range(len(field)):
		i = field[k][0]
		j = field[k][1]
		if k in specialpos:
			pygame.draw.rect(Display,black,(55+55*j,50+55*i,50,50))
			if i == 6 and j == 6:
				textmaker(Display, 395, 390, 30, 30, 'Start', (255,255,255), 20, 0)	
		else:
			pygame.draw.rect(Display,gray,(55+55*j,50+55*i,50,50))
	#make buttons
	pygame.draw.rect(Display, gray,(130,190,50,50))
	textmaker(Display, 140, 201, 30, 30, '2-4', black, 20, 0)
	pygame.draw.rect(Display, gray,(190,190,50,50))
	textmaker(Display, 200, 201, 30, 30, '5-7', black, 17, 0)
	pygame.draw.rect(Display, gray,(250,190,50,50))	
	textmaker(Display, 260, 201, 30, 30, '7-9', black, 17, 0)	
	pygame.draw.rect(Display, gray,(310,190,50,50))	
	textmaker(Display, 319, 201, 30, 30, '10-12', black, 17, 0)	
		
		
def updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, red, blue):
	#updateevent = pygame.USEREVENT + 1
	#pygame.time.set_timer(updateevent, 1000)
	i = field[playerpos][0]
	j = field[playerpos][1]	
	i2 = field[playerposold][0]
	j2 = field[playerposold][1]
	#refresh city icon at old position
	if cities[playerposold][1] == 0:
		pygame.draw.rect(Display,blue,(55+55*j2,50+55*i2,50,50))		
		textmaker(Display, 65+55*j2,54+55*i2, 30, 30, str(round(cities[playerposold][2],2)), red, 15, 0)
		textmaker(Display, 65+55*j2,70+55*i2, 30, 30, str(round(cities[playerposold][3],2)), red, 15, 0)	
	elif cities[playerposold][1] == 1:
		pygame.draw.rect(Display,red,(55+55*j2,50+55*i2,50,50))
		textmaker(Display, 65+55*j2,54+55*i2, 30, 30, str(round(cities[playerposold][2],2)), blue, 15, 0)
		textmaker(Display, 65+55*j2,70+55*i2, 30, 30, str(round(cities[playerposold][3],2)), blue, 15, 0)	
	elif playerposold in specialpos:
		pygame.draw.rect(Display,black,(55+55*j2,50+55*i2,50,50))
		if playerposold == 0:
			textmaker(Display, 395, 390, 30, 30, 'Start', (255,255,255), 20, 0)	
	
	#keep other player on old city
	if CP == 0 and players[1][2] == playerpos:
		pygame.draw.circle(Display, (200,200,255), [80+55*j,75+55*i], 10, 0)
	elif CP == 1 and players[0][2] == playerpos:
		pygame.draw.circle(Display, (255,200,200), [80+55*j,75+55*i], 10, 0)
	
	#update city at new position
	if cities[playerpos][1] == 0:
		pygame.draw.rect(Display,blue,(55+55*j,50+55*i,50,50))		
	elif cities[playerpos][1] == 1:
		pygame.draw.rect(Display,red,(55+55*j,50+55*i,50,50))
	
	#mark location of player
	if CP == 0:
		pygame.draw.circle(Display, (150,150,255), [80+55*j,75+55*i], 10, 0)	
	else:
		pygame.draw.circle(Display, (255,150,150), [80+55*j,75+55*i], 10, 0)	
	
	#write toll / mult
	if cities[playerpos][1] == 0 and playerpos not in specialpos:
		textmaker(Display, 65+55*j,54+55*i, 30, 30, str(round(cities[playerpos][2],2)), red, 15, 0)
		textmaker(Display, 65+55*j,70+55*i, 30, 30, str(round(cities[playerpos][3],2)), red, 15, 0)
	elif cities[playerpos][1] == 1 and playerpos not in specialpos:
		textmaker(Display, 65+55*j,54+55*i, 30, 30, str(round(cities[playerpos][2],2)), blue, 15, 0)
		textmaker(Display, 65+55*j,70+55*i, 30, 30, str(round(cities[playerpos][3],2)), blue, 15, 0)
	pygame.display.update()
	
	
def levelup_cities(CP, cities, specialpos, red, blue):
	return
	

# text related functions	
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
	
def textmaker(Display, x, y, w, h, msg, color, size, font):
	if font == 0:
		smallText = pygame.font.Font("freesansbold.ttf",size)
	elif font == 1:
		smallText = pygame.font.SysFont("Times New Roman",size)
	textSurf, textRect = text_objects(msg, smallText,color)
	textRect.center = ((x+(w/2)), (y+(h/2)))
	Display.blit(textSurf, textRect)	
	