#rooms = [lincoln_room, Bedroom, Boardroom, Blue_room]
#this is a list of functions with the () removed to keep them from running when the list is read. The () are added in the random room chooser in the new_room function
#monsters = [Zombie_mario, Upside_down_triangle_man, A_giant_chinese_crested_dog, A_whale_with_telekinesis]
#minions = [Paper_mummies, Walking_puffer_fish, Pygmy_white_trash_girls, Snapping_petunias]


#-----------------------------------------------------------------------------------------------------

#LPTHW Ex43 is confusing to me because the classes seem to call each other and there are no loops. 
#The classes seem to call each other because of the way the game process is organized.


#The class Scene only defines an enter function.  This enter function only runs if a scene is entered that is not yet configured
#All of the configured scenes have enter functions that will override this enter function


#The Engine class controls how the scenes rotate and when they rotate.

#The Engine class starts with an __init__ function which passes self, and scene_map and this function sets self.scene_map = scene_map
#this kind of __init__ seems to happen a lot and I don't understand it.
#it means from self get scene_map and set it to scene_map.  I just don't know why you need to set scene_map to self.scene_map

#The main function in Engine is the play function and it passes the self parameter
#At first it sets current_scene to self.scene_map.opening_scene().  Which means from self.scene_map get the function opening_scene?
#opening_scene comes from the map class.  How do you get the opening_scene function from self.scene_map?
#Oh, to start the game we set a_map to Map('central_corridor'), then we set a_game to class Engine(a_map) which gives Engine
#the properties of Map.  This sequence kind of combines map and engine classes, or Engine can call from Map.  Why not just combine them from the get go?
#The way that Engine is set up you always have to combine Map(Engine) for it to work.
#The function play sets last_scene to self.scene_map.next_scene('finished'),
#the dot notation is kind of like the \ folder notation in that moving from left to right you see the greatest
#folder then \ a folder in that folder and then \ and so on 
#the dot notation says from this . get this . and the this ., you end at the smallest thing you want on the right
#The play function then starts a while loop with the statement current_scene != last_scene,
#so while the definition current_scene does not equal the definition last scene (as long as it's not the last scene)
#then the while loop states that next_scene_name is equal to from current_scene get the enter function()(which is in every "Scene" class)
#then enter function is basically the story part of the game.
#after next_scene_name current_scene is defined in the while loop as equal to self.scene_map.next_scene(next_scene_name)
#so current scene will be, from self get scene_map, from scene_map get next_scene and pass next_scene_name
#can I put a print statement somewhere to help me understand what is going on while the program is running?
#self is a place holder for the variable name of the instance of the class (a=Class(), here self is a place holder for a.)
#instead of self.scene_map you would call a.scene_map
class room(object):
#for now every room will have the same options of right left straight treasure monsters
#how to organize?
	def __init__(self):
	#on class room initialization print "you enter -RANDOM- room"
		roomed = []
		if i in a:
			#choose another room
		else:
			#enter the room
			
			
			print "You enter the ? room."
			roomed.append(i)
			
			
class engine(object):
	
			
		
		
		
class monsters(object):
	def __init__(self):
		pass
	
	
	
class minions(object):
	def __init__(self):
		pass
		
		
#roomlist = [room() for i in range(4)]
#print roomlist
