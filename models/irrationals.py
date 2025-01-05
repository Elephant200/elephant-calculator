from pydantic import BaseModel

class ArithmeticOperation(BaseModel):
    operand1: str
    operand2: str
    precision: int = 100

class UnaryOperation(BaseModel):
    operand: str
    precision: int = 100

class TrigonometricOperation(BaseModel):
    angle: str
    precision: int = 100
    radians: bool = True

class RootOperation(BaseModel):
    number: str
    root: str
    precision: int = 100