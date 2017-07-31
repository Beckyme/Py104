# -*- coding:utf-8 -*-
from sys import argv

script, fav, user_name = argv
prompt = '* '

print """
This is %s, I'm so glad to see you, %s.
I know that you like %s.
I wish you answer these questions.
""" % (script, user_name, fav)

print "Why do you like %s, %s?" % (fav, user_name)
reason = raw_input(prompt)

print "How deep you like %s, %s?" %(fav, user_name)
deep = raw_input(prompt)

print "How long you like %s, %s?" %(fav, user_name)
long = raw_input(prompt)

print """
So, you like %s because of %s.
And you %s like %s.
You spend %s do this work, and I wish you will keep going.
""" % (fav, reason, deep, fav, long)