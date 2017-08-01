# -*- coding:utf-8 -*-
def people_in_boat(a, b, c, d):
	print "Now we are in Beagle."
	print "This in not the trip which we could saw Darwin."
	print "We can see 4 people in the boat:"
	print "%s, %s, %s and %s." % (a, b, c, d)

print "This is the first method to run this function:"
people_in_boat(11951, 11952, 11953, 11954)
print "Have this kind of \"name\" maybe too strange."


print ""
print "This is the second method to run this function:"
a = "John"
b = "Jimmy"
c = "Xiaoming"
d = "Yono"
people_in_boat(a, b, c, d)


print ""
print "This is the third method to run this function:"
print "You can give them name as you like."
name_a = raw_input("You want to call 11951 as?")
name_b = raw_input("You want to call 11952 as?")
name_c = raw_input("You want to call 11953 as?")
name_d = raw_input("You want to call 11954 as?")
people_in_boat(name_a, name_b, name_c, name_d)


print ""
print "This is the forth method to run this function:"
print "You should give them a number."
number_a = int(raw_input("What number will you give to John?"))
number_b = int(raw_input("What number will you give to Jimmy?"))
number_c = int(raw_input("What number will you give to Xiaoming?"))
number_d = int(raw_input("What number will you give to Yono?"))
people_in_boat(number_a, number_b, number_c, number_d)


print""
print "This is the fifth method to run this function:"
new_a = "You give 11951 a name %s, a new number %d.\n" % (name_a, number_a)
new_b = "You give 11952 a name %s, a new number %d.\n" % (name_b, number_b)
new_c = "You give 11953 a name %s, a new number %d.\n" % (name_c, number_c)
new_d = "You give 11954 a name %s, a new number %d.\n" % (name_d, number_d)
people_in_boat(new_a, new_b, new_c, new_d)


print""
print "This is the sixth method to run this function:"
print "And I want to use the name you give it to these people to run forth again."
print "You should give them a number."
new_number_a = int(raw_input("What number will you give to %s?" % (name_a)))
new_number_b = int(raw_input("What number will you give to %s?" % (name_b)))
new_number_c = int(raw_input("What number will you give to %s?" % (name_c)))
new_number_d = int(raw_input("What number will you give to %s?" % (name_d)))
people_in_boat(new_number_a, new_number_b, new_number_c, new_number_d)

print""
print "This is the seventh method to run this function:"
print "I change them number to float type."
f_number_a = float(new_number_a)
f_number_b = float(new_number_b)
f_number_c = float(new_number_c)
f_number_d = float(new_number_d)
people_in_boat(f_number_a, f_number_b, f_number_c, f_number_d)

print""
print "This is the eighth method to run this function:"
print "Now I change them number to binary."
b_number_a = bin(new_number_a)
b_number_b = bin(new_number_b)
b_number_c = bin(new_number_c)
b_number_d = bin(new_number_d)
people_in_boat(b_number_a, b_number_b, b_number_c, b_number_d)

print""
print "This is the ninth method to run this function:"
print "Now I change them number to hexadecimal." 
# 十六进制
h_number_a = hex(new_number_a)
h_number_b = hex(new_number_b)
h_number_c = hex(new_number_c)
h_number_d = hex(new_number_d)
people_in_boat(h_number_a, h_number_b, h_number_c, h_number_d)

print""
print "This is the tenth method to run this function:"
print "Now I change them number to Octal."
# 八进制
o_number_a = oct(new_number_a)
o_number_b = oct(new_number_b)
o_number_c = oct(new_number_c)
o_number_d = oct(new_number_d)
people_in_boat(o_number_a, o_number_b, o_number_c, o_number_d)