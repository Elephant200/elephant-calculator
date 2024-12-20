from math import sqrt, floor, log


def isPrime(num):
	if num <= 1: return False
	if num <= 3: return True
	if num % 2 == 0 or num % 3 == 0:
		return False
	if num % 6 != 1 and num % 6 != -1: # All primes except 2 and 3 are either 1 more or 1 less than a multiple of 6
		return False
	for i in range(5, floor(sqrt(num)) + 1, 2):
		if num % i == 0: 
			return False
	return True


def nthPrime(n):
	count, test = 0, 1
	while count < n:
		test += 1
		if isPrime(test): count += 1
	return test


def firstPrimes(n):
	# Uses Sieve of Eratosthenes to generate primes efficiently
	if n < 1:
			return []
	limit = n * (floor(log(n)) + 1) # approximate upper limit for primes 
	is_prime = [True] * limit
	p = 2
	while p * p < limit:
			if is_prime[p]:
					for i in range(p * p, limit, p):
							is_prime[i] = False
			p += 1
	primes = [p for p in range(2, limit) if is_prime[p]]
	return primes[:n]


def primeFactorize(n):
	factorList = {}
	i = 2
	while n > 1:
		if n % i == 0:
			try:
				factorList[i] += 1
			except:
				factorList[i] = 1
			n /= i
			i -= 1
		i += 1
	return factorList


def strPrimeFacs(n):
	factorList = primeFactorize(n)
	return ' x '.join(f"{prime}^{factorList[prime]}" if factorList[prime] > 1 else f"{prime}" for prime in factorList)