# -*- coding:utf-8 -*-

#1.raw_input()能够接收用户输入的字符串，Python3.x开始使用input()替代该函数。



#2.
# 1输入字符串 13222319810101****
nID = ''
while 1:
	nID = raw_input("Input your id plz")
	if len(nID) != len("13222319810101****"):
	  print 'wring lenth of id, input again'
	else:
	  break

print 'your id is %s' % (nID)


# 2输入整数
nAge = int(raw_input("input your age plz:\n"))
if nAge > 0 and nAge < 120:
  print 'thanks!'
else:
  print 'bad age'
print 'your age is %d\n' % nAge


# 3输入浮点型
fWeight = 0.0
fWeight = float(raw_input("input your weight\n"))
print 'your weight is %f' % fWeight


# 4输入16进制数据
nHex = int(raw_input('input hex value(like 0x20):\n'),16)
print 'nHex = %x,nOct = %d\n' %(nHex,nHex)


# 5输入8进制数据
nOct = int(raw_input('input oct value(like 020):\n'),8)
print 'nOct = %o,nDec = %d\n' % (nOct,nOct)

#3.
print "What kind of sugar would you like?"
suger = raw_input()
print "What kind of book would you read?"
book = raw_input()

print "Now I know you like %r and %r, but I still not really knowing you..." % (suger, book)

#4.一开始确实没有注意。。。



