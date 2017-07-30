# -*- coding:utf-8 -*-
# 车 = 100
cars = 100
# 每辆车的空座数 = 4.0（浮点数）
space_in_a_car = 4.0
# 司机 = 30
drivers = 30
# 乘客 = 90
passengers = 90
# 空车（无驾驶员） = 车 - 司机
cars_not_driven = cars - drivers
# 可行驶车辆数 = 司机数量
cars_driven = drivers
# 车辆可载人数 = 可行驶车辆数 * 每辆车的空座数
carpool_capacity = cars_driven * space_in_a_car
# 平均每车乘客数 = 乘客 / 可行驶车辆数
average_passengers_per_car = passengers / cars_driven

# 输出所需变量。
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Traceback (most recent call last):
#	File "ex4.py", line 8, in <module>
#		average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined
#文件ex4.py中的第8行，‘car_pool_capacity'没有被定义