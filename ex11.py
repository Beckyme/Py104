# -*- coding:utf-8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "What lbs you want to transform?",
lbs = input()

print "So, %f lbs equal %f kg." % (lbs, lbs * 0.4532)