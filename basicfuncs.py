from __future__ import absolute_import, division, print_function
import pygame
import random
import numpy as np
from PIL import Image

def initfield(Display, field, specialpos, black, gray, display_width, bgcolor):
	global position
	Display.fill(bgcolor)
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
	i = field[playerpos][0]
	j = field[playerpos][1]	
	i2 = field[playerposold][0]
	j2 = field[playerposold][1]

	#refresh city icons at old position
	# Update Icons for P1 cities
	if cities[playerposold][1] == 0:
		if cities[playerposold][5] == 1:
			pygame.draw.rect(Display,blue,(55+55*j2,50+55*i2,15,15))
		elif cities[playerposold][5] == 2:
			pygame.draw.rect(Display,blue,(55+55*j2,50+55*i2,25,25))	
		elif cities[playerposold][5] == 3:
			pygame.draw.rect(Display,blue,(55+55*j2,50+55*i2,37,37))
		elif cities[playerposold][5] == 3:
			pygame.draw.rect(Display,blue,(55+55*j2,50+55*i2,50,50))	
		textmaker(Display, 65+55*j2,54+55*i2, 30, 30, str(round(cities[playerposold][2],2)), red, 15, 0)
		textmaker(Display, 65+55*j2,70+55*i2, 30, 30, str(round(cities[playerposold][3],2)), red, 15, 0)
		
	# Update Icons for P2 cities
	elif cities[playerposold][1] == 1:
		if cities[playerposold][5] == 1:
			pygame.draw.rect(Display,red,(55+55*j2,50+55*i2,15,15))
		elif cities[playerposold][5] == 2:
			pygame.draw.rect(Display,red,(55+55*j2,50+55*i2,25,25))
		elif cities[playerposold][5] == 3:
			pygame.draw.rect(Display,red,(55+55*j2,50+55*i2,37,37))
		elif cities[playerposold][5] == 3:
			pygame.draw.rect(Display,red,(55+55*j2,50+55*i2,50,50))	
	
		textmaker(Display, 65+55*j2,54+55*i2, 30, 30, str(round(cities[playerposold][2],2)), blue, 15, 0)
		textmaker(Display, 65+55*j2,70+55*i2, 30, 30, str(round(cities[playerposold][3],2)), blue, 15, 0)
	
	#restore special blocks
	elif playerposold in specialpos:
		pygame.draw.rect(Display,black,(55+55*j2,50+55*i2,50,50))
		if playerposold == 0:
			textmaker(Display, 395, 390, 30, 30, 'Start', (255,255,255), 20, 0)	
	
	#keep other player on old city
	if CP == 0 and players[1][2] == playerposold:
		pygame.draw.circle(Display, (255,150,150), [80+55*j2,75+55*i2], 10, 0)
	elif CP == 1 and players[0][2] == playerposold:
		pygame.draw.circle(Display, (150,150,255), [80+55*j2,75+55*i2], 10, 0)
	
	#update city at new position
	# Update Icon for P1 cities
	if cities[playerpos][1] == 0:
		if cities[playerposold][5] == 1:
			pygame.draw.rect(Display,blue,(55+55*j,50+55*i,15,15))
		elif cities[playerposold][5] == 2:
			pygame.draw.rect(Display,blue,(55+55*j,50+55*i,25,25))	
		elif cities[playerposold][5] == 3:
			pygame.draw.rect(Display,blue,(55+55*j,50+55*i,37,37))
		elif cities[playerposold][5] == 3:
			pygame.draw.rect(Display,blue,(55+55*j,50+55*i,50,50))	
			
	# Update Icon for P2 cities		
	elif cities[playerpos][1] == 1:
		if cities[playerposold][5] == 1:
			pygame.draw.rect(Display,red,(55+55*j,50+55*i,15,15))
		elif cities[playerposold][5] == 2:
			pygame.draw.rect(Display,red,(55+55*j,50+55*i,25,25))	
		elif cities[playerposold][5] == 3:
			pygame.draw.rect(Display,red,(55+55*j,50+55*i,37,37))
		elif cities[playerposold][5] == 3:
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
	
	
def levelup_cities(Display, field, players, CP, cities, specialpos, playerpos, playerposold, black, red, blue):
	for e in cities:
		if e[1] == CP:
			if e[5] != 4 and e[5] < 5:
				e[5] += 1
			citypos = e[0]
			i = field[citypos][0]
			j = field[citypos][1]
			# Update Icons for P2 cities
			if CP == 0:
				if e[5] == 2:
					pygame.draw.rect(Display,blue,(55+55*j,50+55*i,25,25))	
				elif e[5] == 3:
					pygame.draw.rect(Display,blue,(55+55*j,50+55*i,37,37))
				elif e[5] == 4:
					pygame.draw.rect(Display,blue,(55+55*j,50+55*i,50,50))	
				textmaker(Display, 65+55*j,54+55*i, 30, 30, str(round(e[2],2)), red, 15, 0)
				textmaker(Display, 65+55*j,70+55*i, 30, 30, str(round(e[3],2)), red, 15, 0)
			# Update Icons for P2 cities
			elif CP == 1:
				if e[5] == 2:
					pygame.draw.rect(Display,red,(55+55*j,50+55*i,25,25))	
				elif e[5] == 3:
					pygame.draw.rect(Display,red,(55+55*j,50+55*i,37,37))
				elif e[5] == 4:
					pygame.draw.rect(Display,red,(55+55*j,50+55*i,50,50))	
				textmaker(Display, 65+55*j,54+55*i, 30, 30, str(round(e[2],2)), blue, 15, 0)
				textmaker(Display, 65+55*j,70+55*i, 30, 30, str(round(e[3],2)), blue, 15, 0)
	pygame.display.update()
	
	
def switch_players(Display, CP, double, red, blue):
	if CP == 0 and double != True:
		CP = 1
		pygame.draw.rect(Display, (225,225,250),(180,260,130,35))	
		textmaker(Display, 230, 260, 30, 30, 'Player: '+str(CP+1), red, 30, 0)
	elif CP == 1 and double != True:
		CP = 0
		pygame.draw.rect(Display, (225,225,250),(180,260,130,35))	
		textmaker(Display, 230, 260, 30, 30, 'Player: '+str(CP+1), blue, 30, 0)
	roll = None
	print()
	print()
	return CP, roll

	
	
def end_game(Display, clock, CP, bgcolor, black, grey, lightgrey, red, blue):
	color = bgcolor
	crashed = False
	flash = 'on'
	endevent = pygame.USEREVENT + 1
	endevent2 = pygame.event.Event(endevent)
	pygame.event.post(endevent2)
	while not crashed:
		for event in pygame.event.get():
			Display.fill(bgcolor)
			
			#check if mouse is above buttons
			mouse = pygame.mouse.get_pos()
			if 255+80 > mouse[0] > 255 and 260+50 > mouse[1] > 260:
				pygame.draw.rect(Display, lightgrey,(255,260,80,50))
				textmaker(Display, 280, 270, 30, 30, 'Exit', black, 20, 0)
			else:
				pygame.draw.rect(Display, grey,(255,260,80,50))
				textmaker(Display, 280, 270, 30, 30, 'Exit', black, 20, 0)			
			if 185+80 > mouse[0] > 185 and 260+50 > mouse[1] > 270:
				pygame.draw.rect(Display, lightgrey,(160,260,80,50))
				textmaker(Display, 185, 270, 30, 30, 'Replay', black, 20, 0)
			else:
				pygame.draw.rect(Display, grey,(160,260,80,50))
				textmaker(Display, 185, 270, 30, 30, 'Replay', black, 20, 0)				
			pygame.display.update()
			
			#replay or exit 
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if 255+80 > mouse[0] > 255 and 260+50 > mouse[1] > 260:
						crashed = True
						exitted = True
						return crashed
					elif 185+80 > mouse[0] > 185 and 260+50 > mouse[1] > 270:
						crashed = True
						exitted = False
						return exitted
					else:
						pass
							
			# Display flashing endscreen
			if event.type == 25:		
				if flash == 'off':
					color = blue
					flash = 'on'				
				elif flash == 'on':
					color = red
					flash = 'off'	
				textmaker(Display, 230,140, 30, 30, 'GAME OVER', color, 30, 0)
				textmaker(Display, 230,190, 30, 30, 'Player: '+str(CP+1)+' lost', color, 30, 0)				
				pygame.display.update()
				pygame.event.pump()
				pygame.event.clear()
				endevent = pygame.USEREVENT + 1
				endevent2 = pygame.event.Event(endevent)
				pygame.event.post(endevent2)
				clock.tick(10) 
				
				
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
	