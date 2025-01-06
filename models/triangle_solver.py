from pydantic import BaseModel, Field, field_validator

class TriangleRequest(BaseModel):
    a: float = Field(None, description="Length of side a (optional).")
    b: float = Field(None, description="Length of side b (optional).")
    c: float = Field(None, description="Length of side c (optional).")
    A: float = Field(None, description="Angle opposite side a, in degrees (optional).")
    B: float = Field(None, description="Angle opposite side b, in degrees (optional).")
    C: float = Field(None, description="Angle opposite side c, in degrees (optional).")

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

    @field_validator(mode="before")
    def validate_sufficient_inputs(cls, values):
        provided = sum(1 for v in values.values() if v is not None)
        if provided < 3:
            raise ValueError("At least three parameters, including one side, must be provided.")
        return values
