#Calculator de numere
from colorama import init
from colorama import Fore, Back, Style
init(True)
what = input ("Alege (+,-,*,/): ")
a = float( input("First number: "))
b = float( input("Second number: "))
if what == "+":
	c = a + b
	print("Rezultat: " + str(c) )
elif what == "-":
	c = a - b
	print("Rezultat: " + str(c) )
elif what == "*":
	c = a * b
	print("Rezultat: " + str(c) )
elif what == "/":
	c = a / b
	print("Rezultat: " + str(c) )
else: print("Error")
input("Finish!")