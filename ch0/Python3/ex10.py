# -- coding:utf-8 --
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

while True:
	for i in ["/","-","|","\\","|"]:
		print("%s\r" % i),
	break
'''
break终止循环执行循环体下面的代码
return终止循环并且退出循环所在的方法
continue终止当前循环,进行下一次循环
'''