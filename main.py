import os
import datetime
from csvGeneratorPerf import csvGeneratorPerf

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
	print("6 - Create CSV")
	print("7 - Plot graphs")
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
valgrind = 'valgrind --tool=cachegrind --I1=Ix,Iy,Iz --D1=Dx,Dy,Dz --LL=Lx,Ly,Lz '
valgrindSave = 'valgrind --log-file="TOSAVE" --tool=cachegrind --I1=Ix,Iy,Iz --D1=Dx,Dy,Dz --LL=Lx,Ly,Lz '

alg = {0 : "./bubble_sort_demo ",
	   1 : "./radix_sort_demo ",
	   2 : "./quick_sort_demo ",
	   3 : "./prime_demo ",
	   4 : "./prime_custom_demo "}

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

generate = csvGeneratorPerf()

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

			
			Iy = input("[LEVEL1 INSTRUCTION CACHE] Associativity: ")
			Iz = input("[LEVEL1 INSTRUCTION CACHE] Line Size: ")
			Ix = input("[LEVEL1 INSTRUCTION CACHE] Size: ")

			Dy = input("[LEVEL1 DATA CACHE] Associativity: ")
			Dz = input("[LEVEL1 DATA CACHE] Line Size: ")
			Dx = input("[LEVEL1 INSTRUCTION CACHE] Size: ")

			Ly = input("[LAST LEVEL CACHE] Associativity: ")
			Lz = input("[LAST LEVEL CACHE] Line Size: ")
			Lx = input("[LEVEL1 INSTRUCTION CACHE] Size: ")

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
					os.system(perfSave.replace("FILENAME", "logsPerf/" + selAlg[2:][:-1] + "#" +str(row) + "#" + str(datetime.datetime.now()).replace(" ","_") + ".txt") + selAlg + str(row))

		reshow()

	elif selection == 5:
		
		# showAlg()
		# selAlg = int(input("Select one: "))

		# while((selAlg<0 or selAlg>(len(alg)-1)) and selAlg != 9):
		# 		selAlg = int(input("Error. Type a valid number: "))

		# if selAlg == 9: # Going back to main menu
		# 	pass
		# else:
		
		# 	selAlg = alg[selAlg]
		associativity = 2
		lineSize = 16
		size = 64

		while associativity<=64:
			while lineSize<=128:
				while size<=16384:

					print(str(associativity) + ' ' + str(lineSize) + ' ' + str(size))

					size *= 2
				size = 64
				lineSize *= 2
			lineSize = 16
			associativity *= 2



	elif selection == 6:
		print("Creating csv...")
		generate.generate()
		print("CSV created :3")
		reshow()

	elif selection == 7:
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
				csv = pd.read_csv("logsPerf.csv")
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