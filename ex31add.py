# -*- coding:utf-8 -*-
print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

prompt = "> "
door = raw_input(prompt)

if door == "1":
	print "There's a red box in the room.  What do you do?"
	print "1. Open this box."
	print "2. ignor the box, and go away."
	
	room1 = raw_input(prompt)
	
	if room1 == "1":
		print "There is a knife in the box. What do you do?"
		print "1. Keep search the box."
		print "2. Take the knife."
			
		box1 = raw_input(prompt)
			
		if box1 == "1":
			print "You find some coin. So lucky!"
				
		elif box1 == "2":
			print "A snake is under the knife and bite you. You died."
				
		else:
			print "You waste your time off. You died."
		
	elif room1 == "2":
		print "You find some water and foods. So lucky!"
	else:
		print "Well, %s is not a good idea, game over." % room1
		
elif door == "2":
	print "You stare into the endless abyss at Cthuhlu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input(prompt)
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"
		
else:
	print "You stumble around and fall on a knife and die.  Good job!"