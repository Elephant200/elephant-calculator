from pydantic import BaseModel

class PrimeCheck(BaseModel):
    number: int

class PrimeNth(BaseModel):
    n: int

class PrimeList(BaseModel):
    count: int

class PrimeFactorization(BaseModel):
    number: int