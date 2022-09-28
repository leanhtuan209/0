from os import system
from time import sleep
from random import randint
from random import choice
import colorama

class Color:
        colorama.init(autoreset=True)
        All = [colorama.Fore.RESET, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX]


def Rocket():
	with open("utils/animation/rocket.txt", 'r') as file:
		read = "".join(file.read())
	for x in range(50, 0, -1):
		print(f"{choice(Color.All)}\n" * x + read)
		system('clear')
		s = ""
		read += "\n\t\t"
