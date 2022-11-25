"""
File: quadratic_solver.py
Name:洪筠筑
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
	This code is used to solve the problem of linear equations in two unknowns.
	"""
	print("stanCode Quadratic Solver!")
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	if b*b-4*a*c < 0:
		print("No real roots")
	elif b*b-4*a*c == 0:
		root=(-b)/2*a
		print("One root:("+str(root)+",0)")
	else:
		y = math.sqrt(b*b-4*a*c)
		root1=(-b+y)/2*a
		root2=(-b-y)/2*a
		print("Two roots:("+str(root1)+","+str(root2)+")")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()