"""
File: largest_digit.py
Name: Ashley
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, largest):
	if n < 0:
		n = n * (-1)
	if n % 10 == 0:
		return largest
	else:
		dig = n % 10
		if dig > largest:
			largest = dig
		return find_largest_digit_helper(n//10, largest)


if __name__ == '__main__':
	main()
