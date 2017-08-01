# -*- coding:utf-8 -*-

from sys import exit

end1 = "You're already dead."
end2 = '''
The room is empty.
The door is closed.
You can not find a way to get away from there.
You dead.
'''
end3 = '''
The ghost cause you to lose yourself.
You became a ghost too.
'''
end4 = '''
The enemy is too strong, You can not kill it.
Even though,the ghost appreciate you for your trying.
It self-destruction with enemy, you are alive.
'''

def room3():
	print 'The ghost show you why it dead and wants you to revenge for it.'
	print 'You will:'
	print "1 help it."
	print '2 say no.'
	print "Please input the number for your choose: "
	
	next = int(raw_input('> '))
	if next == 1:
		print end4
	elif next == 2:
		print end3
	else:
		print "The ghost eat you step by step."

def room2():
	print 'This room is rely on past of the ghost.'
	print 'You see:'
	print "1 a lot of dead person."
	print '2 a lot of money.'
	print '3 a lot of water.'
	print "Please input the number for your choose: "
	
	next = int(raw_input('> '))
	if next == 1 or next ==3:
		room3()
	elif next == 2:
		print end3
	else:
		print "The ghost eat you step by step."

def room1():
	print "There is a ghost here."
	print "You can:"
	print "1 Run away."
	print '2 Kill it.'
	print '3 Talk with it.'
	print "Please input the number for your choose: "
	
	next = int(raw_input('> '))
	if next == 1:
		print end1
	elif next == 2:
		print end2
	elif next == 3:
		room2()
	else:
		print "The ghost eat you step by step."
		
room1()
