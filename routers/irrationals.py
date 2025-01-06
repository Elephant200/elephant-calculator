from fastapi import APIRouter, Query
from models.irrationals import ArithmeticOperation, UnaryOperation, TrigonometricOperation, RootOperation
from services.irrationals import *

router = APIRouter()

DEFAULT_PRECISION = 100

@router.post("/add", response_model=str)
def add_numbers(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Add two numbers with specified precision.
    """
    return str(add(data.operand1, data.operand2, precision=precision))


@router.post("/subtract", response_model=str)
def subtract_numbers(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Subtract two numbers with specified precision.
    """
    return str(subtract(data.operand1, data.operand2, precision=precision))


@router.post("/multiply", response_model=str)
def multiply_numbers(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Multiply two numbers with specified precision.
    """
    return str(multiply(data.operand1, data.operand2, precision=precision))


@router.post("/divide", response_model=str)
def divide_numbers(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Divide two numbers with specified precision.
    """
    return str(divide(data.operand1, data.operand2, precision=precision))


@router.post("/sqrt", response_model=str)
def sqrt_number(data: UnaryOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the square root of a number with specified precision.
    """
    return str(sqrt(data.operand, precision=precision))


@router.post("/power", response_model=str)
def power_number(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Raise a number to a power with specified precision.
    """
    return str(power(data.operand1, int(data.operand2), precision=precision))


@router.get("/pi", response_model=str)
def compute_pi(precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the value of π with specified precision.
    """
    return str(pi(precision=precision))


@router.get("/e", response_model=str)
def compute_e(precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the value of e with specified precision.
    """
    return str(advancedE(precision=precision))


@router.post("/sin", response_model=str)
def compute_sin(data: TrigonometricOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the sine of an angle with specified precision.
    """
    return str(sin(data.angle, precision=precision, rad=data.radians))


@router.post("/cos", response_model=str)
def compute_cos(data: TrigonometricOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the cosine of an angle with specified precision.
    """
    return str(cos(data.angle, precision=precision, rad=data.radians))


@router.post("/tan", response_model=str)
def compute_tan(data: TrigonometricOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the tangent of an angle with specified precision.
    """
    return str(tan(data.angle, precision=precision, rad=data.radians))


@router.post("/arcsin", response_model=str)
def compute_arcsin(data: UnaryOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the arcsine of a number with specified precision.
    """
    return str(arcsin(data.operand, precision=precision))


@router.post("/arccos", response_model=str)
def compute_arccos(data: UnaryOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the arccosine of a number with specified precision.
    """
    return str(arccos(data.operand, precision=precision))


@router.post("/arctan", response_model=str)
def compute_arctan(data: UnaryOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the arctangent of a number with specified precision.
    """
    return str(arctan(data.operand, precision=precision))
