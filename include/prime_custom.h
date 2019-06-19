/*******************************************************************************
 * DANIEL'S ALGORITHM IMPLEMENTAIONS
 *
 *  /\  |  _   _  ._ o _|_ |_  ._ _   _ 
 * /--\ | (_| (_) |  |  |_ | | | | | _> 
 *         _|                      
 *
 * PRIME TEST FUNCTION
 *
 * http://en.wikipedia.org/wiki/Primality_test
 * http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
 *
 ******************************************************************************/
#ifndef ALGO_PRIME_H__
#define ALGO_PRIME_H__

#include <stdlib.h>
#include <math.h>
#include "imath.h"

namespace alg {
	/**
	 * check whether a given number is a prime number.
	 * using naive method.
	 */
	static bool test_prime(unsigned int n, int* primos, int* last_index) {

		for (int i = 0; i < (*last_index) && primos[i]*primos[i] < n; i++) {
			if (n % primos[i] == 0) {
				return false;
			}
		}

		primos[(*last_index)]=n;
		(*last_index)++;

		return true;
	}

	/**
	 * http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test 
	 */
	
}

#endif //
