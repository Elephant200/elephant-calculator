from fastapi import APIRouter
from models.irrationals import *
from services.irrationals import *

router = APIRouter()

@router.post("/add", response_model=str)
def add_numbers(data: ArithmeticOperation):
    return str(add(data.operand1, data.operand2, data.precision))

@router.post("/subtract", response_model=str)
def subtract_numbers(data: ArithmeticOperation):
    return str(subtract(data.operand1, data.operand2, data.precision))

@router.post("/multiply", response_model=str)
def multiply_numbers(data: ArithmeticOperation):
    return str(multiply(data.operand1, data.operand2, data.precision))

@router.post("/divide", response_model=str)
def divide_numbers(data: ArithmeticOperation):
    return str(divide(data.operand1, data.operand2, data.precision))

@router.post("/sqrt", response_model=str)
def calculate_sqrt(data: UnaryOperation):
    return str(sqrt(data.operand, data.precision))

@router.post("/nroot", response_model=str)
def calculate_nroot(data: RootOperation):
    return str(nRoot(data.number, data.root, data.precision))

@router.post("/power", response_model=str)
def calculate_power(data: ArithmeticOperation):
    return str(power(data.operand1, data.operand2, data.precision))

@router.get("/pi", response_model=str)
def calculate_pi(precision: int = 100):
    return str(pi(precision))

@router.get("/e", response_model=str)
def calculate_e(precision: int = 100):
    return str(taylorE(precision))

@router.post("/sin", response_model=str)
def calculate_sin(data: TrigonometricOperation):
    return str(sin(data.angle, data.precision, data.radians))

@router.post("/cos", response_model=str)
def calculate_cos(data: TrigonometricOperation):
    return str(cos(data.angle, data.precision, data.radians))

@router.post("/tan", response_model=str)
def calculate_tan(data: TrigonometricOperation):
    return str(tan(data.angle, data.precision, data.radians))

@router.post("/arcsin", response_model=str)
def calculate_arcsin(data: TrigonometricOperation):
    return str(arcsin(data.angle, data.precision, not data.radians))

@router.post("/arccos", response_model=str)
def calculate_arccos(data: TrigonometricOperation):
    return str(arccos(data.angle, data.precision, not data.radians))

@router.post("/arctan", response_model=str)
def calculate_arctan(data: TrigonometricOperation):
    return str(arctan(data.angle, data.precision, not data.radians))
