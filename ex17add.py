# -*- coding:utf-8 -*-

# copy 1.txt 2.txt    ��1.txt�е��ı�������2.txt
# type 1.txt �ɽ�1.txt�е����ݴ�ӡ����Ļ��

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

# �����������ʹ��

from sys import argv; open(argv[2],'w').write(open(argv[1]).read())