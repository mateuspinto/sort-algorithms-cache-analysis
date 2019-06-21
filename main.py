import os
import datetime
from csvGeneratorPerf import csvGeneratorPerf
from csvGeneratorValgrind import csvGeneratorValgrind

def showMenu():
	print()
	print("--------------------------------------------------------")
	print("Welcome to Cache tests!")
	print("--------------------------------------------------------")
	print()
	print("1 - Compile C++ binaries and create folders")
	print("2 - Run algorithm analysis with Perf")
	print("3 - Run cache simulations with Valgrind")
	print("4 - Run empirical tests with Perf")
	print("6 - Create CSV for graph plots")
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
	print("5 - All prime algorithm (only for graph plots)")
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

# Terminal commands
perf = "perf stat -e cache-references,cache-misses,task-clock,cycles,instructions -a "
perfSave = "perf stat -o FILENAME -e cache-references,cache-misses,task-clock,cycles,instructions -a "
valgrind = 'valgrind --log-file="FILENAME" --tool=cachegrind --D1=Dx,Dy,Dz '

# Algorithms
alg = {0 : "./bubble_sort_demo ",
	   1 : "./radix_sort_demo ",
	   2 : "./quick_sort_demo ",
	   3 : "./prime_demo ",
	   4 : "./prime_custom_demo "}

# Perf metrics
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

showMenu()

while keep:
	selection = int(input())

	# Show menu
	if selection == 0:
		showMenu()
	
	# Compile C++ files
	elif selection == 1:
		os.system("make")
		os.system("mkdir logsPerf")
		os.system("mkdir graphsPerf")
		os.system("mkdir logsValgrind")
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
			
			Dx = input("[LEVEL1 INSTRUCTION CACHE] Size: ")
			Dz = input("[LEVEL1 DATA CACHE] Line Size: ")
			Dy = input("[LEVEL1 DATA CACHE] Associativity: ")

			samples = int(input("How much entries do you want? "))

			while(samples<=0):
				samples = int(input("Error. Type a valid number: "))

			filename = "logsValgrind/" + selAlg[2:][:-1] + "#" + str(samples) + 'x' + str(Dx) + 'x' + str(Dy) + 'x' + str(Dz) + 'x' + ".txt"
			os.system(valgrind.replace("FILENAME", filename).replace("Dx", Dx).replace("Dy", Dy).replace("Dz", Dz) + selAlg + str(samples))
			fileOpen = open(filename, "r")
			print(fileOpen.read())
			fileOpen.close()

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

	elif selection == 6:
		print("Creating csv...")
		generate = csvGeneratorPerf()
		generate1 = csvGeneratorValgrind()
		
		generate.generate()
		generate1.generate()
		print("CSV created :3")
		reshow()

	elif selection == 7:
		import pandas as pd
		import matplotlib.pyplot as plt
		import matplotlib.patches as mpatches

		showAlg()
		selAlg = int(input("Select one: "))

		while((selAlg<0 or selAlg>(len(alg)-1)) and selAlg != 9 and selAlg != 5):
				selAlg = int(input("Error. Type a valid number: "))

		if selAlg == 9: # Going back to main menu
			pass

		if selAlg == 5: # Comparation between prime algorithms

			showMetrics()
			metric = int(input("Select one: "))

			while((metric<0 or metric>(len(metrics)-1)) and metric != 99):
				metric = int(input("Error. Type a valid number: "))

			if metric == 99:
				pass
			else:
				metric = metrics[metric]
				csv = pd.read_csv("logsPerf.csv")
				primesWithoutOptimization =  csv[csv.algorithm == 'prime_demo'].sort_values(by='entries').reset_index()
				primesWithOptimization = csv[csv.algorithm == 'prime_custom_demo'].sort_values(by='entries').reset_index()
				plt.plot(primesWithoutOptimization.entries, primesWithoutOptimization[metric], color='red')
				plt.plot(primesWithOptimization.entries, primesWithOptimization[metric], color='blue')
				red_patch = mpatches.Patch(color='red', label='Conventional prime numbers algorithm')
				blue_patch = mpatches.Patch(color='blue', label='Optimized single thread prime algorithm')
				plt.legend(handles=[red_patch, blue_patch])
				plt.xlabel('entries')
				plt.ylabel(metric)
				plt.title("Comparation between prime algorithms in " + metric)
				plt.xscale('linear')
				plt.savefig('graphsPerf/primes_' + metric + '.png')
				plt.show()
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
				plt.title(metric + ' in '+ stringAlg[2:][:-1])
				plt.xlabel('entries')
				plt.ylabel(metric)
				plt.xscale('linear')
				plt.savefig('graphsPerf/' + stringAlg[2:][:-1] + '_' + metric + '.png')
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