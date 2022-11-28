import random
from random import *

bank = float(input("How are you money?:"))
winnings = 0

done = "y"

while done == "y":
	bet = float(input("bet amount: "))
	if bet > bank:
		print("Bet amount is more than you have. Try again!")
		continue
	else:
		choice = float(input("0 or 1?:"))
		result=randint(0,2)
		if choice == result:
			bank += bet
			winnings += bet
			print("You Won!")
		else:
			bank -= bet
			print("You Lost!")

	print("Bank:",bank)
	print()

	done = input("Play again? (y or n)")

print("You've made", winnings, "dollars")
print("You have this much in your bank:", bank)