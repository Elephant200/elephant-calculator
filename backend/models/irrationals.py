from pydantic import BaseModel, field_validator, Field
from decimal import Decimal

class ArithmeticOperation(BaseModel):
    operand1: str = Field(..., description="The first operand as a string to preserve precision.")
    operand2: str = Field(..., description="The second operand as a string to preserve precision.")

    @field_validator("operand1", "operand2")
    def validate_operands(cls, v):
        try:
            Decimal(v)  # Validate that the operand can be parsed as a decimal
        except Exception as e:
            raise ValueError(f"Invalid operand: {v}. Operands must be numeric. Error: {e}")
        return v


class UnaryOperation(BaseModel):
    operand: str = Field(..., description="The operand for the operation as a string to preserve precision.")

    @field_validator("operand")
    def validate_operand(cls, v):
        try:
            Decimal(v)  # Validate that the operand can be parsed as a decimal
        except Exception as e:
            raise ValueError(f"Invalid operand: {v}. Operand must be numeric. Error: {e}")
        return v


class TrigonometricOperation(BaseModel):
    angle: str = Field(..., description="The angle for the trigonometric operation.")
    radians: bool = Field(True, description="Whether the angle is in radians. Defaults to True.")


    @field_validator("angle")
    def validate_angle(cls, v):
        try:
            Decimal(v)  # Validate that the angle can be parsed as a decimal
        except Exception as e:
            raise ValueError(f"Invalid angle: {v}. Angle must be numeric. Error: {e}")
        return v

    @field_validator("radians")
    def validate_radians(cls, v):
        if not isinstance(v, bool):
            raise ValueError(f"Radians must be a boolean value. Received: {v}")
        return v


class RootOperation(BaseModel):
    number: str = Field(..., description="The number for which the root is to be calculated.")
    root: str = Field(..., description="The degree of the root as a string.")

    @field_validator("number", "root")
    def validate_numbers(cls, v):
        try:
            Decimal(v)  # Validate that the input can be parsed as a decimal
        except Exception as e:
            raise ValueError(f"Invalid input: {v}. Must be numeric. Error: {e}")
        return v

    @field_validator("root")
    def validate_positive_root(cls, v):
        if Decimal(v) <= 0:
            raise ValueError("Root must be greater than zero.")
        return v