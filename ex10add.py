# -*- coding:utf-8 -*-
print "I am 6'2\" tall." # 将字符串中的双引号转义
print 'I am 6\'2" tall.' # 将字符串中的单引号转义
print "转义序列\"escape sequences\"\n" # 将字符串中的双引号转义
print ''' I don't want to give up.''' #不知道例子里为什么这里会有空行0.0

tabby_cat = "\vI'm tabbed in."
persian_cat = "I'm split\ron a line."
backslash_cat = "I'm \\ a \\ cat."
how_much_cat = 56

fat_cat = '''
I\'ll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print 'Today I made a misstake. I\'ll not repetition it again.'

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat,
print "\v"
print "\r %f" % how_much_cat
print "\t %x" % how_much_cat # 十六进制
print "\t %o" % how_much_cat # 八进制



pa = "I\'ll show you all I typed \""
pb = "And this is anothers\' \""
print "\r %s \ I want show you something special" % how_much_cat
print "It write: %r ." % pa
print "It write: %s ." % pb
