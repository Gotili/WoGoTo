from __future__ import absolute_import, division, print_function
import pygame
import random
import numpy as np
from PIL import Image
import basicfuncs as funcs

#initialize and start WoGoTo
######################################################################	
######################################################################	

playernum = 2
citynum = 20
specialf = 4
playermoney = 500

fieldnum = citynum + specialf
specialpos = [0,6,12,18]
dicenums = [2,3,4,5,6,7,8,9,10,11,12]

#dicepossibilities
ld =  [[1,1], [1,2], [2,1], [2,2]]  
lm =  [[1,4], [4,1], [2,3], [3,2], [3,3], [3,4], [4,3], [2,5], [5,2], [6,1], [1,6]]	  
hm =  [[3,4], [4,3], [2,5], [5,2], [6,1], [1,6], [2,6], [6,2], [3,5], [5,3], [4,4],
	   [6,3], [3,6], [5,4], [4,5]]
hd =  [[6,4], [4,6], [5,5], [6,5], [5,6], [6,6]]
	 
field = [[6,6],[6,5],[6,4],[6,3],[6,2],[6,1],[6,0],
		 [5,0],[4,0],[3,0],[2,0],[1,0],[0,0],
		 [0,1],[0,2],[0,3],[0,4],[0,5],[0,6],
		 [1,6],[2,6],[3,6],[4,6],[5,6]]
		 
display_width = 493
display_height = 475	
bgcolor = (225,225,250)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (150, 150, 150)
lightgray = (210, 210, 210)
white = (255, 255, 255)
exitted = False
crashed = False


######################################################################
######################################################################
	

while not exitted:
	cities = []
	cityints = []
	specials = []
	players = []	
	crashed = False
	double = False
	doublecnt = 0
	#create empty cities
	for i in range(fieldnum):
		if i not in specialpos:
			#number, owner, toll, multiplicator, betted?, Citylevel
			cities.append([i, 2, 100+i*1.04, 1, False, 1])
			cityints.append(i)
		else:	
			#else initialize special fields
			cities.append([i, 2, 100+i*1.04, 1, False, 1])		
	for i in range(playernum):
		#number, money, pos
		players.append([i, playermoney, 0])

	#programm start	
	pygame.init()
	pygame.font.init()
	Display = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('WoGoTo') #Fenstername
	clock = pygame.time.Clock() 
	funcs.initfield(Display, field, specialpos, black, gray, display_width, bgcolor)
	CP = np.random.randint(0,2)	
	if CP == 0:
		funcs.textmaker(Display, 230, 280, 30, 30, 'Player: '+str(CP+1), blue, 30, 0)
	else:
		funcs.textmaker(Display, 230, 280, 30, 30, 'Player: '+str(CP+1), red, 30, 0)
	pygame.display.update()
	
	#random start player
	
	#run game loop / #play a round
	while not crashed:	
		for event in pygame.event.get():
			#button interaction
			mouse = pygame.mouse.get_pos()
			if 130+50 > mouse[0] > 130 and 190+50 > mouse[1] > 190:
				pygame.draw.rect(Display, lightgray,(130,190,50,50))
				funcs.textmaker(Display, 140, 201, 30, 30, '2-4', black, 17, 0)
			else:
				pygame.draw.rect(Display, gray,(130,190,50,50))
				funcs.textmaker(Display, 140, 201, 30, 30, '2-4', black, 17, 0)
				
			if 190+50 > mouse[0] > 190 and 190+50 > mouse[1] > 190:
				pygame.draw.rect(Display, lightgray,(190,190,50,50))
				funcs.textmaker(Display, 200, 201, 30, 30, '5-7', black, 17, 0)
			else:
				pygame.draw.rect(Display, gray,(190,190,50,50))
				funcs.textmaker(Display, 200, 201, 30, 30, '5-7', black, 17, 0)		
			if 250+50 > mouse[0] > 250 and 190+50 > mouse[1] > 190:
				pygame.draw.rect(Display, lightgray,(250,190,50,50))
				funcs.textmaker(Display, 260, 201, 30, 30, '7-9', black, 17, 0)			
			else:
				pygame.draw.rect(Display, gray,(250,190,50,50))	
				funcs.textmaker(Display, 260, 201, 30, 30, '7-9', black, 17, 0)				
			if 310+50 > mouse[0] > 310 and 190+50 > mouse[1] > 190:
				pygame.draw.rect(Display, lightgray,(310,190,50,50))
				funcs.textmaker(Display, 319, 201, 30, 30, '10-12', black, 17, 0)				
			else:
				pygame.draw.rect(Display, gray,(310,190,50,50))	
				funcs.textmaker(Display, 319, 201, 30, 30, '10-12', black, 17, 0)				
			pygame.display.update()
			
			# Roll dice by clicking mouse1
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if 130+50 > mouse[0] > 130 and 190+50 > mouse[1] > 190:
						pygame.draw.rect(Display, gray,(130,190,50,50))
						funcs.textmaker(Display, 140, 201, 30, 30, '2-4', black, 20, 0)
						roll = random.choice(ld)
					elif 190+50 > mouse[0] > 190 and 190+50 > mouse[1] > 190:
						pygame.draw.rect(Display, gray,(190,190,50,50))
						funcs.textmaker(Display, 200, 201, 30, 30, '5-7', black, 17, 0)
						roll = random.choice(lm)
					elif 250+50 > mouse[0] > 250 and 190+50 > mouse[1] > 190:
						pygame.draw.rect(Display, gray,(250,190,50,50))	
						funcs.textmaker(Display, 260, 201, 30, 30, '7-9', black, 17, 0)	
						roll = random.choice(hm)
					elif 310+50 > mouse[0] > 310 and 190+50 > mouse[1] > 190:
						pygame.draw.rect(Display, gray,(310,190,50,50))	
						funcs.textmaker(Display, 319, 201, 30, 30, '10-12', black, 17, 0)	
						roll = random.choice(hd)
					else:
						roll = None
					diceroll = roll #random.choice(dicenums)
					pygame.display.update()
					gameevent = pygame.USEREVENT + 1
					gameevent2 = pygame.event.Event(gameevent)
					pygame.event.post(gameevent2)
				
			# process game
			if event.type == 25 and roll != None:
				print('Player '+ str(CP+1) + ' turn:')
				money = players[CP][1]
				playerposold = players[CP][2]
				playerpos = playerposold + diceroll[0] + diceroll[1]
				
				# Dice double?
				if diceroll[0] == diceroll[1]:
					print('DOUBLE - Roll again!')
					double = True
					doublecnt += 1
					if doublecnt == 3:
						print('Triple double? Going to jail!')
						double = False
						doublecnt = 0
						CP, roll = funcs.switch_players(Display, CP, double, red, blue)
						continue
				else:
					double = False
					doublecnt = 0
					
				if playerpos > fieldnum-1:
					playerpos = playerpos - fieldnum				
					funcs.levelup_cities(Display, field, players, CP, cities, specialpos, playerpos, playerposold, black, red, blue)
				
				# set new player position
				players[CP][2] = playerpos
				print('Oldpos: ' + str(playerposold) + ', Diceroll: ' + str(diceroll[0]) + '-' + str(diceroll[1]) + ': ' + str(diceroll[0]+diceroll[1]) +', Newpos: ' + str(playerpos))
				
				# If landed on City -> Check
				if playerpos in cityints:
					currentowner = cities[playerpos][1]
					#print(currentowner)
					if currentowner == 2 and playerpos not in specialpos:
						#take empty city
						cities[playerpos][1] = CP
						funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, red, blue, )
						print('City ' + str(playerpos) + ' taken, toll: ' + str(cities[playerpos][3]*cities[playerpos][2]))	
					elif currentowner == CP:
						#own city -> bet
						if cities[playerpos][4] == False:
							citymult = 4
							cities[playerpos][4] = True
							toll = cities[playerpos][2]
							level = cities[playerpos][5]
							cities[playerpos][3] = citymult
							if level == 1:
								cities[playerpos][2] = citymult * toll * level
							else:
								cities[playerpos][2] = citymult * toll * level*0.75
								
							funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, red, blue, )
							print(cities[playerpos][3])
							print('Bet on City ' + str(playerpos) + ', toll: ' + str(cities[playerpos][2]))	
					elif currentowner != CP and currentowner != 2:
						#enemy city -> pay
						citymult = cities[playerpos][3]
						toll = cities[playerpos][2]
						money = money - toll
						funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, red, blue, )
						print('Paid ' + str(round(toll*citymult,2)))
								
				elif playerpos in specialpos:
					print('Yay free 200')
					money = money + 200
					players[CP][1] = money
					funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, red, blue, )
				
				# check if bankrupt:
				if money < 0:
					print()
					print()
					crashed = True
					break
				else:
					players[CP][1] = money
					print('Player '+str(CP+1)+' Money: '+ str(round(money,2)))
				
				#switch players
				CP, roll = funcs.switch_players(Display, CP, double, red, blue)
	
				#refresh event queue and display
				pygame.display.update() #alternativ .flip , auch mit einzelnen Frames moeglich
				pygame.event.pump()
				pygame.event.clear()
				clock.tick(30) #frames per second		
	exitted = funcs.end_game(Display, clock, CP, bgcolor, black, gray, lightgray, red, blue)

	
pygame.quit() #zuerst pygame und dann python schließen
quit()