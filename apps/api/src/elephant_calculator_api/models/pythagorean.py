from pydantic import BaseModel, Field, field_validator

class PythagoreanTriplesRequest(BaseModel):
    max_hypotenuse: int = Field(..., description="The maximum hypotenuse length for generating triples.")

    @field_validator("max_hypotenuse")
    def validate_positive_hypotenuse(cls, v):
        if v <= 0:
            raise ValueError("Max hypotenuse must be a positive integer.")
        return v
