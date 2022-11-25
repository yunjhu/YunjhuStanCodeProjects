"""
File: weather_master.py
Name:洪筠筑
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100


def main():
	"""
	This program illustrates the highest temperature, the lowest temperature, average temperature, and how many cold days.
	"""
	print('stanCode\"Weather Master 4.0\"')
	temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to exit)?'))
	if temp == EXIT:
		print('No temperatures are entered.')
	else:
		maximum = temp
		minimum = temp
		total = temp
		how_many_days = 1
		cold_day = 0
		if temp < 16:
			cold_day += 1
		while True:
			temp = int(input('Next Temperature: (or -100 to exit)?'))
			if temp == EXIT:
				break
			total += temp
			if temp < 16:
				cold_day += 1
			if temp > maximum:
				maximum = temp
			if temp < minimum:
				minimum = temp
			how_many_days += 1
		print("Highest temperature = " + str(maximum))
		print("Lowest temperature = " + str(minimum))
		print("Average = " + str(total/how_many_days))
		print(str(cold_day) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
