# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename,"r+")

print "This is the file %r 's  content:" % filename
print txt.read()

print "Please write something to celebrate the New Year."

line1 = raw_input("Wish1: ")
line2 = raw_input("Wish2: ")
line3 = raw_input("Wish3: ")

print "I'm going to write these to the file."

txt.seek(0,2)

txt.write('\n{0}\n{1}\n{2}\n'.format(line1,line2,line3))
txt.write('%s\n%s\n%s\n' %(line1,line2,line3))

print "Then I'll closed this file."
print txt.close()