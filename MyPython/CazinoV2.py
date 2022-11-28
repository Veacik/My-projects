#Random Generator
import random

from random import *

import pylint

point = float(input("Твой баланс?: "))

done = "y"

while done == "y":
	cost = float(input("Для игры ведите 100оч.: "))	
	if cost > point:
		print("Для игры Требуется 100оч.")
		continue
	elif cost != 100:
		print("Для игры Требуется 100оч.")
		continue
	else: 
		cost == 100
		point = point - 100
		game = randint(0, 10)	
		if game == 1:
			point = point + 20
		elif game == 2:
			point = point + 40
		elif game == 3:
			point = point + 60
		elif game == 4:
			point = point + 80
		elif game == 5:
			point = point + 100
		elif game == 6:
			point = point + 120
		elif game == 7:
			point = point + 140
		elif game == 8:
			point = point + 160
		elif game == 9:
			point = point + 180
		elif game == 10:
			point = point + 200
		print(game)
		print("Твой Баланс: " + str(point))

		done = input("Продолжоть?(y / n): ")

print("Ты выйграл:", point, "очьков")