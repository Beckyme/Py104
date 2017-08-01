# -*- coding:utf-8 -*-

'''
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count,f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
print current_line

current_line += 1
print_a_line(current_line, current_file)
print current_line

current_line += 1
print_a_line(current_line, current_file)
print current_line
'''


def number(a, b, c):
	print "Now you tpye:", a,b,c


print "Now please type 3 numbers (arithmetic progression) here."
print "I will tell you the next number."
a = float(raw_input("The first number is: "))
b = float(raw_input("The second number is: "))
c = float(raw_input("The third number is: "))
number(a,b,c)

current_number = c
current_number += c -b
print "The next number is:", current_number