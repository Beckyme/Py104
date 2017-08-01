# -*- coding:utf-8 -*-
filename = raw_input("What file you want to open?")
txt = open(filename)

print txt.read()
txt.close()

# 比起用argv，我更喜欢raw_input，互动性强~