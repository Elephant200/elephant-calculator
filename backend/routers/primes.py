from fastapi import APIRouter
from models.primes import *
from services.primes import isPrime, nthPrime, firstPrimes, strPrimeFacs

router = APIRouter()

@router.post("/is_prime", response_model=bool)
def check_prime(data: PrimeCheck):
    """
    Check if a number is prime.

    Args:
        data (PrimeCheck): Contains the number to check for primality.

    Returns:
        bool: True if the number is prime, otherwise False.
    """
    return isPrime(data.number)

@router.post("/nth_prime", response_model=int)
def find_nth_prime(data: PrimeNth):
    """
    Find the nth prime number.

    Args:
        data (PrimeNth): Contains the position of the prime number to find.

    Returns:
        int: The nth prime number.
    """
    return nthPrime(data.n)

@router.post("/list_primes", response_model=list[int])
def generate_prime_list(data: PrimeList):
    """
    Generate a list of the first n prime numbers.

    Args:
        data (PrimeList): Contains the number of primes to generate.

    Returns:
        list[int]: A list of the first n prime numbers.
    """
    return firstPrimes(data.count)

@router.post("/factorization", response_model=str)
def prime_factorization(data: PrimeFactorization):
    """
    Perform prime factorization of a number.

    Args:
        data (PrimeFactorization): Contains the number to factorize.

    Returns:
        str: A string representation of the prime factors.
    """
    return strPrimeFacs(data.number)
