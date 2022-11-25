"""
File: coin_flip_runs.py
Name:洪筠筑
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
	"""
	This program is used to calculate the number of the continuous H or T
	"""
	print('Let\'s flip the coin!')
	number_of_runs = int(input('Number of runs:'))
	run = 0
	ans = ''
	a_roll = random.randrange(0, 2)
	if a_roll == 0:
		# 0 is head
		ans += 'H'
	else:
		# 1 is tail
		ans += 'L'
	is_in_a_row = False
	while True:
		if run == number_of_runs:
			print(ans)
			break
		b_roll = random.randrange(0, 2)
		if a_roll == b_roll:
			if not is_in_a_row:
				run += 1
				is_in_a_row = True
		else:
			is_in_a_row = False
		if b_roll == 0:
			# 0 is head
			ans += 'H'
		else:
			# 1 is tail
			ans += 'L'
		a_roll = b_roll


# def random_toll():


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
