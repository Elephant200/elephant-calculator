from pydantic import BaseModel

class ArithmeticOperation(BaseModel):
    operand1: str
    operand2: str  

class UnaryOperation(BaseModel):
    operand: str

class TrigonometricOperation(BaseModel):
    angle: str
    radians: bool = True

class RootOperation(BaseModel):
    number: str
    root: str