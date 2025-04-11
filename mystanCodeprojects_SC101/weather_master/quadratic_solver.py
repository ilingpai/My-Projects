"""
File: quadratic_solver.py
Name:Sandy
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	find the roots
	"""
	print("StanCode Quadratic Solver!")
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	delta = b*b-4*a*c
	if delta >= 0:
		l1 = math.sqrt(delta)
		x1 = ((-b) + l1) / 2 * a
		x2 = ((-b) - l1) / 2 * a
		if delta > 0:
			print("Two roots: " + str(x1) + "," + str(x2))
		elif delta == 0:
			print("One root: " + str(x1))
	else:
		print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
