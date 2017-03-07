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
ld =  [[1,1], [1,2], [2,1], [2,2], [1,3], [3,1]]  
lm =  [[1,4], [4,1], [2,3], [3,2], [3,3], [3,4], [4,3], [2,5], [5,2], [6,1], [1,6]]	  
hm =  [[3,4], [4,3], [2,5], [5,2], [6,1], [1,6], [2,6], [6,2], [3,5], [5,3], [4,4],
	   [6,3], [3,6], [5,4], [4,5]]
hd =  [[6,4], [4,6], [5,5], [6,5], [5,6], [6,6]]

gesdice = []
gesdice.extend(ld)
gesdice.extend(lm)
gesdice.extend(hm)
gesdice.extend(hd)
	 
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
grey = (150, 150, 150)
lightgrey = (210, 210, 210)
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
	tdouble = False
	doublecnt = 0
	# Create empty cities
	for i in range(fieldnum):
		if i not in specialpos:
			# Number, Owner, Base toll, Current toll, Multiplicator, Betted?, Citylevel
			cities.append([i, 2, 100+i*1.04, 100+i*1.04, 1, False, 1])
			cityints.append(i)
		else:	
			# Else initialize special fields
			cities.append([i, 2, 100+i*1.04, 100+i*1.04, 1, False, 1])		
	for i in range(playernum):
		# Number, Money, Position, Dicecontrol
		players.append([i, playermoney, 0, 0.5])

	# Programm start	
	pygame.init()
	pygame.font.init()
	Display = pygame.display.set_mode((display_width,display_height))
	pygame.display.set_caption('WoGoTo') #Fenstername
	clock = pygame.time.Clock() 
	# Initialize field
	funcs.initfield(Display, field, specialpos, black, grey, display_width, bgcolor)
	# Randomize start player
	CP = np.random.randint(0,2)	
	if CP == 0:
		pygame.draw.circle(Display, (150,150,255), [80+55*6,75+55*6], 10, 0)
		funcs.textmaker(Display, 230, 260, 30, 30, 'Player: '+str(CP+1), blue, 30, 0)
	else:
		pygame.draw.circle(Display, (255,150,150), [80+55*6,75+55*6], 10, 0)
		funcs.textmaker(Display, 230, 260, 30, 30, 'Player: '+str(CP+1), red, 30, 0)
	pygame.display.update()
	
	
	# Run game loop / Play a round
	while not crashed:	
		for event in pygame.event.get():
			# Interactive buttons
			mouse = pygame.mouse.get_pos()
			if 130+50 > mouse[0] > 130 and 190+50 > mouse[1] > 190:
				pygame.draw.rect(Display, lightgrey,(130,190,50,50))
				funcs.textmaker(Display, 140, 201, 30, 30, '2-4', black, 17, 0)
			else:
				pygame.draw.rect(Display, grey,(130,190,50,50))
				funcs.textmaker(Display, 140, 201, 30, 30, '2-4', black, 17, 0)	
			if 190+50 > mouse[0] > 190 and 190+50 > mouse[1] > 190:
				pygame.draw.rect(Display, lightgrey,(190,190,50,50))
				funcs.textmaker(Display, 200, 201, 30, 30, '5-7', black, 17, 0)
			else:
				pygame.draw.rect(Display, grey,(190,190,50,50))
				funcs.textmaker(Display, 200, 201, 30, 30, '5-7', black, 17, 0)		
			if 250+50 > mouse[0] > 250 and 190+50 > mouse[1] > 190:
				pygame.draw.rect(Display, lightgrey,(250,190,50,50))
				funcs.textmaker(Display, 260, 201, 30, 30, '7-9', black, 17, 0)			
			else:
				pygame.draw.rect(Display, grey,(250,190,50,50))	
				funcs.textmaker(Display, 260, 201, 30, 30, '7-9', black, 17, 0)				
			if 310+50 > mouse[0] > 310 and 190+50 > mouse[1] > 190:
				pygame.draw.rect(Display, lightgrey,(310,190,50,50))
				funcs.textmaker(Display, 319, 201, 30, 30, '10-12', black, 17, 0)				
			else:
				pygame.draw.rect(Display, grey,(310,190,50,50))	
				funcs.textmaker(Display, 319, 201, 30, 30, '10-12', black, 17, 0)				
			pygame.display.update()
			
			# Roll dice by clicking mouse1
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:			
					if 130+50 > mouse[0] > 130 and 190+50 > mouse[1] > 190:
						pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
						pygame.draw.rect(Display, grey,(130,190,50,50))
						funcs.textmaker(Display, 140, 201, 30, 30, '2-4', black, 20, 0)
						roll = random.choice(ld)
					elif 190+50 > mouse[0] > 190 and 190+50 > mouse[1] > 190:
						pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
						pygame.draw.rect(Display, grey,(190,190,50,50))
						funcs.textmaker(Display, 200, 201, 30, 30, '5-7', black, 17, 0)
						roll = random.choice(lm)
					elif 250+50 > mouse[0] > 250 and 190+50 > mouse[1] > 190:
						pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
						pygame.draw.rect(Display, grey,(250,190,50,50))	
						funcs.textmaker(Display, 260, 201, 30, 30, '7-9', black, 17, 0)	
						roll = random.choice(hm)
					elif 310+50 > mouse[0] > 310 and 190+50 > mouse[1] > 190:
						pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
						pygame.draw.rect(Display, grey,(310,190,50,50))	
						funcs.textmaker(Display, 319, 201, 30, 30, '10-12', black, 17, 0)	
						roll = random.choice(hd)
					else:
						roll = None
					
					# Dice Control? 
					if roll != None:
						randomnum = float(np.random.rand(1,1))
						print('Player '+ str(CP+1) + ' turn:')
						pygame.draw.rect(Display, bgcolor,(125,308,240,50))
						if randomnum < players[CP][3]:
							print('DICE CONTROL')
							diceroll = roll
							if CP == 0:
								funcs.textmaker(Display, 170, 310, 30, 30, 'DICE CONTROL', blue, 15, 0)
								funcs.textmaker(Display, 170, 330, 30, 30, str(diceroll[0])+'-'+str(diceroll[1]), blue, 15, 0)
							else:
								funcs.textmaker(Display, 170, 310, 30, 30, 'DICE CONTROL', red, 15, 0)
								funcs.textmaker(Display, 170, 330, 30, 30, str(diceroll[0])+'-'+str(diceroll[1]), red, 15, 0)						
						else:
							print('DICE RANDOM')
							diceroll = random.choice(gesdice)
							if CP == 0:
								funcs.textmaker(Display, 170, 310, 30, 30, 'DICE RANDOM', blue, 15, 0)
								funcs.textmaker(Display, 170, 330, 30, 30, str(diceroll[0])+'-'+str(diceroll[1]), blue, 15, 0)
							else:
								funcs.textmaker(Display, 170, 310, 30, 30, 'DICE RANDOM', red, 15, 0)
								funcs.textmaker(Display, 170, 330, 30, 30, str(diceroll[0])+'-'+str(diceroll[1]), red, 15, 0)
					pygame.display.update()
					gameevent = pygame.USEREVENT + 1
					gameevent2 = pygame.event.Event(gameevent)
					pygame.event.post(gameevent2)
				
			# Process game
			if event.type == 25 and roll != None:			
				# Dice double?
				if diceroll[0] == diceroll[1]:
					print('DOUBLE - Roll again!')
					if CP == 0:
						funcs.textmaker(Display, 290, 320, 30, 30, 'DOUBLE', blue, 20, 0)
					else:
						funcs.textmaker(Display, 290, 320, 30, 30, 'DOUBLE', red, 20, 0)
					double = True
					doublecnt += 1
					#if doublecnt == 3:
					#	print('Triple double? Going to jail!')
					#	double = False
					#	doublecnt = 0
					#	CP, roll = funcs.switch_players(Display, CP, double, red, blue)
				else:
					double = False
					doublecnt = 0
				
				# Get some data from player
				money = players[CP][1]
				playerposold = players[CP][2]
				# new player position	
				playerpos = playerposold + diceroll[0] + diceroll[1]
				players[CP][2] = playerpos
				
				# Check if start is passed and level up cities
				if playerpos > fieldnum-1:
					playerpos = playerpos - fieldnum
					players[CP][2] = playerpos			
					cities, players = funcs.levelup_cities(Display, field, players, CP, cities, specialpos, playerpos, playerposold, black, grey, red, blue)
				if playerposold > fieldnum-1:
					playerposold = playerposold - fieldnum
				print('Oldpos: ' + str(playerposold) + ', Diceroll: ' + str(diceroll[0]) + '-' + str(diceroll[1]) + ': ' + str(diceroll[0]+diceroll[1]) +', Newpos: ' + str(playerpos))	
				
				# Check if landed on City 
				if playerpos in cityints:
					currentowner = cities[playerpos][1]
					# City empty -> take
					if currentowner == 2 and playerpos not in specialpos:
						cities[playerpos][1] = CP
						cities, players = funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, grey, red, blue)
						print('City ' + str(playerpos) + ' taken, toll: ' + str(cities[playerpos][3]))	
						
					# Own city -> Try bet	
					elif currentowner == CP:
						if cities[playerpos][5] == False:
							citymult = 3
							cities[playerpos][5] = True
							basetoll = cities[playerpos][2]
							level = cities[playerpos][6]
							cities[playerpos][4] = citymult
							if level == 1:
								cities[playerpos][3] = basetoll * citymult * level
							else:
								cities[playerpos][3] = basetoll * citymult * level*0.75				
							cities, players = funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, grey, red, blue)
							print('Bet on City ' + str(playerpos) + ', toll: ' + str(round(cities[playerpos][3],2)))	
						else:
							print('City ' + str(playerpos) + ' already boosted.. toll: ' + str(round(cities[playerpos][3],2)))
					# Enemy city -> pay		
					elif currentowner != CP and currentowner != 2:
						toll = cities[playerpos][3]
						money = money - toll
						cities, players = funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, grey, red, blue)
						print('Paid ' + str(round(toll,2)))
								
				elif playerpos in specialpos:
					print('Yay free 200')
					money = money + 200
					players[CP][1] = money
					cities, players = funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, grey, red, blue)
				
				# Check if bankrupt:
				if money < 0:
					print()
					print()
					players[CP][2] = 0
					crashed = True
					break
				else:
					players[CP][1] = money
					print('Player '+str(CP+1)+' Money: '+ str(round(money,2)))
				
				# Switch players
				CP, roll = funcs.switch_players(Display, CP, double, red, blue)
	
				# Refresh event queue and display
				pygame.display.update() # Alternativ .flip
				pygame.event.pump()
				pygame.event.clear()
				pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
				clock.tick(30) # Frames per second		
	exitted = funcs.end_game(Display, clock, CP, bgcolor, black, grey, lightgrey, red, blue)

# Close Process	
pygame.quit() 
quit()