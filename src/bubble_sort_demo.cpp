#include <stdio.h>
#include <stdlib.h> 
#include <time.h>

#include <errno.h>   // for errno
#include <limits.h>  // for INT_MAX

#include "generic.h"
#include "bubble_sort.h"

using namespace alg;
int main (int argc, char const *argv[]) {

	char *p;

	int * list = NULL;

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

	list = (int*) malloc(MAX_ELEMENTS * sizeof(int));

	for(int i = 0; i < MAX_ELEMENTS; i++ ){
		list[i] = rand()%(MAX_ELEMENTS*10);
	}

	//printf("The list before sorting is:\n");
	//printlist(list,MAX_ELEMENTS);

	alg::BubbleSort(list,0,MAX_ELEMENTS-1);

	//printf("The list after sorting using bubble-sort algorithm:\n");
	//printlist(list,MAX_ELEMENTS);
	
	return 0;
}
