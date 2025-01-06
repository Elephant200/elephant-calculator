from pydantic import BaseModel, validator
from decimal import Decimal

class ArithmeticOperation(BaseModel):
    operand1: str
    operand2: str

    @validator("operand1", "operand2")
    def validate_operands(cls, v):
        try:
            Decimal(v)  # Validate that the operand can be parsed as a decimal
        except Exception as e:
            raise ValueError(f"Invalid operand: {v}. Operands must be numeric. Error: {e}")
        return v


class UnaryOperation(BaseModel):
    operand: str

    @validator("operand")
    def validate_operand(cls, v):
        try:
            Decimal(v)  # Validate that the operand can be parsed as a decimal
        except Exception as e:
            raise ValueError(f"Invalid operand: {v}. Operand must be numeric. Error: {e}")
        return v


class TrigonometricOperation(BaseModel):
    angle: str
    radians: bool = True

    @validator("angle")
    def validate_angle(cls, v):
        try:
            Decimal(v)  # Validate that the angle can be parsed as a decimal
        except Exception as e:
            raise ValueError(f"Invalid angle: {v}. Angle must be numeric. Error: {e}")
        return v

    @validator("radians")
    def validate_radians(cls, v):
        if not isinstance(v, bool):
            raise ValueError(f"Radians must be a boolean value. Received: {v}")
        return v


class RootOperation(BaseModel):
    number: str
    root: str

    @validator("number", "root")
    def validate_numbers(cls, v):
        try:
            Decimal(v)  # Validate that the input can be parsed as a decimal
        except Exception as e:
            raise ValueError(f"Invalid input: {v}. Must be numeric. Error: {e}")
        return v

    @validator("root")
    def validate_positive_root(cls, v):
        if Decimal(v) <= 0:
            raise ValueError("Root must be greater than zero.")
        return v
