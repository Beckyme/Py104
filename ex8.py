# -*- coding: utf-8 -*-
# 给formatter赋值格式化字符串。
formatter = "%r %r %r %r"

# 输出变量formatter，格式化字符串输出的具体内容随%后的赋值而改变。
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could tpye up right.",
	"But it didn't sing.",
	"So I said goodnight."
)