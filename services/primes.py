import os
from math import sqrt, floor, log


def calculate_columns(column_width):
    """
    Calculate the number of columns that can fit in the terminal based on the column width.
    """
    terminal_width = os.get_terminal_size().columns
    return max(1, terminal_width // column_width)


def calculate_column_width(limit):
    """
    Calculate the column width based on the largest possible prime within the limit.
    """
    return len(str(limit)) + 4  # Add padding for spacing


def print_in_columns(item, column_width, count, columns):
    """
    Prints a single item in the appropriate column layout.
    """
    print(f"{item:<{column_width}}", end="")
    if (count + 1) % columns == 0:
        print()


def firstPrimes(n, printIt=False):
    """
    Uses Sieve of Eratosthenes to generate the first n primes, printing them in columns as they are generated.
    """
    if n < 1:
        return []
    
    limit = n * (floor(log(n)) + 1)  # approximate upper limit for primes
    is_prime = [True] * limit
    p = 2

    primes = []
    count = 0

    if printIt:
        column_width = calculate_column_width(limit)
        columns = calculate_columns(column_width)

    while p * p < limit:
        if is_prime[p]:
            for i in range(p * p, limit, p):
                is_prime[i] = False
        p += 1

    for p in range(2, limit):
        if is_prime[p]:
            primes.append(p)
            if printIt:
                print_in_columns(p, column_width, count, columns)
                count += 1
            if len(primes) >= n:
                break

    if printIt and count % columns != 0:
        print()
    return primes


def nthPrime(n):
    """
    Finds the nth prime using a simple increment and isPrime check.
    """
    count, test = 0, 1
    while count < n:
        test += 1
        if isPrime(test):
            count += 1
    return test


def isPrime(num):
    """
    Checks if a number is prime using efficient trial division.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    if num % 6 != 1 and num % 6 != -1:
        return False
    for i in range(5, floor(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def primeFactorize(n):
    """
    Factorizes a number into its prime factors.
    """
    factorList = {}
    i = 2
    while n > 1:
        if n % i == 0:
            factorList[i] = factorList.get(i, 0) + 1
            n /= i
        else:
            i += 1
    return factorList


def strPrimeFacs(n):
    """
    Formats prime factors as a string.
    """
    factorList = primeFactorize(n)
    return ' x '.join(f"{prime}^{factorList[prime]}" if factorList[prime] > 1 else f"{prime}" for prime in factorList)
