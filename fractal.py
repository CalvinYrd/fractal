from os import name as os_name
from os import system as os_system

from colorama import Fore as colorama_Fore
from colorama import Back as colorama_Back
from threading import Thread as threading_Thread

class ComplexNumber:
	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary

	def get(self):
		return [self.real, self.imaginary]

	def getString(self):
		if (type(self) == str):
			res = self
		else:
			res = self.get()

			if (str(res[1]).startswith("-")):
				end = str(res[1]).replace('-', '- ', 1)
			else:
				end = f"+ {res[1]}"

			res = f"{res[0]} {end}i"

		return res

	def add(self, num):
		if (type(num) == int):
			numReal = numImaginary = num
		else:
			numReal = num.real
			numImaginary = num.imaginary

		newReal = self.real + numReal
		newImaginary = self.imaginary + numImaginary

		return ComplexNumber(newReal, newImaginary)

	def substract(self, num):
		if (type(num) == int):
			numReal = num
		else:
			numReal = num.real

		newReal = self.real - numReal

		return ComplexNumber(newReal, self.imaginary)

	def multiply(self, num):
		newReal = [
			self.real * num.real,
			self.imaginary * num.imaginary
		]
		newImaginary = [
			self.real * num.imaginary,
			num.real * self.imaginary
		]

		newReal = newReal[0] - newReal[1]
		newImaginary = newImaginary[0] + newImaginary[1]

		return ComplexNumber(newReal, newImaginary)

	def power(self, size):
		res = self

		for i in range(size - 1):
			res = res.multiply(res)

		return ComplexNumber(res.real, res.imaginary)

def floatRange(x, y, step):
	numbers = [x]

	while numbers[-1] < y:
		numbers.append(round(numbers[-1] + step, 2))

	return numbers

def groupList(l):
	newL = []

	for el in l:
		if (el not in newL):
			newL.append(el)
	
	return newL

def diverges(num, power, substract):
	elements = []
	result = False

	r = 100
	for i in range(r):
		num = num.power(power).substract(substract)
		elements.append(num.get())

	if (len(groupList(elements)) > r - 1):
		result = True

	return result

def point(color = None):
	if (color == "def"):
		color = colorama_Fore.WHITE
	else:
		color = colorama_Fore.BLACK

	return f"{color}■{colorama_Fore.RESET}"

def drawLine(height, width, step, power, substract):
	res = ""
	for i in floatRange(-width, width+1, step):
		if (diverges(ComplexNumber(i, height), power, substract)):
			col = "def"
		else:
			col = None

		res += point(col)
	return res

def drawFractal(resolution = 19, power = 2, substract = 1):
	try:
		print(colorama_Back.WHITE)
		r = (0.7 / (resolution * 1.2)) * resolution
		step = 0.09505 / resolution

		for i in floatRange(-r, r, step):
			print(drawLine(-i * 2, r*3, step, power, substract))
		
		raise KeyboardInterrupt
	
	except (KeyboardInterrupt):
		print(colorama_Back.RESET)

if (os_name == "nt"):
	clear = lambda: os_system("cls")
else:
	clear = lambda: os_system("clear")

clear()
drawFractal(power = 2)
