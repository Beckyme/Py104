robots = 52
rabbits = 10
cats = 15
dogs = 13
foods = 30
oil = 50

if foods >= cats and robots >= cats:
	print "We creat some robots to feed cats."
elif foods < cats and robots < cats:
	print "We need to purchase some food to feed cat."
else:
	print "We are confused."
	
robots -= cats
foods -= cats

if foods >= rabbits and robots >= rabbits:
	print "We creat some robots to feed rabbits."
elif foods < rabbits and robots < rabbits:
	print "We need to purchase some food to feed rabbits."
else:
	print "We are confused."
	
robots -= rabbits
foods -= rabbits

if foods >= dogs and robots >= dogs:
	print "We creat some robots to feed dogs."
elif foods < dogs and robots < dogs:
	print "We need to purchase some food to feed dogs."
else:
	print "We are confused."
	
robots += rabbits + cats
print robots

if oil >= robots:
	print "We should maintain robots use oil."
else:
	print "We need purchase some oil to maintain the robots."