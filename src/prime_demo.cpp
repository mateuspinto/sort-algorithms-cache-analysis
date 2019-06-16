#include <stdio.h>
#include <prime.h>
#include <time.h>

#include <errno.h>   // for errno
#include <limits.h>  // for INT_MAX

using namespace alg;
int main(int argc, char const *argv[])
{

	char *p;

	errno = 0;
	long num = strtol(argv[1], &p, 10);

	// Check for errors: e.g., the string does not represent an integer
	// or the integer is larger than int
	if (errno != 0 || *p != '\0' || num > INT_MAX) {
		// Put here the handling of the error, like exiting the program with
		// an error message
	} else {
		// No error 
	}


	unsigned i;
	time_t t1 = time(NULL);

	time_t t2 = time(NULL);

	int count = 0;
	t1 = time(NULL);
	for (i = 0; i<num+1; i++) {
		if (test_prime(i)) count++;
	}
	t2 = time(NULL);

	printf("found %d primes using raw_test, cost %ld secs\n", count,t2-t1);

	return 0;
}
