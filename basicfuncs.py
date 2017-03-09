from __future__ import absolute_import, division, print_function
import pygame
import random
import numpy as np

def initfield(Display, field, specialpos, black, grey, display_width, bgcolor):
	global position
	Display.fill(bgcolor)
	textmaker(Display, display_width/2, 10, 30, 30, 'WoGoTo', (0,0,0), 30, 0)	
	positions = []	
	# Make field
	for k in range(len(field)):
		i = field[k][0]
		j = field[k][1]
		if k in specialpos:
			pygame.draw.rect(Display,black,(55+55*j,50+55*i,50,50))
			if i == 6 and j == 6:
				textmaker(Display, 395, 390, 30, 30, 'Start', (255,255,255), 20, 0)	
		else:
			pygame.draw.rect(Display,grey,(55+55*j,50+55*i,50,50))
	draw_dicebuttons(Display, black, grey)
	

# Makes Dicedraw buttons
def draw_dicebuttons(Display, black, grey):
	pygame.draw.rect(Display, grey,(130,190,50,50))
	textmaker(Display, 140, 201, 30, 30, '2-4', black, 20, 0)
	pygame.draw.rect(Display, grey,(190,190,50,50))
	textmaker(Display, 200, 201, 30, 30, '5-7', black, 17, 0)
	pygame.draw.rect(Display, grey,(250,190,50,50))	
	textmaker(Display, 260, 201, 30, 30, '7-9', black, 17, 0)	
	pygame.draw.rect(Display, grey,(310,190,50,50))	
	textmaker(Display, 319, 201, 30, 30, '10-12', black, 17, 0)	
	

# Evaluate new player position
def get_newplayerpos(Display, field, players, cities, CP, specialpos, playerposold, black, grey, red, blue, diceroll, fieldnum, P1color, P2color):
	playerpos = playerposold + diceroll[0] + diceroll[1]
	# Check if start is passed and level up cities
	if playerpos > fieldnum-1:
		playerpos = playerpos - fieldnum
		players[CP][2] = playerpos	
		cities, players = levelup_cities(Display, field, players, CP, cities, specialpos, playerpos, playerposold, black, grey, red, blue)
		cities = calc_toll(cities, playerpos, cities[playerpos][2], cities[playerpos][4], cities[playerpos][6])
		updatecitys(Display, field, cities, players, specialpos, black, grey, blue, red)
		draw_playerpos(Display, field, cities, players, specialpos, blue, red, P1color, P2color)
	if playerposold > fieldnum-1:
		playerposold = playerposold - fieldnum
	pygame.display.update()
	print('Oldpos: ' + str(playerposold) + ', Diceroll: ' + str(diceroll[0]) + '-' + str(diceroll[1]) + ': ' + str(diceroll[0]+diceroll[1]) +', Newpos: ' + str(playerpos))	
	return cities, players, playerpos, playerposold
	
	
def updatecitys(Display, field, cities, players, specialpos, black, grey, blue, red):
	for city in cities:
		#redraw blue citys
		cityi = field[city[0]][0]
		cityj = field[city[0]][1]
		if city[1] == 0:
			pygame.draw.rect(Display, grey, (55+55*cityj, 50+55*cityi, 50, 50))
			draw_citylevel(Display, blue, city[6], cityi, cityj)	
			write_toll(Display, field, cities, city[0], red)
		elif city[1] == 1:
			pygame.draw.rect(Display, grey, (55+55*cityj, 50+55*cityi, 50, 50))
			draw_citylevel(Display, red, city[6], cityi, cityj)	
			write_toll(Display, field, cities, city[0], blue)	
		if city[0] in specialpos:
			pygame.draw.rect(Display, black, (55+55*field[city[0]][1], 50+55*field[city[0]][0], 50, 50))
			if city[0] == 0:
				textmaker(Display, 395, 390, 30, 30, 'Start', (255,255,255), 20, 0)		
	pygame.display.update()
	
	
def draw_playerpos(Display, field, cities, players, specialpos, blue, red, P1color, P2color):
	for player in players:
		playerpos = player[2]
		playeri = field[playerpos][0]
		playerj = field[playerpos][1]
		if player[0] == 0:
			pygame.draw.circle(Display, P1color, [80+55*playerj, 75+55*playeri], 10, 0)
		elif player[0] == 1:
			pygame.draw.circle(Display, P2color, [80+55*playerj, 75+55*playeri], 10, 0)
		if playerpos not in specialpos:	
			if cities[playerpos][1] == 0:
				write_toll(Display, field, cities, playerpos, red)
			if cities[playerpos][1] == 1:
				write_toll(Display, field, cities, playerpos, blue)
	pygame.display.update()

# Draws Cities according to player and citylevel	
def draw_citylevel(Display, color, level, i, j):
	if level == 1:
		pygame.draw.rect(Display, color,(55+55*j, 50+55*i, 15,15))
	elif level == 2:
		pygame.draw.rect(Display, color,(55+55*j, 50+55*i, 25,25))	
	elif level == 3:
		pygame.draw.rect(Display, color,(55+55*j, 50+55*i, 37, 37))
	elif level == 4:
		pygame.draw.rect(Display, color,(55+55*j, 50+55*i, 50, 50))	
		
		
def levelup_cities(Display, field, players, CP, cities, specialpos, playerpos, playerposold, black, grey, red, blue):
	for e in cities:
		if e[1] == CP:
			if e[6] != 4 and e[6] < 5:
				e[6] += 1
			citypos = e[0]
			i = field[citypos][0]
			j = field[citypos][1]
			# Update tolls
			cities = calc_toll(cities, playerpos, e[2], e[4], e[6])
			# Update city icons
			if CP == 0:
				color1 = blue
				color2 = red
			else:
				color1 = red
				color2 = blue
			pygame.draw.rect(Display,grey,(55+55*j,50+55*i,50,50))		
			draw_citylevel(Display, color1, e[6], i, j)
			# Remark player position
			if e[0] == playerpos:
				if CP == 0:
					pygame.draw.circle(Display, (150,150,255), [80+55*j, 75+55*i], 10, 0)	
				elif CP == 1:
					pygame.draw.circle(Display, (255,150,150), [80+55*j, 75+55*i], 10, 0)		
			# Toll banner
			textmaker(Display, 65+55*j,54+55*i, 30, 30, str(round(e[3],1)), color2, 15, 0)
			textmaker(Display, 65+55*j,70+55*i, 30, 30, str(round(e[4],1)) + 'x', color2, 15, 0)				
	pygame.display.update()
	return cities, players

	
# Calculates tolls on cities	
def calc_toll(cities, playerpos, basetoll, citymult, level):
	if level == 1:
		cities[playerpos][3] = basetoll * citymult * level
	elif level == 2:
		cities[playerpos][3] = basetoll * citymult * level*0.75	
	elif level == 3:
		cities[playerpos][3] = basetoll * citymult * level*0.9	
	elif level == 4:
		cities[playerpos][3] = basetoll * citymult * level*1.1		
	return cities
	
	
# Switch to other player
def switch_players(Display, CP, double, red, blue):
	pygame.draw.rect(Display, (225,225,250),(180,260,130,35))
	if CP == 0 and double != True:
		CP = 1	
		textmaker(Display, 230, 260, 30, 30, 'Player: '+str(CP+1), red, 30, 0)
	elif CP == 1 and double != True:
		CP = 0
		textmaker(Display, 230, 260, 30, 30, 'Player: '+str(CP+1), blue, 30, 0)
	elif double == True:
		if CP == 0:
			textmaker(Display, 230, 260, 30, 30, 'Player: '+str(CP+1), blue, 30, 0)
		elif CP == 1:
			textmaker(Display, 230, 260, 30, 30, 'Player: '+str(CP+1), red, 30, 0)
	roll = None
	print()
	print()
	pygame.display.update()
	return CP, roll

	
def end_game(Display, clock, CP, bgcolor, black, grey, lightgrey, red, blue):
	print()
	print()
	color = bgcolor
	crashed = False
	flash = 'on'
	pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
	endevent = pygame.USEREVENT + 1
	endevent2 = pygame.event.Event(endevent)
	pygame.event.post(endevent2)	
	while not crashed:
		for event in pygame.event.get():
			Display.fill(bgcolor)
			# Check if mouse is above buttons
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
			
			# Replay or exit 
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
				
				
# Text related functions	
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
		
# Write tolls
def write_toll(Display, field, cities, pos, color):
	textmaker(Display, 65+55*field[pos][1], 54+55*field[pos][0], 30, 30, str(round(cities[pos][3],1))	    , color, 15, 0)
	textmaker(Display, 65+55*field[pos][1], 70+55*field[pos][0], 30, 30, str(round(cities[pos][4],1)) + 'x' , color, 15, 0)	
	
def textmaker(Display, x, y, w, h, msg, color, size, font):
	if font == 0:
		smallText = pygame.font.Font("freesansbold.ttf",size)
	elif font == 1:
		smallText = pygame.font.SysFont("Times New Roman",size)
	textSurf, textRect = text_objects(msg, smallText,color)
	textRect.center = ((x+(w/2)), (y+(h/2)))
	Display.blit(textSurf, textRect)	