from pydantic import BaseModel, field_validator

class TriangleRequest(BaseModel):
    a: float = None
    b: float = None
    c: float = None
    A: float = None
    B: float = None
    C: float = None

    @field_validator("a", "b", "c")
    def validate_positive_sides(cls, v, field):
        if v is not None and v <= 0:
            raise ValueError(f"{field.name} (side length) must be greater than zero.")
        return v

    @field_validator("A", "B", "C")
    def validate_angle_range(cls, v, field):
        if v is not None and (v <= 0 or v >= 180):
            raise ValueError(f"{field.name} (angle) must be in the range (0, 180) degrees.")
        return v
