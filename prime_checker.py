"""
File: prime_checker.py
Name:洪筠筑
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	This program is used to identify the prime number.
	"""
	print("Welcome to the prime checker!")
	n=int(input("n= "))
	while n != EXIT:
		x = n
		while x != 1:
			x -= 1
			if n%x == 0:
				if x != 1:
					print("n is not a prime number.")
					break
				else:
					print("n is a prime number.")
		n = int(input("n= "))
	print("Have a good one!")


		# if x == 1:
		# 	print("n is a prime number.")
		# 	n = int(input("n= "))


# while x != 1:
# 	x-=1
# 	n%x != 0



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
