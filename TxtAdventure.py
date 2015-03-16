from sys import exit
import random

#learn about classes and how to better organize all of these functions

class room(object):
#for now every room will have the same options of right left straight treasure monsters
#how to organize?
	def __init__(self):
	#on class room initialization print "you enter -RANDOM- room"
		print "You enter the %s room."
	
#class lincoln(room):
	print "You enter the Lincoln Room.  You immediately get a headache."
	
#class Bed(room):
	print "You enter the bedroom."
	
#class Board(room):
	print "You enter the boardroom."
	
#class Blue(room):
	print "You enter the Blue Room."
	

#one monster per room
class monsters(object):
	def __init__(self):
		pass
	
#class Zombie_mario(monsters):
	print "You encounter Zombie Mario!"
	
#class Upside_down_triangle_man(monsters):
	print "You encounter Upside-down Triangle Man!"
	
#class A_giant_chinese_crested_dog(monsters):
	print "You encounter A Giant Chinese Crested Dog!"
	
#class A_whale_with_telekinesis(monsters):
	print "You encounter A Whale with telekinesis!"
	
	
#multiple minions per room
class minions(object):
	def __init__(self):
		pass
		
#class Paper_mummies(minions):
	print "You encounter Paper Mummies!"
	
#class Walking_puffer_fish(minions):
	print "You encounter a walking puffer fish!"
	
#class Pygmy_white_trash_girls(minions):
	print "You encounter pygmy white trash girls!"
	
#class Snapping_petunias(minions):
	print "You encounter some snapping Petunias!"
	
#Instead of trying to use lists, try to use dictionaries and combine keys
#rooms = {lincoln_room:, Bedroom:, Boardroom:, Blue_room:}	

#rooms = [lincoln_room, Bedroom, Boardroom, Blue_room]
#this is a list of functions with the () removed to keep them from running when the list is read. The () are added in the random room chooser in the new_room function
#monsters = [Zombie_mario, Upside_down_triangle_man, A_giant_chinese_crested_dog, A_whale_with_telekinesis]
#minions = [Paper_mummies, Walking_puffer_fish, Pygmy_white_trash_girls, Snapping_petunias]

#room_weight = 1
#monster_weight = 1
#minion_weight = 5
#Master = (room_weight * rooms) + (monster_weight * monsters) + (minion_weight * minions)

#print Master
	
#def new_room():
	while  len(rooms) > 0:
	
		rooms.pop(rooms.index(random.choice(rooms)))()
		#random.choice() - randomly chooses an element from a list
		#rooms.index() - requires an element in a list as input and returns its location in the list
		#rooms.pop() - requires the location of an element in a list as input, takes that element and returns it and then removes it from the list
		#this whole sequence returns the name of a function and then the () are added at the end in order to run it
	
		print "You see three doors and a treasure chest"
		print "Which way would you like to go?"
	
		choice = raw_input("\n 1. Right \n 2. Left \n 3. Straight \n 4. Treasure Chest \n >")
	
		if "1" in choice or "2" in choice or "3" in choice:
			new_room()
		elif "4" in choice:
			treasure()
		else:
			dead("Excellent Choice.")
			
	else:
		dead("Congratulations there are no more rooms!")
				
#def treasure():#need a way to return to room after looking inside treasure chest
	print "You open the treasure chest and look inside."
	
#def dead(why):

	print why, "You've died! Finally some peace for the both of us."
	print "Play again?"
	
	choice = raw_input("Y or N \n >")
	
	if "y" in choice or "Y" in choice:
		new_room()
	else:
		exit(0)
	
def start():
	new_room()
	
#start()