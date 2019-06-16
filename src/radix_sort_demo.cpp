#include <stdio.h>
#include <stdint.h>
#include <time.h>

#include <errno.h>   // for errno
#include <limits.h>  // for INT_MAX


#include "generic.h"
#include "radix_sort.h"

int main(int argc, char const *argv[])
{
	using namespace alg;
	
	char *p;

	uint32_t * list = NULL;

	errno = 0;
	long MAX_ELEMENTS = strtol(argv[1], &p, 10);

	// Check for errors: e.g., the string does not represent an integer
	// or the integer is larger than int
	if (errno != 0 || *p != '\0' || MAX_ELEMENTS > INT_MAX) {
		// Put here the handling of the error, like exiting the program with
		// an error message
	} else {
		// No error 
	}

	list = (uint32_t *) malloc(MAX_ELEMENTS * sizeof(uint32_t));

	int i = 0;
	srand(time(NULL));
	// generate random numbers and fill them to the list
	for(i = 0; i < MAX_ELEMENTS; i++ ){
		list[i] = rand()%(MAX_ELEMENTS*10);
	}

	printf("The list before sorting is:\n");
	printlist(list,MAX_ELEMENTS);

	// sort the list using insertion sort
	radix_sort(list, MAX_ELEMENTS);  
	check_order(list, MAX_ELEMENTS);

	// print the result
	printf("The list after sorting using radix sort algorithm:\n");
	printlist(list,MAX_ELEMENTS);

	return 0;
}
