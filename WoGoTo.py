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
field = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],
		 [1,6],[2,6],[3,6],[4,6],[5,6],[6,6],
		 [6,5],[6,4],[6,3],[6,2],[6,1],[6,0],
		 [5,0],[4,0],[3,0],[2,0],[1,0]]	
		 
display_width = 500
display_height = 500	
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (150, 150, 150)
white = (255, 255, 255)
cities = []
cityints = []
specials = []
players = []
	 
#create empty cities
for i in range(fieldnum):
	if i not in specialpos:
		#number, owner, toll, multiplicator, betted?, Citylevel
		cities.append([i, 2, 100+i*1.04, 1, False, 1])
		cityints.append(i)
	else:	
		#else initialize special fields
		cities.append([i, 2, 100+i*1.04, 1, False, 1])
		

#print(cityints)

for i in range(playernum):
	#number, money, pos
	players.append([i, playermoney, 0])

#random start player
CP = np.random.randint(0,1)



######################################################################
######################################################################



#programm start	
pygame.init()
pygame.font.init()
Display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('WoGoTo')#Fenstername
clock = pygame.time.Clock() 
crashed = False
funcs.initfield(Display, field, specialpos, black, gray, display_width)

#run game loop / #play a round
while not crashed:	


	#for e in pygame.event.get():
	#	if e.type == 
	
	
	print('Player '+ str(CP+1) + ' turn:')
	#roll dice
	diceroll = random.choice(dicenums)
	money = players[CP][1]
	playerposold = players[CP][2]
	playerpos = playerposold + diceroll
	if playerpos > fieldnum-1:
		playerpos = playerpos - fieldnum
	players[CP][2] = playerpos
	print('Oldpos: ' + str(playerposold) + ', Diceroll: ' + str(diceroll) + ', Newpos: ' + str(playerpos))
	
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
				toll = cities[playerpos][2]
				cities[playerpos][4] = True
				cities[playerpos][3] = citymult
				cities[playerpos][2] = citymult * toll
				funcs.updatefield(Display, field, cities, players, specialpos, CP, playerpos, playerposold, black, red, blue, )
				print(cities[playerpos][3])
				print('Bet on City ' + str(playerpos) + ', toll: ' + str(cities[playerpos][3]*cities[playerpos][2]))	
		elif currentowner != CP and currentowner != 2:
			#enemy city -> pay
			citymult = cities[playerpos][3]
			toll = cities[playerpos][2]
			money = money - (toll*citymult)
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
		print('Player '+str(CP+1)+' lost')
		crashed = True
	else:
		players[CP][1] = money
		print('Player '+str(CP+1)+' Money: '+ str(round(money,2)))
	
	#switch players
	if CP == 0:
		CP = 1
	else:
		CP = 0
	
	pygame.display.update() #alternativ .flip , auch mit einzelnen Frames moeglich
	pygame.event.pump() 
	clock.tick(0.5) #frames per second
	print()
	print()

##keep window open
#while not crashed:	
#	for event in pygame.event.get():
#		if event.type == MOUSEBUTTONUP:
#			crashed = True
#		pygame.event.wait()
		
pygame.quit() #zuerst pygame und dann python schliesem
quit()