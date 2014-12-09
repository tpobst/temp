from sys import exit
import random

#learn about classes and how to better organize all of these functions

def lincoln_room():
	print "You enter the Lincoln Room.  You immediately get a headache."
	
def Bedroom():
	print "You enter the bedroom."
	
def Boardroom():
	print "You enter the boardroom."
	
def Blue_room():
	print "You enter the Blue Room."
	
	
def Zombie_mario():
	print "You encounter Zombie Mario!"
	
def Upside_down_triangle_man():
	print "You encounter Upside-down Triangle Man!"
	
def A_giant_chinese_crested_dog():
	print "You encounter A Giant Chinese Crested Dog!"
	
def A_whale_with_telekinesis():
	print "You encounter A Whale with telekinesis!"
	
	
def Paper_mummies():
	print "You encounter Paper Mummies!"
	
def Walking_puffer_fish():
	print "You encounter a walking puffer fish!"
	
def Pygmy_white_trash_girls():
	print "You encounter pygmy white trash girls!"
	
def Snapping_petunias():
	print "You encounter some snapping Petunias!"
	
#Instead of trying to use lists, try to use dictionaries and combine keys
#rooms = {lincoln_room:, Bedroom:, Boardroom:, Blue_room:}	

rooms = [lincoln_room, Bedroom, Boardroom, Blue_room]
#this is a list of functions with the () removed to keep them from running when the list is read. The () are added in the random room chooser in the new_room function
monsters = [Zombie_mario, Upside_down_triangle_man, A_giant_chinese_crested_dog, A_whale_with_telekinesis]
minions = [Paper_mummies, Walking_puffer_fish, Pygmy_white_trash_girls, Snapping_petunias]

room_weight = 1
monster_weight = 1
minion_weight = 5
Master = (room_weight * rooms) + (monster_weight * monsters) + (minion_weight * minions)

print Master
	
def new_room():
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
				
def treasure():#need a way to return to room after looking inside treasure chest
	print "You open the treasure chest and look inside."
	
def dead(why):

	print why, "You've died! Finally some peace for the both of us."
	print "Play again?"
	
	choice = raw_input("Y or N \n >")
	
	if "y" in choice or "Y" in choice:
		new_room()
	else:
		exit(0)
	
def start():
	new_room()
	
start()