from fastapi import APIRouter, Query
from models.irrationals import *
from services.irrationals import *
from utils.formatters import trim_trailing_zeroes

router = APIRouter()

DEFAULT_PRECISION = 100

@router.post("/add", response_model=str)
def add_numbers(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Add two numbers with specified precision.

    Args:
        data (ArithmeticOperation): Contains two operands as strings to preserve precision.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The result of the addition as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(add(data.operand1, data.operand2, precision=precision))


@router.post("/subtract", response_model=str)
def subtract_numbers(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Subtract two numbers with specified precision.

    Args:
        data (ArithmeticOperation): Contains two operands as strings to preserve precision.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The result of the subtraction as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(subtract(data.operand1, data.operand2, precision=precision))


@router.post("/multiply", response_model=str)
def multiply_numbers(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Multiply two numbers with specified precision.

    Args:
        data (ArithmeticOperation): Contains two operands as strings to preserve precision.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The result of the multiplication as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(multiply(data.operand1, data.operand2, precision=precision))


@router.post("/divide", response_model=str)
def divide_numbers(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Divide two numbers with specified precision.

    Args:
        data (ArithmeticOperation): Contains two operands as strings to preserve precision.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The result of the division as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(divide(data.operand1, data.operand2, precision=precision))


@router.post("/sqrt", response_model=str)
def sqrt_number(data: UnaryOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the square root of a number with specified precision.

    Args:
        data (UnaryOperation): Contains the operand as a string to preserve precision.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The square root of the operand as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(sqrt(data.operand, precision=precision))


@router.post("/power", response_model=str)
def power_number(data: ArithmeticOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Raise a number to a power with specified precision.

    Args:
        data (ArithmeticOperation): Contains the base and exponent as strings to preserve precision.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The result of the exponentiation as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(power(data.operand1, int(data.operand2), precision=precision))


@router.get("/pi", response_model=str)
def compute_pi(precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the value of π with specified precision.

    Args:
        precision (int, optional): The precision for the calculation. Defaults to 100.

    Returns:
        str: The value of π as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(pi(precision=precision))


@router.get("/e", response_model=str)
def compute_e(precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the value of e with specified precision.

    Args:
        precision (int, optional): The precision for the calculation. Defaults to 100.

    Returns:
        str: The value of e as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(e(precision=precision))


@router.post("/sin", response_model=str)
def compute_sin(data: TrigonometricOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the sine of an angle with specified precision.

    Args:
        data (TrigonometricOperation): Contains the angle (in radians or degrees) and whether the angle is in radians.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The sine of the angle as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(sin(data.angle, precision=precision, rad=data.radians))


@router.post("/cos", response_model=str)
def compute_cos(data: TrigonometricOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the cosine of an angle with specified precision.

    Args:
        data (TrigonometricOperation): Contains the angle (in radians or degrees) and whether the angle is in radians.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The cosine of the angle as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(cos(data.angle, precision=precision, rad=data.radians))


@router.post("/tan", response_model=str)
def compute_tan(data: TrigonometricOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the tangent of an angle with specified precision.

    Args:
        data (TrigonometricOperation): Contains the angle (in radians or degrees) and whether the angle is in radians.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The tangent of the angle as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(tan(data.angle, precision=precision, rad=data.radians))


@router.post("/arcsin", response_model=str)
def compute_arcsin(data: UnaryOperation, precision: int = Query(DEFAULT_PRECISION, description="Precision for the calculation")):
    """
    Compute the arcsine of a number with specified precision.

    Args:
        data (UnaryOperation): Contains the operand as a string to preserve precision.
        precision (int, optional): The precision for the operation. Defaults to 100.

    Returns:
        str: The arcsine of the operand as a string.
    """
    if precision < 1:
        raise ValueError("Precision must be positive.")
    return trim_trailing_zeroes(arcsin(data.operand, precision=precision))
