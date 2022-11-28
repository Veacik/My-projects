import mouse
from mouse import is_pressed, double_click

from time import sleep

import keyboard 
from keyboard import press_and_release, add_hotkey, wait




while True:
	if is_pressed(button = "left"):	
		while True:
			sleep(0.01)
			double_click(button = "left")
			sleep(60.0)




print("Thanks You!")