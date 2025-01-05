from fastapi import APIRouter
from models.primes import *
from services.primes import *

router = APIRouter()

@router.post("/is_prime", response_model=bool)
def check_prime(data: PrimeCheck):
    return isPrime(data.number)

@router.post("/nth_prime", response_model=int)
def get_nth_prime(data: PrimeNth):
    return nthPrime(data.n)

@router.post("/generate", response_model=list)
def list_first_primes(data: PrimeList):
    return firstPrimes(data.count)

@router.post("/factorization", response_model=str)
def prime_factorization(data: PrimeFactorization):
    return strPrimeFacs(data.number)
