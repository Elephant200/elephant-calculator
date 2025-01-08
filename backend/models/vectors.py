from pydantic import BaseModel, Field, field_validator, model_validator

class VectorOperation(BaseModel):
    vector1: list[float] = Field(..., description="The first vector for the operation.")
    vector2: list[float] = Field(..., description="The second vector for the operation.")

    @field_validator("vector1", "vector2")
    def validate_vectors(cls, vector):
        if not vector:
            raise ValueError("Vectors must not be empty.")
        if not all(isinstance(x, (int, float)) for x in vector):
            raise ValueError("All elements in the vector must be integers or floats.")
        return vector

    @model_validator(mode="after")
    def validate_matching_dimensions(cls, values):
        if len(values.vector1) != len(values.vector2):
            raise ValueError("vector1 and vector2 must have the same dimensions.")
        return values


class ScalarVectorOperation(BaseModel):
    vector: list[float] = Field(..., description="The vector to scale.")
    scalar: float = Field(..., description="The scalar value for scaling the vector.")

    @field_validator("vector")
    def validate_vector(cls, vector):
        if not vector or not all(isinstance(x, (int, float)) for x in vector):
            raise ValueError("Vector must be a non-empty list of numeric values.")
        return vector

    @field_validator("scalar")
    def validate_scalar(cls, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Scalar must be a numeric value (int or float).")
        return scalar
