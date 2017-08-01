# -*- coding:utf-8 -*-
cities = {'CA':'San Francisco', "MI":"Detroit", 'FL':'Jacksonville'}

cities['NY'] = "New York"
cities["OR"] = "Portland"

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."
		
# ok pay attention!
cities['_find'] = find_city

for i in cities:
        
        if True:
                print("State? (ENTER to quit)"),
                state = raw_input('> ')
	
        elif not state:break

	city_found = cities['_find'](cities, state)
	print city_found