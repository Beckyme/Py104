# -*- coding:utf-8 -*-
def circle(a, b):
	print "If we have a cicle, we know the radius is %.2f." % a
	return 2 * a * b
	
perimeter = circle(15,3.1415)

print "The perimeter is %.3f." % perimeter

def circle_new(a, b):
	print "If you have a cicle, you can decide the radius you want."
	return a * b * b
	
area = circle(float(raw_input("Please type the radius you want: ")), 3.1415)

print "The area is %.3f." % area

print ""
def program(a, b):
	print "You know the first program in the word?"
	return a + b
	
programmer = program("hello ", "word!")

print "The program is: %s" % programmer

def operation(a, b, c, d, e):
	print "I want to know the answer of a operation."
	return c
	
a = float(raw_input("Please type the first number: "))
b = float(raw_input("Please type the second number: "))
c = float(raw_input("Please type the third number: "))
d = float(raw_input("Please type the forth number: "))
e = a + b / c * d

print "The answer is %.2f." % e

def format_new(dd, ee):
	return dd / ee

def format(aa, bb, cc):
	return aa + bb - cc

the_answer = format(24, format_new(34, 100), 1023)

print "The answer of 24 + 34 / 100 -1023 is: ", the_answer

def other(aaa, bbb, ccc, ddd):
	return aaa + bbb / ccc - ddd
	
coo = other(24, 34, 100, 1023)
print "So, the answer of 24 + 34 / 100 -1023 is: %.2f." % coo

def what(ab, cd, ef, gh):
	return ab + cd / ef - gh

ab = float(raw_input("Please type the first number: "))
cd = float(raw_input("Please type the second number: "))
ef = float(raw_input("Please type the third number: "))
gh = float(raw_input("Please type the forth number: "))

co = what(ab, cd, ef, gh)
print "So, you want to know %.2f + %.2f / %.2f - %.2f is " % (ab, cd, ef, gh, ), co, "."