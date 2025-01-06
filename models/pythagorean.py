from pydantic import BaseModel, field_validator

class PythagoreanTriplesRequest(BaseModel):
    max_hypotenuse: int

    @field_validator("max_hypotenuse")
    def validate_positive_hypotenuse(cls, v):
        if v <= 0:
            raise ValueError("Max hypotenuse must be a positive integer.")
        return v
