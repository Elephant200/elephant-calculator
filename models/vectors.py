from pydantic import BaseModel, field_validator

class VectorOperation(BaseModel):
    vector1: list[float]
    vector2: list[float]

    @field_validator("vector1", "vector2")
    def validate_vectors(cls, v, field):
        if not v:
            raise ValueError(f"{field.name} must not be empty.")
        if not all(isinstance(x, (int, float)) for x in v):
            raise ValueError(f"All elements in {field.name} must be numeric (int or float).")
        return v

    @field_validator("vector2")
    def validate_matching_dimensions(cls, v, values):
        vector1 = values.get("vector1")
        if vector1 and len(vector1) != len(v):
            raise ValueError("vector1 and vector2 must have the same dimensions.")
        return v


class ScalarVectorOperation(BaseModel):
    vector: list[float]
    scalar: float

    @field_validator("vector")
    def validate_vector(cls, v):
        if not v:
            raise ValueError("vector must not be empty.")
        if not all(isinstance(x, (int, float)) for x in v):
            raise ValueError("All elements in vector must be numeric (int or float).")
        return v

    @field_validator("scalar")
    def validate_scalar(cls, v):
        if not isinstance(v, (int, float)):
            raise ValueError("scalar must be a numeric value (int or float).")
        return v
