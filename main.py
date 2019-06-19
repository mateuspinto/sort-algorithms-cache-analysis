import os
import datetime
from csvGenerator import csvGenerator

def showMenu():
	print()
	print("--------------------------------------------------------")
	print("Welcome to Cache tests!")
	print("--------------------------------------------------------")
	print()
	print("1 - Compile C++ binaries")
	print("2 - Run algorithm analysis with Perf")
	print("3 - Run cache simulations with Valgrind")
	print("4 - Run empirical tests")
	print("5 - Create CSV")
	print("6 - Plot graphs")
	print("8 - Delete binaries")
	print("9 - Quit")
	print()
	print("--------------------------------------------------------")
	print()

def reshow():
	print("Type 0 to display the menu again: ")

def showAlg():
	print()
	print("--------------------------------------------------------")
	print("Algorithms that has been implemented")
	print("--------------------------------------------------------")
	print()
	print("0 - Run bubble sort")
	print("1 - Run radix sort")
	print("2 - Run quick sort")
	print("3 - Run primes algorithm (without optimization)")
	print("4 - Run primes algorithm (with optimization)")
	print("9 - Go back to main menu")
	print()
	print("--------------------------------------------------------")

def showMetrics():
	print()
	print("--------------------------------------------------------")
	print("Which metrics do you want to see?")
	print("--------------------------------------------------------")
	print()
	print("0 - cacheReferences")
	print("1 - cacheReferencesRelat")
	print("2 - cacheMisses")
	print("3 - cacheMissesRelat")
	print("4 - taskClock")
	print("5 - taskClockRelat")
	print("6 - cycles")
	print("7 - cyclesRelat")
	print("8 - instructions")
	print("9 - instructionsRelat")
	print("10 - elapsedSeconds")
	print()
	print("--------------------------------------------------------")


keep = 1
perf = "perf stat -e cache-references,cache-misses,task-clock,cycles,instructions -a "
perfSave = "perf stat -o FILENAME -e cache-references,cache-misses,task-clock,cycles,instructions -a "
valgrind = "valgrind --tool=cachegrind --I1=Ix,Iy,Iz --D1=Dx,Dy,Dz --LL=Lx,Ly,Lz "

alg = {0 : "./bubble_sort_demo ",
	   1 : "./radix_sort_demo ",
	   2 : "./quick_sort_demo ",
	   3 : "./prime_demo ",
	   4 : "./prime_demo "}

metrics = {0 : 'cacheReferences',
		   1 : 'cacheReferencesRelat',
		   2 : 'cacheMisses',
		   3 : 'cacheMissesRelat',
		   4 : 'taskClock',
		   5 : 'taskClockRelat',
		   6 : 'cycles',
		   7 : 'cyclesRelat',
		   8 : 'instructions',
		   9 : 'instructionsRelat',
		   10: 'elapsedSeconds'}

generate = csvGenerator()

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

	# Run Perf
	elif selection == 2:

		showAlg()
		selAlg = int(input("Select one: "))

		while((selAlg<0 or selAlg>(len(alg)-1)) and selAlg != 9):
				selAlg = int(input("Error. Type a valid number: "))

		if selAlg == 9: # Going back to main menu
			pass
		else:

			selAlg = alg[selAlg]

			samples = int(input("How much entries do you want? "))

			while(samples<=0):
				samples = int(input("Error. Type a valid number: "))

			os.system(perf + selAlg + str(samples))
		
		reshow()

	# Run Valgrind
	elif selection == 3:

		showAlg()
		selAlg = int(input("Select one: "))

		while((selAlg<0 or selAlg>(len(alg)-1)) and selAlg != 9):
				selAlg = int(input("Error. Type a valid number: "))

		if selAlg == 9: # Going back to main menu
			pass
		else:
		
			selAlg = alg[selAlg]

			
			Iy = int(input("[LEVEL1 INSTRUCTION CACHE] How much words per block? "))
			Iz = int(input("[LEVEL1 INSTRUCTION CACHE] How much blocks? "))

			Dy = int(input("[LEVEL1 DATA CACHE] How much words per block? "))
			Dz = int(input("[LEVEL1 DATA CACHE] How much blocks? "))

			Ly = int(input("[LAST LEVEL CACHE] How much words per block? "))
			Lz = int(input("[LAST LEVEL CACHE] How much blocks? "))

			Ix = str(Iy * Iz)
			Dx = str(Dy * Dz)
			Lx = str(Ly * Lz)

			Iy = str(Iy)
			Iz = str(Iz)
			
			Dy = str(Dy)
			Dz = str(Dz)

			Ly = str(Ly)
			Lz = str(Lz)

			samples = int(input("How much entries do you want? "))

			while(samples<=0):
				samples = int(input("Error. Type a valid number: "))

			os.system(valgrind.replace("Ix", Ix).replace("Iy", Iy).replace("Iz", Iz).replace("Dx", Dx).replace("Dy", Dy).replace("Dz", Dz).replace("Lx", Lx).replace("Ly", Ly).replace("Lz", Lz) + selAlg + str(samples))

		reshow()

	# Run empirical tests with Perf
	elif selection == 4:

		showAlg()
		selAlg = int(input("Select one: "))

		while((selAlg<0 or selAlg>(len(alg)-1)) and selAlg != 9):
				selAlg = int(input("Error. Type a valid number: "))

		if selAlg == 9: # Going back to main menu
			pass
		else:

			selAlg = alg[selAlg]

			order = int(input("Select order: "))

			for zeros in range(order+1):
				for i in range(0,10):
					row = i*(10**zeros)
					os.system(perfSave.replace("FILENAME", "logs/" + selAlg[2:][:-1] + "#" +str(row) + "#" + str(datetime.datetime.now()).replace(" ","_") + ".txt") + selAlg + str(row))

		reshow()

	elif selection == 5:
		print("Creating csv...")
		generate.generate()
		print("CSV created :3")
		reshow()

	elif selection == 6:
		import pandas as pd
		import matplotlib.pyplot as plt

		showAlg()
		selAlg = int(input("Select one: "))

		while((selAlg<0 or selAlg>(len(alg)-1)) and selAlg != 9):
				selAlg = int(input("Error. Type a valid number: "))

		if selAlg == 9: # Going back to main menu
			pass
		else:

			stringAlg = alg[selAlg]

			showMetrics()
			metric = int(input("Select one: "))

			while((metric<0 or metric>(len(metrics)-1)) and metric != 99):
				metric = int(input("Error. Type a valid number: "))

			if metric == 99:
				pass
			else:

				metric = metrics[metric]
				csv = pd.read_csv("logs.csv")
				algCsv = csv[csv.algorithm == stringAlg[2:][:-1]].sort_values(by='entries').reset_index()
				plt.plot(algCsv.entries, algCsv[metric])
				plt.title(stringAlg[2:][:-1])
				plt.xlabel('entries')
				plt.ylabel(metric)
				plt.show()

		reshow()

	# Clear binaries
	elif selection == 8:
		os.system("make clean")
		reshow()

	# Quit
	elif selection == 9:
		print("Thank ya")
		keep = 0