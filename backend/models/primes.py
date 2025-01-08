from pydantic import BaseModel, Field, field_validator

class PrimeCheck(BaseModel):
    number: int = Field(..., description="The number to check for primality.")

    @field_validator("number")
    def validate_positive_integer(cls, v):
        if v <= 1:
            raise ValueError("Number must be greater than 1 to check for primality.")
        return v


class PrimeNth(BaseModel):
    n: int = Field(..., description="The position of the prime number to find.")

    @field_validator("n")
    def validate_positive_index(cls, v):
        if v <= 0:
            raise ValueError("The value of n must be a positive integer.")
        return v


class PrimeList(BaseModel):
    count: int = Field(..., description="The number of primes to generate.")

    @field_validator("count")
    def validate_positive_count(cls, v):
        if v <= 0:
            raise ValueError("The count must be a positive integer.")
        return v


class PrimeFactorization(BaseModel):
    number: int = Field(..., description="The number to factorize into primes.")

    @field_validator("number")
    def validate_positive_integer(cls, v):
        if v <= 1:
            raise ValueError("Number must be greater than 1 for factorization.")
        return v
