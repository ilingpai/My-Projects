"""
File: weather_master.py
Name:Sandy
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This number controls when to stop the game
EXIT = -100


def main():
	"""
	1.find the maximum temperature.
	2.find the minimum temperature.
	3.find the average temperature.
	4.How many days are lower than 16 degree?
	"""
	print('StanCode "Weather Master 4.0"')
	data = int(input('Next Temperature: (or -100 to quit)? '))
	cold = 16 > data  # lower than 16 degrees
	n = 1  # count the numbers of the temperature
	total = data  # sum input data
	average = total / n  # find the avg degree.
	if data == EXIT:
		print("No temperatures were entered.")
	else:
		maximum = data
		minimum = data
		if data >= 16:
			cold = 0
		else:
			cold = 1
		while True:
			data = int(input('Next Temperature: (or -100 to quit)? '))
			if data == EXIT:
				break
			if data < 16:  # total days of temperature lower than 16 degree
				cold += 1
			if data != EXIT:
				n += 1
				total += data
				average = total/n
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
		print('Highest Temperature: ' + str(maximum))
		print('Lowest Temperature: ' + str(minimum))
		print('Average Temperature: ' + str(average))
		print(str(cold) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
