from pydantic import BaseModel, Field, field_validator, model_validator

class TriangleRequest(BaseModel):
    a: float | None = Field(None, description="Length of side a (optional).")
    b: float | None = Field(None, description="Length of side b (optional).")
    c: float | None = Field(None, description="Length of side c (optional).")
    A: float | None = Field(None, description="Angle opposite side a, in degrees (optional).")
    B: float | None = Field(None, description="Angle opposite side b, in degrees (optional).")
    C: float | None = Field(None, description="Angle opposite side c, in degrees (optional).")

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

    @model_validator(mode="after")
    def validate_sufficient_inputs(cls, values):
        """
        Ensure at least three inputs, including one side, are provided.
        """
        sides = [values.a, values.b, values.c]
        angles = [values.A, values.B, values.C]

        # Count the number of non-None values
        provided_sides = sum(1 for side in sides if side is not None)
        provided_angles = sum(1 for angle in angles if angle is not None)

        if provided_sides + provided_angles < 3 or provided_sides < 1:
            raise ValueError("At least three parameters, including one side, must be provided.")

        return values