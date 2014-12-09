class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])
				   
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#is this calling the objects happy_bday and bulls_on_parade in the form of the function sing_me_a_song
#?  Which is a part of the the class song.  happy_bday and bulls_on_parade are being passed to the
# the function as the variable lyrics.