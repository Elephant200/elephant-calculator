from fastapi import APIRouter
from services.primes import *

router = APIRouter()

@router.post("/is_prime", response_model=bool)
def check_prime(data: int):
    return isPrime(data)

@router.post("/nth_prime", response_model=int)
def get_nth_prime(data: int):
    return nthPrime(data)

@router.post("/first_primes", response_model=list)
def list_first_primes(data: int):
    return firstPrimes(data)

@router.post("/factorization", response_model=str)
def prime_factorization(data: int):
    return strPrimeFacs(data)
