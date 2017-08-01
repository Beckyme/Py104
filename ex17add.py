# -*- coding:utf-8 -*-

# copy 1.txt 2.txt    则将1.txt中的文本拷贝至2.txt
# type 1.txt 可将1.txt中的内容打印至屏幕上

'''
from sys import argv
from os.path import exists

script, from_file, to_file =argv

print "Copying from %s to %s" % (from_file, to_file)

input = open(from_file).read()
output = open(to_file, 'w')
output.write(input)

print "Alright, all done."
'''

# 上述代码可以使用

from sys import argv; open(argv[2],'w').write(open(argv[1]).read())