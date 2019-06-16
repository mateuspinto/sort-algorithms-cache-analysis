import os

def showMenu():
	print()
	print("--------------------------------------------------------")
	print("Welcome to Cache tests!")
	print("--------------------------------------------------------")
	print()
	print("1 - Compile C++ binaries")
	print("2 - Run bubble sort")
	print("3 - Run radix sort")
	print("4 - Run quick sort")
	print("5 - Run primes algorithm (without optimization)")
	print("6 - Run primes algorithm (with optimization)")
	print("8 - Delete binaries")
	print("9 - Quit")
	print()
	print("--------------------------------------------------------")
	print()

def reshow():
	print("Type 0 to display the menu again: ")

keep = 1
perf = "perf stat -e cache-references,cache-misses,task-clock,cycles,instructions -a "

showMenu()

while keep:
	selection = int(input())

	# Show menu
	if selection == 0:
		showMenu()
	
	# Compile C++ files
	elif selection == 1:
		os.system("make")
		reshow()

	# BUBBLE SORT
	elif selection == 2:
		samples = int(input("How much entries do you want? "))

		while(samples<=0):
			samples = int(input("Error. Type a valid number: "))

		os.system(perf + "./bubble_sort_demo " + str(samples))
		reshow()
		
	# RADIX SORT
	elif selection == 3:
		samples = int(input("How much entries do you want? "))

		while(samples<=0):
			samples = int(input("Error. Type a valid number: "))

		os.system(perf + "./radix_sort_demo " + str(samples))
		reshow()

	# QUICK SORT
	elif selection == 4:
		samples = int(input("How much entries do you want? "))

		while(samples<=0):
			samples = int(input("Error. Type a valid number: "))

		os.system(perf + "./quick_sort_demo " + str(samples))
		reshow()

	# PRIME WITHOUT OPTIMIZATION
	elif selection == 5:
		samples = int(input("How much entries do you want? "))

		while(samples<=0):
			samples = int(input("Error. Type a valid number: "))

		os.system(perf + "./prime_demo " + str(samples))
		reshow()

	# Clear binaries
	elif selection == 8:
		os.system("make clean")
		reshow()

	# Quit
	elif selection == 9:
		print("Thank ya")
		keep = 0